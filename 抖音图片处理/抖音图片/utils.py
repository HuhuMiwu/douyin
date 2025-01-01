import os
import re
import requests
from 抖音图片处理.抖音图片.settings import COOKIE_FILE

def save_cookie(cookie):
    """保存cookie到文件"""
    with open(COOKIE_FILE, 'w', encoding='utf-8') as f:
        f.write(cookie)

def load_cookie():
    """从文件加载cookie"""
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return None

def validate_url(url):
    """验证抖音用户主页URL格式"""
    pattern = r'https?://(?:www\.)?douyin\.com/user/[A-Za-z0-9_-]+'
    return bool(re.match(pattern, url))

def check_cookie(cookie):
    """检查cookie是否有效"""
    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # 尝试访问抖音主页
        response = requests.get('https://www.douyin.com/', headers=headers)
        # 如果返回的页面包含特定字符串，说明cookie有效
        return 'login' not in response.url
    except:
        return False 