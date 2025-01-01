import os
from 抖音图片处理.douyin_spider import run_spider
from 抖音图片处理.pipelines import DownloadPipeline
from 抖音图片处理.settings import DOWNLOAD_DIR
from 抖音图片处理.utils import validate_url

def get_valid_url():
    """获取有效的URL"""
    while True:
        url = input("请输入抖音用户主页URL: ").strip()
        if not url:
            print("URL不能为空！")
            continue
            
        if not validate_url(url):
            print("URL格式不正确！请输入正确的抖音用户主页URL")
            continue
            
        return url

def get_user_choice():
    """获取用户选择"""
    while True:
        choice = input("\n是否继续下载其他用户? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("请输入 y 或 n")

def main():
    while True:
        # 获取URL
        url = get_valid_url()
        
        print("\n开始爬取...")
        # 运行爬虫获取数据
        items = run_spider(url)
        
        if not items:
            print("未获取到任何数据！")
            if not get_user_choice():
                break
            continue
            
        # 下载图片
        print("\n开始下载图片...")
        pipeline = DownloadPipeline(DOWNLOAD_DIR)
        for item in items:
            pipeline.process_item(item)
        pipeline.close()  # 显示下载统计信息
        
        # 询问是否继续
        if not get_user_choice():
            break
            
    print("\n程序结束，感谢使用！")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序已终止")
    except Exception as e:
        print(f"\n程序出错: {e}")
    finally:
        input("\n按回车键退出...")