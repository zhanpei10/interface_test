# 添加购物车练习
import pytest
from api_keyword.interface_keyword import InterfaceKey
from common.common_method import *


class TestAddCar:

    # 设置前置条件
    @classmethod
    def setup_class(cls):
        cls.kw = InterfaceKey()

    # 这是一个登录接口测试
    @pytest.mark.parametrize('data', get_data_by_yaml(r'..\data\login_data.yaml'))
    def test_login(self, data):
        log().info('登录接口测试')
        url = get_url('sit_server', 'host') + data['url']
        res = self.kw.do_post(path=url, json=data['data'])
        print(res.text)


if __name__ == '__main__':
    pytest.main()