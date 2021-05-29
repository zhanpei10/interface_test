import requests
from common.common_method import *


def import_file():
    url = 'http://10.111.32.82:10219/whale-openapi/individualEquipment/import'
    headers = {
        # 'Accept': 'application/json,text/plain, */*',
        'accessToken': get_access_token(),
          }
    files = {
        'file': open(r'../common/import_file/test_qtzb.xlsx', mode='rb')
    }
    data = {
        'equipmentCategory': 2,
    }
    res = requests.post(url=url, headers=headers, data=data, files=files)
    print(res.text)
    print(res.request.body)
    print(res.request.headers)


if __name__ == '__main__':
    import_file()
