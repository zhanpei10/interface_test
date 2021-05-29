# 事件流程设置
import pytest
from common.common_method import *
from api_keyword.interface_keyword import InterfaceKey
import uuid
import time
import json


class TestCaseManageService:

    @classmethod
    def setup_class(cls):
        '''
        类前置方法  关联接口关联参数初始化操作
        :return:
        '''
        log().info('------------------------事件上报操作流程相关接口测试开始--------------------------')
        set_class_common(cls)
        # 事件上报相关参数设置
        cls.serial = str(uuid.uuid1())  # 事件编号
        cls.taskNumber = str(uuid.uuid1())  # 任务号
        cls.reportTime = int(time.time()) * 1000  # 上报时间
        cls.processClosedTime = (int(time.time()) + 24*60*60*2) * 1000  # 处理截止事件
        cls.transferDispatchTime = (int(time.time()) + 24*60*60) * 1000  # 转派时间
        cls.suspectUsers = [{}]
        # 其他参数配置
        cls.keywords = None  # 搜索关键字参数
        cls.id = None   # 事件id
        cls.deadLine = time.strftime('%Y-%m-%d %H:%M:%S')
        cls.dealTime = time.strftime('%Y-%m-%d %H:%M:%S')  # 处置时间
        cls.phase = None  # 案件阶段
        cls.caseId = None  # 案件id

    @classmethod
    def teardown_class(cls):
        log().info('-------------------事件上报操作流程相关接口测试结束---------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_merge_check.yaml'))
    def test_case_merge_check(self, data):
        '''
        事件是否进行合并接口测试
        :param data:
        :return:
        '''
        log().info('事件是否合并接口测试')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        # 为赋值keywords
        TestCaseManageService.keywords = self.serial

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case.yaml'))
    def test_case(self, data):
        '''
        事件上报接口测试
        :param data:
        :return:
        '''
        log().info('事件上报接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_list.yaml'))
    def test_case_list(self, data):
        '''
        查询事件列表接口测试
        :param data:
        :return:
        '''
        log().info('查询事件列表接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        TestCaseManageService.id = get_data_by_json(res.text, 'id')
        TestCaseManageService.caseId = get_data_by_json(res.text, 'id')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_id.yaml'))
    def test_case_id(self, data):
        '''
        根据事件id查询事件详情
        :param data:
        :return:
        '''
        log().info('根据事件id查询事件详情接口测试开始')
        res = set_request(self, data, 'get', address_id=self.id)
        TestCaseManageService.phase = get_data_by_json(res.text, 'phase')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_starred_case_id.yaml'))
    def test_case_starred_case_id(self, data):
        '''
        根据事件id添加事件关注
        :param data:
        :return:
        '''
        log().info('添加事件关注接口测试开始')
        res = set_request(self, data, 'put', address_id=self.caseId)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_unstarred_case_id.yaml'))
    def test_case_un_starred_case_id(self, data):
        '''
        删除事件关注接口测试
        :param data:
        :return:
        '''
        log().info('删除事件关注接口测试')
        res = set_request(self, data, 'delete', address_id=self.caseId)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_operate.yaml'))
    def test_case_operate(self, data):
        '''
        事件流程处理接口测试
        :return:
        '''
        log().info('事件流程处理接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    #  暂不清楚使用场景
    # @pytest.mark.parametrize('data', get_data_by_yaml(r'../data/case_manage_service/case_operate_auto.yaml'))
    # def test_case_operate_auto(self, data):
    #     '''
    #     获取案件阶段的受理方式
    #     :param data:
    #     :return:
    #     '''
    #     log().info('获取案件阶段的受理方式')
    #     url = self.host + data['url']
    #     headers = set_value(self, **data['headers'])
    #     params = set_value(self, **data['data'])
    #     res = self.kw.do_get(path=url, headers=headers, params=params)
    #     print(res.request.url)
    #     make_assert(res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_timershaft_case_id.yaml'))
    def test_case_timershaft_case_id(self, data):
        '''
        获取案件的时间责任轴
        :param data:
        :return:
        '''
        log().info('获取案件的时间责任轴')
        res = set_request(self, data, 'get', address_id=self.caseId)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_case_manage_service.py::TestCaseManageService'])





