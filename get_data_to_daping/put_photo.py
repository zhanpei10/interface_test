# 上传文件
import requests
from common.common_method import *


def put_p():
    url = 'http://10.111.32.82:10219/whale-general-service/generalservice/put'
    with open(r'../common/import_file/renovation_file_1.jpg', mode='rb') as f1:
        files = {
            'objectFile': f1
        }
        headers = {
            'accessToken': get_access_token()
        }
        res = requests.put(url=url, headers=headers, files=files)
        print(res.text)


if __name__ == '__main__':
    put_p()
