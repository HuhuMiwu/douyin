import json
import re
import time
import os
import queue
import logging
from DrissionPage import ChromiumPage
from .items import DouyinItem

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DouyinSpider:
    def __init__(self, url=None):
        self.url = url
        self.browser = None
        self.max_retries = 3  # 最大重试次数
        
    def _init_browser(self):
        """初始化浏览器"""
        try:
            self.browser = ChromiumPage()
            self.browser.listen.start('v1/web/aweme/post/')
            return True
        except Exception as e:
            logger.error(f"初始化浏览器失败: {e}")
            return False
            
    def _get_user_info(self):
        """获取用户信息"""
        for attempt in range(self.max_retries):
            try:
                # 等待元素加载
                time.sleep(2)
                
                # 尝试获取用户信息
                user_name = self.browser.ele('.arnSiSbK', timeout=10).text
                douyin_id = self.browser.ele('.OcCvtZ2a', timeout=10).text.split('：')[-1]
                total_count = int(self.browser.ele('.MNSB3oPV', timeout=10).text)
                
                name = f'{user_name}_{douyin_id}'
                logger.info(f'用户: {name}, 作品数: {total_count}')
                return user_name, douyin_id, total_count
                
            except Exception as e:
                logger.error(f"获取用户信息失败 (尝试 {attempt + 1}/{self.max_retries}): {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2)  # 等待后重试
                    continue
                raise  # 重试次数用完，抛出异常
                
    def _load_more(self):
        """加载更多内容"""
        try:
            # 获取可滚动容器元素
            scroll_container = self.browser.ele('x://div[@class="parent-route-container route-scroll-container IhmVuo1S"]')
            if not scroll_container:
                logger.error("未找到可滚动容器")
                return None
                
            # 滚动到底部
            scroll_container.scroll.to_bottom()
            time.sleep(1)
            
            # 往上滚一点
            scroll_container.scroll.up(300)
            time.sleep(0.5)
            
            # 再次滚动到底部
            scroll_container.scroll.to_bottom()
            time.sleep(1)
            
            # 等待API响应
            try:
                res = self.browser.listen.wait(timeout=3)
                if res and res.response and res.response.body:
                    return res.response.body
            except queue.Empty:
                pass
                
            return None
            
        except Exception as e:
            logger.error(f"加载更多失败: {e}")
            return None
            
    def start_crawl(self):
        """开始爬取"""
        items = []
        works_with_images = 0
        total_images = 0
        
        try:
            # 初始化浏览器
            if not self._init_browser():
                logger.error("浏览器初始化失败，程序退出")
                return items
                
            # 访问用户主页
            logger.info("正在访问用户主页...")
            try:
                self.browser.get(self.url)
                time.sleep(3)  # 增加等待时间
            except Exception as e:
                logger.error(f"访问用户主页失败: {e}")
                return items
                
            # 获取用户信息
            try:
                user_name, douyin_id, total_count = self._get_user_info()
            except Exception as e:
                logger.error(f"获取用户信息失败: {e}")
                return items
                
            # 循环加载数据
            page = 1
            no_data_count = 0
            max_no_data = 3  # 连续3次没有新数据就退出
            last_items_count = 0
            
            while page < 100 and len(items) < total_count:  # 修改循环条件
                logger.info(f'============第{page}页============')
                
                # 加载更多数据
                res_json = self._load_more()
                if not res_json:
                    logger.error(f'第{page}页未获取到响应')
                    no_data_count += 1
                    if no_data_count >= max_no_data:
                        logger.info("连续多次未获取到数据，结束爬取")
                        break
                    continue
                
                # 获取作品列表
                image_list = res_json.get('aweme_list', [])
                if not image_list:
                    logger.info("没有更多作品了")
                    break
                    
                logger.info(f"本页获取到 {len(image_list)} 个作品")
                
                # 处理每个作品
                for index in image_list:
                    if len(items) >= total_count:
                        break
                        
                    try:
                        work_id = index['aweme_id']
                        title = index.get('desc', '').strip()
                        if not title:
                            title = f'work_{work_id}'
                        title = re.sub(r'[^\w\s]', '', title)  # 移除非字母数字和空白字符
                        title = re.sub(r'\s+', '_', title)  # 将多个空白字符替换为一个下划线
                        
                        logger.info(f'作品: {title}, ID: {work_id}')
                        
                        # 获取图片列表
                        images_list = index.get('images', [])
                        if not images_list:
                            logger.info("未找到图片数据")
                            # 即使没有图片也添加到items列表，但不增加works_with_images计数
                            items.append(DouyinItem(
                                user_name=user_name,
                                douyin_id=douyin_id,
                                work_id=work_id,
                                title=title,
                                image_urls=[]
                            ))
                            continue
                            
                        # 处理图片
                        image_urls = []
                        for idx, image in enumerate(images_list, 1):
                            image_url = image['url_list'][0]
                            image_urls.append(image_url)
                            total_images += 1
                            
                        # 只有实际有图片URL时才增加计数
                        if image_urls:
                            works_with_images += 1
                            
                        # 添加到结果列表
                        items.append(DouyinItem(
                            user_name=user_name,
                            douyin_id=douyin_id,
                            work_id=work_id,
                            title=title,
                            image_urls=image_urls
                        ))
                        
                    except Exception as e:
                        logger.error(f'处理作品失败: {e}')
                        continue
                
                # 检查是否有新作品
                if len(items) > last_items_count:
                    last_items_count = len(items)
                    no_data_count = 0
                else:
                    no_data_count += 1
                    logger.info(f"未获取到新作品 ({no_data_count}/{max_no_data})")
                
                page += 1
                time.sleep(1)  # 页面间隔
                    
        except KeyboardInterrupt:
            logger.info("\n用户中断程序")
        except Exception as e:
            logger.error(f"爬取过程出错: {e}")
        finally:
            if self.browser:
                try:
                    self.browser.quit()
                except:
                    pass
                    
        return items[:total_count]

def run_spider(url):
    """运行爬虫"""
    try:
        spider = DouyinSpider(url)
        return spider.start_crawl()
    except Exception as e:
        logger.error(f"爬虫运行失败: {e}")
        return [] 