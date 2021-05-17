# 添加购物车接口测试
import pytest
from api_keyword.MyApiKeyword import RequestKeyword
import allure
from data_driver.DataDriver import get_yaml_data

class TestAddCar:

    # 添加赋值函数
    def fz(self, kwargs):
        for key,value in kwargs.items():
            if type(value) is dict:
                self.fz(value)
            elif not value:
                kwargs[key] = getattr(self, key)
                print(kwargs)
        return kwargs

    # 设置前置条件
    @classmethod
    def setup_class(cls):
        cls.kw = RequestKeyword()
        cls.url = cls.kw.get_url('sit_url', 'url')
        cls.token = None
        cls.userid = None
        cls.openid = None

    @allure.feature('登录接口验证')
    @allure.story('获取用户的token信息')
    @allure.title('登录接口')
    @pytest.mark.parametrize('data', get_yaml_data(r'../data/add_car_login.yaml'))
    def test_login1(self, data):
        url = self.kw.get_url('sit_url', 'url') + data['path']
        res = self.kw.do_post(path=url, json=data['data'])
        token = self.kw.get_value_by_json(res.text, 'token')
        TestAddCar.token = token

    # 获取用户信息接口
    @allure.feature('访问获取用户信息接口')
    @allure.story('获取用户的相关信息 userid openid')
    @allure.title('获取用户信息')
    @pytest.mark.parametrize('data', get_yaml_data(r'../data/get_user.yaml'))
    def test_get_user(self, data):
        url = self.kw.get_url('sit_url', 'url') + data['path']
        headers = self.fz(data)['headers']
        res = self.kw.do_get(path=url, headers=headers)
        TestAddCar.userid = self.kw.get_value_by_json(res.text, 'userid')
        TestAddCar.openid = self.kw.get_value_by_json(res.text, 'openid')

    # 添加购物车
    @allure.feature('访问添加购物车接口')
    @allure.story('在商品添加到购物车')
    @allure.title('添加购物车')
    @pytest.mark.parametrize('data', get_yaml_data(r'../data/add_car.yaml'))
    def test_add_car(self, data):
        url = self.url + data['path']
        data = self.fz(data)
        res = self.kw.do_post(path=url, json=data['data'], headers=data['headers'])
        print(res.text)


if __name__ == '__main__':
    pytest.main()