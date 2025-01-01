import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 下载目录
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), 'downloads')

# 确保目录存在
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 下载设置
DOWNLOAD_THREADS = 5  # 同时下载的最大线程数 