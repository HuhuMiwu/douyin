class DouyinItem:
    """抖音作品数据项"""
    def __init__(self, user_name, douyin_id, work_id, title, image_urls):
        self.user_name = user_name  # 用户名
        self.douyin_id = douyin_id  # 抖音号
        self.work_id = work_id      # 作品ID
        self.title = title          # 作品标题
        self.image_urls = image_urls # 图片URL列表 