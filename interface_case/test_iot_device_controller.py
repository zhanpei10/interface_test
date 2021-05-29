# 噪音和扬尘设备相关接口测试
import pytest
from common.common_method import *
import random
import time


class TestIotDevice:

    @classmethod
    def setup_class(cls):
        '''
        类前置方法
        :return:
        '''
        log().info('------------------噪音和扬尘设备相关接口测试开始---------------------')
        set_class_common(cls)
        cls.name = 'iotName_' + str(random.randint(1, 100))
        cls.serial = 'autoTest_' + str(random.randint(1, 100))
        cls.createTime = None
        cls.id = None
        cls.type = None
        cls.deviceId = None
        cls.updateTime = int(time.time()) * 1000
        # 设备关联参数
        cls.devices = [{
            'deviceId': None,
            'type': None,
        }]
        cls.projectId = None

    @classmethod
    def teardown_class(cls):
        '''
        后置方法
        :return:
        '''
        log().info('------------------噪音和扬尘设备相关接口测试结束---------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/iot_device_controller/iot_device_type.yaml'))
    def test_iot_device_type(self, data):
        '''
        获取所有的设备类型接口测试
        :param data:
        :return:
        '''
        log().info('获取所有的设备类型接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/iot_device_controller/iot_device_add.yaml'))
    def test_iot_device_add(self, data):
        '''
        新增设备接口测试
        :param data:
        :return:
        '''
        log().info('新增设备接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/iot_device_controller/iot_device_list.yaml'))
    def test_iot_device_list(self, data):
        '''
        根据设备名称查询设备列表接口测试
        :param data:
        :return:
        '''
        log().info('根据设备名称查询设备列表接口测试')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg')
        TestIotDevice.createTime = get_data_by_json(res.text, 'createTime')
        TestIotDevice.id = get_data_by_json(res.text, 'id')
        TestIotDevice.devices[0]['deviceId'] = get_data_by_json(res.text, 'id')
        TestIotDevice.devices[0]['type'] = get_data_by_json(res.text, 'type')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/iot_device_controller/iot_device_update_by_id.yaml'))
    def test_iot_device_update_by_id(self, data):
        '''
        修改设备接口测试
        :param data:
        :return:
        '''
        log().info('修改设备接口测试开始')
        res = set_request(self, data, 'put', address_id=self.id)
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/iot_device_controller/iot_device_page.yaml'))
    def test_iot_device_page(self, data):
        '''
        分页查询设备
        :param data:
        :return:
        '''
        log().info('分页查询设备接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/iot_device_controller/iot_device_relation.yaml'))
    def test_iot_device_relation(self, data):
        '''
        设备关联工地接口测试
        :param data:
        :return:
        '''
        log().info('设备关联工地接口测试')
        log().info('获取项目id')
        project_data = {'url': '/construction/list',
                        'headers': {'accessToken': None},
                        'data': {'pageSize': 30, 'page': 1}}
        project_res = set_request(self, project_data, 'get')
        ids = get_data_by_json(project_res.text, 'id')
        log().info(project_res.text)
        log().info(ids)
        TestIotDevice.projectId = ids[0]
        log().info('设备关联工地接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/iot_device_controller/iot_device_delete_by_id.yaml'))
    def test_test_iot_device_controller(self, data):
        '''
        删除设备
        :param data:
        :return:
        '''
        log().info('删除设备接口测试开始')
        res = set_request(self, data, 'delete', address_id=self.id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_iot_device_controller.py::TestIotDevice'])
