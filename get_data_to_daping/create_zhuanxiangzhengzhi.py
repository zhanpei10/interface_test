from api_keyword.interface_keyword import InterfaceKey
from common.common_method import *
import random


# 添加专项整治的数据
def create_zxzz():

    name = '这是测试新建的名称' + str(random.randint(10001, 100003))
    url = 'http://10.111.32.82:10219/whale-openapi/renovation/create'
    data = {"title": name, "renovationCategory": 4235,
            "coverUrl": "/skyline/img/special-rectification-template-2.131adc78.png", "renovationType": 1,
            "renovationLevel": 1, "attendOrganId": "1", "leadOrganId": "1", "aim": "而威尔",
            "content": "<p>而且额外企鹅群翁无群二去</p>", "status": 1, "startTimestamp": 1623415040000,
            "endTimestamp": 1624451840000, "renovationAnnexReqList": None}
    headers = {
        'accessToken': get_access_token()
    }
    res = InterfaceKey().do_post(path=url, json=data, headers=headers)
    print(res.text)


if __name__ == '__main__':
    for i in range(44):
        create_zxzz()
