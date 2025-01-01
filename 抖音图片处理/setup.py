from setuptools import setup, find_packages
import subprocess
import sys

def install_playwright_browsers():
    """安装 Playwright 浏览器"""
    try:
        print("正在安装 Playwright 浏览器...")
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        print("Playwright 浏览器安装成功")
    except Exception as e:
        print(f"Playwright 浏览器安装失败: {e}")

class PostInstallCommand:
    """安装后的配置命令"""
    def run(self):
        install_playwright_browsers()

setup(
    name='douyin-spider',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'playwright',
        'requests',
        'asyncio',
        'aiohttp',  # 用于异步请求
        'tqdm'      # 用于进度条显示
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    python_requires='>=3.7',
    author='Your Name',
    author_email='your.email@example.com',
    description='抖音图片爬虫',
    long_description='一个用于抓取抖音用户图片的爬虫工具',
    keywords='douyin, spider, crawler, image downloader',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
