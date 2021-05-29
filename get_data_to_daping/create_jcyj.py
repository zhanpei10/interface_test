# 新增检测预计

import requests
from common.common_method import *


def create_jcyj():
    for i in range(101, 201):
        url = 'http://10.242.212.164:10228/algo_index/algo/' + str(i)
        data = {"appVersion": "10000", "updateAt": 1530583681000, "createAt": 1530583681000, "quality": None,
                "duration": 120000, "panoramicImage": {"format": None, "width": 1920,
                                                       "url": "video_event_panoramic/20201117-d9ba9961-000a580ae0001a-3e0753d0-000863f8",
                                                       "height": 1080}, "alarmStatus": 1, "alarmType": 3021,
                "qualitys": None, "judgeStatus": 1, "appId": "APP0003", "alarmId": "d76d0e375fbbc7f2f673f27272cf4967",
                "capturedAt": 1605650350000, "alarmLevel": 3, "sectionImage": None,
                "camera": {"address": None, "code": None, "deviceCode": None, "platformTaskId": "3s16av8bu8lc",
                           "type": 2,
                           "labels": None, "parentSerial": None, "path": "0-1-9-", "affiliation": [0, 1, 9],
                           "cameraId": None, "regionId": None, "serial": "3s16av8bu8lc", "district": "其它",
                           "name": "渣土车2",
                           "indoor": False, "block": None, "id": 100032,
                           "position": {"latitude": 30.9, "longitude": 121.93069}, "floor": "0",
                           "group": {"zoomLevel": 8, "path": "0-1-9-", "serial": "3s169qpf569s", "name": "渣土车验证",
                                     "id": 9,
                                     "position": None}}, "continuing": 0,
                "sectionLocations": [{"top": 356, "left": 546, "width": 43, "height": 44}]}
        res = requests.put(url=url, json=data)
        print(res)


if __name__ == '__main__':
    create_jcyj()
