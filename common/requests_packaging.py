import requests


def visit(url, params=None, data=None, method='get', json=None, **kwargs):
    """访问接口获取接口返回，json格式"""
    res = requests.request(method, url, params=params, data=data, json=json, **kwargs)
    try:
        return res.json()
    except Exception as err:
        raise err
