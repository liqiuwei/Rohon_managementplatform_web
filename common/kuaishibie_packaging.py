import base64
import json
import requests


def base64_api(img, uname='16600281508', pwd='15003940322'):
    """快识别接口识别验证码"""
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


# http://www.kuaishibie.cn/
# if __name__ == "__main__":
#     img_path = "C:/Users/Administrator/Desktop/file.jpg"
#     result = base64_api(uname='16600281508', pwd='15003940322', img='123.png')
#     print(result)
