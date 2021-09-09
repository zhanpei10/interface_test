# 用户自定义应用接口测试
import pytest
from common.get_config import *
from common.assert_myself import *


class TestUserCustomModule:

    @classmethod
    def setup_class(cls):
        '''
        类前置方法
        :return:
        '''
        log().info('----------------用户自定义应用接口测试开始----------------')
        set_class_common(cls)

    @classmethod
    def teardown_class(cls):
        '''

        :return:
        '''
        log().info('----------------用户自定义应用接口测试开始----------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/user_custom_module_service/custom_modules_of_loginuser.yaml'))
    def test_custom_modules_of_login_user(self, data):
        '''
        查看用户自定义应用列表接口
        :param data:
        :return:
        '''
        log().info('查看用户自定义应用列表接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/user_custom_module_service/custom_modules.yaml'))
    def test_custom_modules(self, data):
        '''
        保存自定义应用接口
        :param data:
        :return:
        '''
        log().info('保存自定义应用接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_user_custom_module.py::TestUserCustomModule'])
