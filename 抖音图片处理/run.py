from 抖音图片处理.main import main

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:

        print("\n程序已终止")
    except Exception as e:
        print(f"\n程序出错: {e}")
    finally:
        input("\n按回车键退出...") 