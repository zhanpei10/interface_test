# 装备平台管理
import pytest
from common.get_config import *
from common.assert_myself import *
import random
import socket
import struct


class TestPlatformController:

    @classmethod
    def setup_class(cls):
        '''
        类前置条件,配置相关参数
        :return:
        '''
        log().info('-------------装备平台接口测试开始--------------------')
        cls.kw = InterfaceKey()
        cls.host = get_url()
        cls.accessToken = get_access_token()
        # 设置新建平台参数
        cls.platformIp = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))  # ip
        cls.port = random.randint(1024, 65535)  # 端口
        cls.platformName = 'platformNameTest_' + str(random.randint(1, 10))
        cls.username = 'usernameTest_' + str(random.randint(11, 20))
        # 设置id
        str1 = ''
        for i in range(0, 20):
            str1 += str(random.randint(0, 9))
        cls.platformId = str1
        # 设置查询平台列表参数
        cls.platformType = None
        cls.serial = None
        cls.createTime = None

    @classmethod
    def teardown_class(cls):
        '''
        类后置条件
        :return:
        '''
        log().info('-------------装备平台接口测试结束--------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/platform_controller/platform_create.yaml'))
    def test_platform_create(self, data):
        '''
        新增装备平台接口测试
        :param data:
        :return:
        '''
        log().info('新增装备平台接口测试开始')
        res = set_request(self, data, 'post')
        TestPlatformController.platformType = data['data']['platformType']
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/platform_controller/platform_list_by_type.yaml'))
    def test_platform_list_by_type(self, data):
        '''
        根据平台类别查询平台列表
        :param data:
        :return:
        '''
        log().info('根据平台类别查询平台列表接口测试开始')
        res = set_request(self, data, 'get')
        serials = get_data_by_json(res.text, 'serial')
        TestPlatformController.serial = serials[len(serials) - 1]
        createTimes = get_data_by_json(res.text, 'createTime')
        TestPlatformController.createTime = createTimes[len(createTimes) - 1]
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/platform_controller/platform_list_by_serial.yaml'))
    def test_platform_list_by_serial(self, data):
        '''
        根据serial查询单个平台平台列表
        :param data:
        :return:
        '''
        log().info('根据serial查询单个平台接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/platform_controller/platform_update.yaml'))
    def test_platform_update(self, data):
        '''
        修改平台信息接口测试
        :param data:
        :return:
        '''
        log().info('修改平台信息接口测试开始')
        res = set_request(self, data, 'put')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/platform_controller/platform_delete.yaml'))
    def test_platform_delete(self, data):
        '''
        删除平台信息接口测试
        :param data:
        :return:
        '''
        log().info('删除平台信息接口测试开始')
        res = set_request(self, data, 'delete')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_platform_controller.py::TestPlatformController'])
