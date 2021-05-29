# 加班申请相关接口测试
import pytest
from common.common_method import *
import time


class TestOvertime:

    @classmethod
    def setup_class(cls):
        '''
        加班申请前置方法
        :return:
        '''
        log().info('----------------加班申请接口测试开始--------------------')
        set_class_common(cls)
        # 加班申请附件参数
        cls.attachments = {
            'fileName': 'put_photo.png',
            'type': 1,
            'url': put_photo(cls.accessToken)
        }
        cls.overTimeBeginTimestamp = int(time.time()) * 1000
        cls.overTimeEndTimestamp = int(time.time() + 24 * 60 * 60) * 1000
        cls.overtime = int((cls.overTimeEndTimestamp - cls.overTimeBeginTimestamp) / 3600 / 1000)

    @classmethod
    def teardown_class(cls):
        '''
        加班申请后置方法
        :return:
        '''
        log().info('----------------加班申请接口测试开始--------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/overtime/create.yaml'))
    def test_create(self, data):
        '''
        新建加班申请
        :param data:
        :return:
        '''
        log().info('新建加班申请开始')
        for i in  range(10):
            res = set_request(self, data=data, method='post')
            print(res.request.headers)
            print(res.request.body)
            print(res.text)

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/overtime/prove.yaml'))
    def test_put(self, data):
        '''
        加班审批功能
        :param data:
        :return:
        '''
        log().info('加班审批开始')
        for i in range(1, 10):
            res = set_request(self, method='put', data=data, address_id=109)
            print(res.request.body)
            print(res.text)


if __name__ == '__main__':
    pytest.main(['./test_overtime.py::TestOvertime::test_create'])
