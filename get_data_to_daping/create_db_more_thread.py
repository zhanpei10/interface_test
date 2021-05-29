# 使用多线程的方式创建单兵装备
import requests
from common.common_method import *
from threading import Thread


def create_token(name):
    url = 'http://10.111.32.82:10219/uums/auth/token'
    print(name)
    data = {
        "grantType": "password",
        "identifyCode": "",
        "password": "kobe8888",
        "username": name,
    }
    res = InterfaceKey().do_post(path=url, json=data)
    data = get_data_by_json(res.text, 'accessToken')
    if data:
        return data
    else:
        print(res.text)
        raise '登陆失败，无无法获取token'


def create_db(name):
    url = 'http://10.111.32.82:10219/whale-openapi/individualEquipment/create'
    data = {"equipmentName": "autoTest77777", "equipmentType": 3, "brand": "dsadsdad", "euqipmentModel": "dadadasd",
            "useStatus": 1, "buyDateTimestamp": "2021-06-29", "ownerId": 100537, "accessPlatformStatus": 0,
            "platform": None, "platformName": None, "orgName": None, "equipmentCode": None, "gbNo": None,
            "markNo": None,
            "vmsAddress": None, "protocol": None, "userName": None, "password": None, "platformId": None,
            "mainTabIndex": 1,
            "equipmentCategory": 1}
    headers = {
        'accessToken': create_token(name),
    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)


def task(name):
    create_db(name)


if __name__ == '__main__':
    t1 = Thread(target=task, args=('kobeAdmin006',))
    t2 = Thread(target=task, args=('kobeAdmin009',))
    t3 = Thread(target=task, args=('kobeAdmin001',))
    t4 = Thread(target=task, args=('kobeAdmin012',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
