# import os
# from aip import AipOcr
#
# from config.config import DATA_PATH
#
#
# class baiduApi:
#     """识别图片里的文字"""
#
#     def __init__(self, APP_ID='23002661', API_KEY='eUr6QpGP244AiG07kOu7h0p8',
#                  SECRET_KEY='h6v0uirki8Sr0XF7ZEmGvPcIFHAv6EQb'):
#         """
#         APP_ID = '你的 App ID'
#         API_KEY = '你的 Api Key'
#         SECRET_KEY = '你的 Secret Key'
#         """
#         self.APP_ID = APP_ID
#         self.API_KEY = API_KEY
#         self.SECRET_KEY = SECRET_KEY
#         self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
#
#     def get_file_content(self, imageFile):
#         with open(imageFile, 'rb') as fp:
#             return fp.read()
#
#     def getWordFromImage(self, imageFile):
#         image = self.get_file_content(imageFile)
#         result = self.client.basicGeneral(image)
#         return result
#
#     def data(self, file):
#         data = baiduApi(self.APP_ID, self.API_KEY, self.SECRET_KEY)
#         imageFile = file
#         data = data.getWordFromImage(imageFile)
#         return data


# if __name__ == "__main__":
#
#     data = os.path.join(DATA_PATH, '1605772681(1).jpg')
#     shuj = baiduApi().data(data)
#     print(shuj['words_result'][0]['words'])


