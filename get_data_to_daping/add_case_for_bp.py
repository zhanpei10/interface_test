# 标品上报事件

import requests
import time

def get_token():
    url = 'https://10.9.242.39:10220/whale-openapi/uums/auth/token'
    data = {
        'packData': "FC3NNVQG5DOQN0apKz/HCIp4dwpe1y1WYbf4IrHFUeQwYCfrnKITkN62Eq2chfMxuw9yWO9BDkReua44VD6aJNopQcu4tJ9WkvmF1PxciaeB5FGvhCpfTbZ7n24pP95u"
    }
    headers = {
        'Connection': 'close',
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res)


# def test_add_case():
#     url =
#     data =
#     headers = {
#         accessToken: get_token
#     }

if __name__ == '__main__':
    res = time.time() + 60*24*60*60
    res1 = time.localtime(res)
    print(time.strftime('%Y-%m-%d', res1))
    print()
