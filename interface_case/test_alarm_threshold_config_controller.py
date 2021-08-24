# 告警阀值相关接口测试
import time

import pytest
from common.common_method import *
import random


class TestAlarmThresholdConfigController:

    @classmethod
    def setup_class(cls):
        '''
        告警阀值相关接口测试类前置函数前置
        :return:
        '''
        log().info('-------------------告警阀值相关接口测试开始------------')
        set_class_common(cls)
        cls.name = 'autoTestName_' + str(random.randint(1, 10))
        cls.keyword = None
        cls.id = None
        cls.createTime = None
        cls.updateTime = int(time.time()) * 1000
        # 网格信息
        cls.gridName = None
        cls.gridSerial = None
        # 创建人员信息
        cls.creator = None
        cls.updater = None

    @classmethod
    def teardown_class(cls):
        log().info('-------------------告警阀值相关接口测试结束------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/alarm_threshold_config_controller/alarm_threshold_add.yaml'))
    def test_alarm_threshold_add(self, data):
        '''
        新增告警阀值接口测试
        :param data:
        :return:
        '''
        log().info('新增告警阀值接口测试')
        if 'tree' in data['url']:
            # 获取网格信息
            res_data = get_parameter_by_interface(self, data, 'post', ['gridName', 'gridSerial'], data['context'])
            TestAlarmThresholdConfigController.gridName = res_data['gridName'][0]
            TestAlarmThresholdConfigController.gridSerial = res_data['gridSerial'][0]
        else:
            res = set_request(self, data, 'post')
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
            TestAlarmThresholdConfigController.keyword = self.name

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/alarm_threshold_config_controller/alarm_threshold_page.yaml'))
    def test_alarm_threshold_page(self, data):
        '''
        分页查询告警阀值接口测试
        :param data:
        :return:
        '''
        log().info('分页查询告警阀值接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        TestAlarmThresholdConfigController.id = get_data_by_json(res.text, 'id')
        TestAlarmThresholdConfigController.createTime = get_data_by_json(res.text, 'createTime')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/alarm_threshold_config_controller/alarm_threshold_id.yaml'))
    def test_alarm_threshold_id(self, data):
        '''
        根据id查询告警阀值详情
        :param data:
        :return:
        '''
        log().info('根据id查询告警阀值详情接口测试开始')
        res = set_request(self, data, 'get', address_id=self.id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        TestAlarmThresholdConfigController.updater = get_data_by_json(res.text, 'creator')
        TestAlarmThresholdConfigController.creator = get_data_by_json(res.text, 'creator')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/alarm_threshold_config_controller/alarm_threshold_modify_id.yaml'))
    def test_alarm_threshold_modify_id(self, data):
        '''
        根据id修改告警阀值
        :param data:
        :return:
        '''
        log().info('根据id修改告警阀值接口测试开始')
        res = set_request(self, data, 'post', address_id=self.id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/alarm_threshold_config_controller/alarm_threshold_delete_id.yaml'))
    def test_alarm_threshold_delete_id(self, data):
        '''
        根据id删除告警阀值
        :param data:
        :return:
        '''
        log().info('根据id删除告警阀值接口测试开始')
        res = set_request(self, data, 'post', address_id=self.id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_alarm_threshold_config_controller.py::TestAlarmThresholdConfigController'])
