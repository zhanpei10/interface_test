from api_keyword.interface_keyword import InterfaceKey
from common.common_method import *
import requests


def make_working_day():
    '''
    设置工作时长
    :return:
    '''
    url = get_url('skyline_sit', 'sit_host') + '/work/save/off/day'
    headers = {
        'accessToken': get_access_token()
    }
    data = {
        'admin': True,
        'userid': 100835,
        'offDays': ["2021-10-01", "2021-10-02"],
        'workTimes': [{'end': '12:00', 'start': '9:00'}, {'end': '18:00', 'start': '13:00'}],
    }
    res = requests.post(url=url, headers=headers, json=data)
    print(res.text)
    print(res.request.body)


def get_dk_data():
    '''
    新增打开数据
    :return:
    '''
    url = get_url('skyline_sit', 'sit_host') + '/attendanceRecord/clockIn'
    headers = {
        'accessToken': get_access_token()
    }
    data = {
        "clockInMechine": "aaf611c833174f648cef8b0a4d07732c",
        "clockInMechineName": "一楼考勤机_门_1",
        "clockInTime": "2021-08-19 09:00:00",
        "type": 0,
        "userId": 100835,
        "username": "kobekq1",
    }
    res = requests.post(url=url, headers=headers, json=data)
    print(res.request.body)
    print(res.text)


if __name__ == '__main__':
    make_working_day()
