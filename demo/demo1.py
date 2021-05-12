import cx_Oracle
# class ManagementPlatform():
#
#     def __init__(self):
#         self.parameter = None
#
#     def selective_type(self):
#         """选择登录还是注册"""
#         print("提示:【1】登录、【2】注册")
#         parameter = input('请选择：')
#         if parameter == '2':
#             self.register()
#         elif parameter == '1':
#             self.login()
#
#     @staticmethod
#     def register():
#         """注册"""
#         user = input('请输入账号：')
#         pwd = input('请输入密码：')
#         affirm_pwd = input('请再次输入密码：')
#         if pwd == affirm_pwd:
#             with open('text.txt', 'a') as f:
#                 f.write(user)
#                 f.write(pwd)
#         else:
#             print('两次密码不一致')
#
#     @staticmethod
#     def login():
#         """登录"""
#         user = input('请输入账号：')
#         pwd = input('请输入密码：')
#         with open('text.txt', 'r') as f:
#             data = f.read()
#         if user and pwd in data:
#             print('登录成功')
#         else:
#             print('账号或密码错误')
#
#
# ManagementPlatform().selective_type()
