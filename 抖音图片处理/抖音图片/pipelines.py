
import os
import requests
import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

class DownloadPipeline:
    def __init__(self, download_dir):
        self.download_dir = download_dir
        self.download_stats = defaultdict(int)  # 用于统计下载信息
        
    @classmethod
    def from_settings(cls, settings):
        return cls(
            download_dir=settings.DOWNLOAD_DIR
        )
        
    def process_item(self, item):
        """处理每个作品项"""
        # 创建用户目录
        user_dir = os.path.join(self.download_dir, f"{item.user_name}_{item.douyin_id}")
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
            
        # 下载图片
        for idx, url in enumerate(item.image_urls, 1):
            # 构建文件名
            filename = f"{item.title}_{idx:02d}.jpg"
            filepath = os.path.join(user_dir, filename)
            
            # 如果文件已存在，跳过
            if os.path.exists(filepath):
                continue
                
            try:
                # 下载图片
                response = requests.get(url)
                response.raise_for_status()
                
                # 保存图片
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                    
                # 更新统计信息
                self.download_stats['images'] += 1
                
            except Exception as e:
                logger.error(f"下载失败: {filename}, 错误: {e}")
                
        # 更新作品统计
        if item.image_urls:
            self.download_stats['works'] += 1
            
    def close(self):
        """完成下载后的汇总信息"""
        logger.info("\n下载统计:")
        logger.info(f"成功下载 {self.download_stats['works']} 个作品")
        logger.info(f"共下载 {self.download_stats['images']} 张图片") 