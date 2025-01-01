import os
import time
import random
import requests
import logging
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from urllib3.exceptions import InsecureRequestWarning

# 禁用 SSL 警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logger = logging.getLogger(__name__)

class DownloadPipeline:
    def __init__(self, download_dir, max_workers=5):
        self.download_dir = download_dir
        self.max_workers = max_workers
        self.download_stats = defaultdict(int)  # 用于统计下载信息
        self.download_queue = Queue()  # 下载队列
        self.stats_lock = threading.Lock()  # 统计信息的线程锁
        
    @classmethod
    def from_settings(cls, settings):
        return cls(
            download_dir=settings.DOWNLOAD_DIR,
            max_workers=settings.get('DOWNLOAD_THREADS', 5)
        )
        
    def _download_image(self, task):
        """下载单个图片的工作函数"""
        url, filepath = task
        try:
            # 随机等待0.5-2秒
            time.sleep(random.uniform(0.5, 2))
            
            # 下载图片，禁用 SSL 验证
            response = requests.get(url, timeout=10, verify=False)
            response.raise_for_status()
            
            # 保存图片
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            # 更新统计信息（线程安全）
            with self.stats_lock:
                self.download_stats['images'] += 1
                logger.debug(f"下载成功: {os.path.basename(filepath)}")
                
            return True
            
        except Exception as e:
            logger.error(f"下载失败: {os.path.basename(filepath)}, 错误: {e}")
            return False
            
    def process_item(self, item):
        """处理每个作品项"""
        # 创建用户目录
        user_dir = os.path.join(self.download_dir, f"{item.user_name}_{item.douyin_id}")
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
            
        # 准备下载任务
        download_tasks = []
        for idx, url in enumerate(item.image_urls, 1):
            # 构建文件名
            filename = f"{item.title}_{idx:02d}.jpg"
            filepath = os.path.join(user_dir, filename)
            
            # 如果文件已存在，跳过
            if os.path.exists(filepath):
                continue
                
            download_tasks.append((url, filepath))
            
        # 如果有需要下载的图片
        if download_tasks:
            # 使用线程池下载
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                # 提交所有下载任务
                future_to_task = {
                    executor.submit(self._download_image, task): task 
                    for task in download_tasks
                }
                
                # 等待所有任务完成
                success_count = 0
                for future in as_completed(future_to_task):
                    if future.result():
                        success_count += 1
                        
                # 如果有成功下载的图片，更新作品统计
                if success_count > 0:
                    with self.stats_lock:
                        self.download_stats['works'] += 1
                        
            # 每个作品下载完后随机等待1-3秒
            time.sleep(random.uniform(1, 3))
            
    def close(self):
        """完成下载后的汇总信息"""
        logger.info("\n下载统计:")
        logger.info(f"成功下载 {self.download_stats['works']} 个作品")
        logger.info(f"共下载 {self.download_stats['images']} 张图片") 