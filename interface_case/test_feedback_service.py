# 意见反馈相关接口测试
import pytest
from common.common_method import *
import time


class TestFeedback:

    @classmethod
    def setup_class(cls):
        '''
        类前置函数
        :return:
        '''
        log().info('----------------意见反馈相关接口测试开始------------------')
        set_class_common(cls)
        cls.reportTime = time.strftime('%Y-%m-%d %H:%M:%S')
        cls.id = None

    @classmethod
    def teardown_class(cls):
        log().info('----------------意见反馈相关接口测试结束------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/feedback_service/feedback.yaml'))
    def test_feedback(self, data):
        '''
        新增意见接口测试
        :param data:
        :return:
        '''
        log().info('新增意见接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/feedback_service/feedback_list.yaml'))
    def test_feedback_list(self, data):
        '''
        获取意见反馈列表接口测试
        :param data:
        :return:
        '''
        log().info('获取意见反馈列表接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        ids = get_data_by_json(res.text, 'id')
        TestFeedback.id = ids[0]

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/feedback_service/feedback_detail_id.yaml'))
    def test_feedback_detail_id(self, data):
        '''
        获取意见详情接口测试
        :param data:
        :return:
        '''
        log().info('获取意见详情接口测试开始')
        res = set_request(self, data, 'get', address_id=self.id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_feedback_service.py::TestFeedback'])
