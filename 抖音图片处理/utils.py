import os
import re
import logging

logger = logging.getLogger(__name__)

def validate_url(url):
    """验证抖音用户主页URL格式"""
    pattern = r'https?://(?:www\.)?douyin\.com/user/[A-Za-z0-9_-]+'
    return bool(re.match(pattern, url)) 