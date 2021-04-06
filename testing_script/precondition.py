# import requests
#
# from middleware.heandler import Hadnler
#
#
#
#
# logging = Hadnler.logger
#
#
# def login_cookie():
#     """登录获取session属性"""
#     session = requests.session()
#     data = {"user.rohon_us_username": "YWRtaW4=",
#             "user.rohon_us_password": "YWRtaW4=",
#             "valicode": ""}
#     url = 'http://192.168.1.61:8080/2.0.59.231_1/user.action'
#     data = session.request('post', url=url, data=data).text
#     try:
#         if data == 'ok*2*extisByWebapps':
#             return session
#     except Exception as err:
#         logging.info('登录失败')
#         raise err
#
# login_cookie()