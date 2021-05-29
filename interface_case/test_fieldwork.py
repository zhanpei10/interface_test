# 外勤管理相关接口测试
import pytest
from common.common_method import *
import time


class TestFieldwork:
    '''
    外勤相关接口测试类
    '''

    @classmethod
    def setup_class(cls):
        '''
        外勤接口测试前置方法
        :return:
        '''
        log().info('-----------外勤相关接口测试开始--------------')
        set_class_common(cls)
        # 开始时间和结束时间配置
        cls.reason = '请假原因' * 4
        cls.endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 2 * 24 * 60 * 60))
        cls.startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 1 * 24 * 60 * 60))
        # 时间长度控制
        num = ((time.time() + 10 * 24 * 60 * 60) - (time.time() + 1 * 24 * 60 * 60)) / (60 * 60 * 24)
        cls.length = round(round(num, 1), 0)

    @classmethod
    def teardown(cls):
        log().info('-----------外勤相关接口测试结束--------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/filedwork_record_controller/save.yaml'))
    def test_save(self, data):
        '''
        外勤申请测试
        :param data:
        :return:
        '''
        log().info('>>>外勤申请接口测试开始')
        res = set_request(self, data=data, method='post')
        print(self.reason)
        print(res.request.body)
        print(res.text)


if __name__ == '__main__':
    pytest.main(['./test_fieldwork.py::TestFieldwork::test_save'])
