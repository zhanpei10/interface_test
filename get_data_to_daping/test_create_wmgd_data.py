# 添加文明工地数据
import pytest
from common.common_method import *
import json
from api_keyword.interface_keyword import InterfaceKey
import ast
import requests


@pytest.mark.parametrize('data', get_data_by_yaml('./test_wmgd.yaml'))
def test_create_wmgd(data):
    '''
    兴建文明工地
    :param data:
    :return:
    '''
    with open(r'./test1.txt', mode='rt', encoding='utf-8') as f1:
        for line in f1:
            res = ast.literal_eval(line)
            for key, value in data.items():
                if key in res:
                    data[key] = res[key]
            url = 'http://10.111.32.82:10219/whale-openapi/construction'
            headers = {
                'accessToken': get_access_token()
            }
            res = requests.post(url=url, json=data, headers=headers)
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg')
            break


if __name__ == '__main__':
    # pytest.main(['./test_create_wmgd_data.py::test_create_wmgd'])
    url = 'http://10.242.212.164:10212/whale-openapi/CaseManageService/DetailCase/'
    params = {
        'id' : 36532
    }

    res = requests.get(url=url, params=params)

    print(res.text)
