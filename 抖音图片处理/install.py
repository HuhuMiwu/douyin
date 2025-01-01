import os
import sys
import subprocess

def install_requirements():
    """安装所有依赖"""
    try:
        print("开始安装...")
        
        # 安装 pip 依赖
        subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True)
        
        # 安装 playwright
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
        
        # 安装 playwright 浏览器
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        
        print("\n所有依赖安装成功！")
        print("\n现在你可以运行 'python main.py' 来启动爬虫")
        
    except Exception as e:
        print(f"\n安装过程出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements() 