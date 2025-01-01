import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 下载目录
DOWNLOAD_DIR = os.path.join(ROOT_DIR, 'downloads')

# 存储登录状态的目录和文件
AUTH_DIR = os.path.join(ROOT_DIR, 'auth')
AUTH_FILE = os.path.join(AUTH_DIR, 'storage.json')

# Cookie文件
COOKIE_FILE = os.path.join(AUTH_DIR, 'cookie.txt')

# 确保目录存在
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(AUTH_DIR, exist_ok=True)

# 下载设置
DOWNLOAD_DELAY = 1  # 下载延迟
DOWNLOAD_TIMEOUT = 10  # 下载超时
RETRY_TIMES = 3  # 重试次数

# 请求头设置
DEFAULT_HEADERS = {
    'cookie':'passport_csrf_token=1f95c5a726fdab67469728838f84016a; passport_csrf_token_default=1f95c5a726fdab67469728838f84016a; bd_ticket_guard_client_web_domain=2; ttwid=1%7CB1TDXTXgoDE8FEovQTWCH90YLl8s9YCkAB_I8Xqnavs%7C1734360441%7Ca0c49f5c5bfe4709eb85837012cdec0f87931428e0dfc62b759c9b129468a06f; UIFID_TEMP=c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0a562825fde2a47b8dd6523e1cb636223497a9acc41b6f401f86f753b107f44a217d3e26d3a5d0cbdc8abea8bb1b1cca2b2a7b27a91194069edde9af4fd8a318d76ae7293668304147b7a095d44dd5792; hevc_supported=true; dy_swidth=1440; dy_sheight=900; fpk1=U2FsdGVkX1+dAgRsRZ3KEqMvmYIJw3dFg+psSAknr9E9uFbgjNj5lSEiw8Tv5K/7WYV6ABMjHN4A51okF9p2cA==; fpk2=f51bb482c660d0eeadd1f058058a2b35; s_v_web_id=verify_m4z55w1b_wOuKmPd9_4LBG_42zj_A85o_HFY4Pnu1ino7; xgplayer_user_id=648675360165; UIFID=c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0a562825fde2a47b8dd6523e1cb636223497a9acc41b6f401f86f753b107f44a20d904518ae7a2c333fa12c9e94837849519a2197c6240d30c15ea348b8055ebb9cc45149ca476692cf5fa7e1767e646b8f922d423ccca85ec7d4519ab384eb3e6532e2c55154a2b173ecf62fafbd8bc147940c78d3d1640191b1b752d86282e32146bf8c1bea62ce95eb4b8377810137dca0406afdd493729b4dde9633315eba; passport_assist_user=CkDX4Jubycu4FsICYuNjFiUG2LX_nJcA2zUr84gRlew-rhi7WtZFB4QhCWIS0N2cDSG0V7bcz_S9Aj2EqUgwjl3BGkoKPCgSbY1iNcYadAWBR4YAI-HMVh-jm-LyI0C1bQPXgGWWb-LWqWtoZNQnPDIAsd-THUgCEtFCmzGAOH4GKxCp4OQNGImv1lQgASIBAxRpknU%3D; n_mh=HZExvFxTnBkRDz4-lTA8uryB0k3Wi5r5qmsAwYUrBpU; sso_uid_tt=d7143e95a9f27d921f33e19df8375c39; sso_uid_tt_ss=d7143e95a9f27d921f33e19df8375c39; toutiao_sso_user=e122392fbbfbc36f8473c07a93a19eec; toutiao_sso_user_ss=e122392fbbfbc36f8473c07a93a19eec; sid_ucp_sso_v1=1.0.0-KGNlYjRjODRmNTk2OTZkNDhlYTJkZDAwNjA1NzVhYjc5YzE3YTIxMDkKIQi-weC14o23ARCIu567BhjvMSAMMPPXiZ8GOAZA9AdIBhoCbGYiIGUxMjIzOTJmYmJmYmMzNmY4NDczYzA3YTkzYTE5ZWVj; ssid_ucp_sso_v1=1.0.0-KGNlYjRjODRmNTk2OTZkNDhlYTJkZDAwNjA1NzVhYjc5YzE3YTIxMDkKIQi-weC14o23ARCIu567BhjvMSAMMPPXiZ8GOAZA9AdIBhoCbGYiIGUxMjIzOTJmYmJmYmMzNmY4NDczYzA3YTkzYTE5ZWVj; login_time=1734843785297; passport_auth_status=ede02ddcf4f3aa0f7b1f52f6e1acb02b%2C; passport_auth_status_ss=ede02ddcf4f3aa0f7b1f52f6e1acb02b%2C; uid_tt=d3a5b04a3c71ccb02cecf97dd6cbe7f5; uid_tt_ss=d3a5b04a3c71ccb02cecf97dd6cbe7f5; sid_tt=c07c7fd6e063b07f719ba81cebf39080; sessionid=c07c7fd6e063b07f719ba81cebf39080; sessionid_ss=c07c7fd6e063b07f719ba81cebf39080; is_staff_user=false; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=94b5c75ddcd609c96a593ff75eda1882; __security_server_data_status=1; sid_guard=c07c7fd6e063b07f719ba81cebf39080%7C1734843796%7C5183991%7CThu%2C+20-Feb-2025+05%3A03%3A07+GMT; sid_ucp_v1=1.0.0-KDE4MWVlYzcwY2ZiN2ZhMGUwYTU4MjU4MzEzZjA2Mzk0MTliMmUzNzIKGwi-weC14o23ARCUu567BhjvMSAMOAZA9AdIBBoCbGYiIGMwN2M3ZmQ2ZTA2M2IwN2Y3MTliYTgxY2ViZjM5MDgw; ssid_ucp_v1=1.0.0-KDE4MWVlYzcwY2ZiN2ZhMGUwYTU4MjU4MzEzZjA2Mzk0MTliMmUzNzIKGwi-weC14o23ARCUu567BhjvMSAMOAZA9AdIBBoCbGYiIGMwN2M3ZmQ2ZTA2M2IwN2Y3MTliYTgxY2ViZjM5MDgw; is_dash_user=1; store-region=cn-zj; store-region-src=uid; my_rd=2; SEARCH_RESULT_LIST_TYPE=%22single%22; __security_mc_1_s_sdk_crypt_sdk=1f66bff9-4cc8-a201; __security_mc_1_s_sdk_cert_key=9c929100-4f7c-a7bd; __security_mc_1_s_sdk_sign_data_key_web_protect=6fd2511a-4d8f-9b21; __security_mc_1_s_sdk_sign_data_key_web_protect_time=bc1a31d4-4a60-b524; live_use_vvc=%22false%22; xgplayer_device_id=3607647305; publish_badge_show_info=%220%2C0%2C0%2C1735461039560%22; WallpaperGuide=%7B%22showTime%22%3A1734843839438%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A71%2C%22cursor2%22%3A22%2C%22hoverTime%22%3A1734843840075%7D; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A900%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; volume_info=%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; strategyABtestKey=%221735666904.597%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; download_guide=%220%2F%2F1%22; __ac_nonce=06774d747001678f5a6f2; __ac_signature=_02B4Z6wo00f01hKZypgAAIDCJb0Ox2o0.Q4Suc4AAOPg63; IsDouyinActive=true; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA03Mwj75hYjHCYULcZxNon5Xj0Mvp_LzapyK_W2FRiDw%2F1735747200000%2F0%2F0%2F1735711137059%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA03Mwj75hYjHCYULcZxNon5Xj0Mvp_LzapyK_W2FRiDw%2F1735747200000%2F0%2F0%2F1735711737060%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTFh2VVJKWjNmUzQ3U3hiTkZjcDlHaGtiNkdhaU56WmZXSkdQR3BueFdZMjVMbC8wanJSbFM5ckcyWSs4RytydllYUDFldktGVk9GczV1RW81OU1acXc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; passport_fe_beating_status=true; odin_tt=722bc663c11c25f0287ad97ea1ec97f90b6eda4f5e5084de0ee41d4e31beb158cf78cd99794cb8a4a0c309a997b34729; csrf_session_id=be3f53e8b8fd5567634fd056e9e71bad',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Referer': 'https://www.douyin.com/'
}

# 图片存储设置
IMAGES_STORE = 'downloads' 