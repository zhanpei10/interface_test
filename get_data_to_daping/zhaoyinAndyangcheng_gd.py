from api_keyword.interface_keyword import InterfaceKey
import time
from common.common_method import *
import random


# 添加噪音数据
def make_zy_data():
    str_time = time.strftime('%Y-%m-%d %H:%M:%S')
    num1 = random.uniform(60, 120)
    url = 'http://10.9.242.39:10620/gms/device-data/access'
    data = {
        "params": [
            {"accessTimeStamp": str_time,
             "dataValue": num1,
             "deviceName": "654321",
             "deviceType": "NOISE",
             "productKey": "这是备注信息字段"
             }
        ]
    }
    res = InterfaceKey().do_post(path=url, json=data)
    # assert_data = get_data_by_json(res.text, 'errorMsg')
    print(res.text)
    # assert assert_data == 'ok'
    print('数据添加成功')


# 添加扬尘数据
def make_yang_cheng():
    str_time = time.strftime('%Y-%m-%d %H:%M:%S')
    num1 = random.uniform(60, 120)
    url = 'http://10.9.242.39:10620/gms/device-data/access'
    data = {
        "params": [
            {"accessTimeStamp": str_time,
             "dataValue": num1,
             "deviceName": "123456",
             "deviceType": "DUST",
             "productKey": "这是备注信息"
             }
        ]
    }
    res = InterfaceKey().do_post(path=url, json=data)
    assert_data = get_data_by_json(res.text, 'errorMsg')
    print(res.text)
    assert assert_data == 'ok'
    print('数据添加成功')


if __name__ == '__main__':
    while True:
        num = 3
        while num > 0:
            make_zy_data()
            # make_yangcheng()
            num = num - 1
        time.sleep(600)
