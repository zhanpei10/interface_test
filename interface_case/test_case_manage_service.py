# 事件流程设置
import pytest
from common.assert_myself import *
from common.get_config import *
import uuid
import time
from common.get_data_by_mysql import MysqlData


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
        cls.processClosedTime = int(time.time()) * 1000 + 2 * 24 * 60 * 60  # 处理截止时间
        cls.transferDispatchTime = int(time.time()) * 1000 + 24 * 60 * 60  # 转派时间
        cls.suspectUsers = [{}]
        cls.caseType = None
        cls.gridSerial = None
        cls.images = put_photo(cls.accessToken)
        # 其他参数配置
        cls.keywords = None  # 搜索关键字参数
        cls.id = None  # 事件id
        cls.deadLine = time.strftime('%Y-%m-%d %H:%M:%S')
        cls.dealTime = time.strftime('%Y-%m-%d %H:%M:%S')  # 处置时间
        cls.phase = None  # 案件阶段
        cls.caseId = None  # 案件id
        # 流程参数配置
        cls.userId = None  # 处置人员id

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
        # 调用事件流程接口，获取事件类型
        if "process" in data['url']:
            TestCaseManageService.caseType = \
                get_parameter_by_interface(self, data, 'post', 'eventType', data['context'])[0]
        # 查询已配置流程的事件和网格
        else:
            get_data_sql = 'SELECT gp.process_id, gp.grid_id, gr.serial ' \
                           'FROM info_r_grid_process gp ' \
                           'JOIN info_r_grid_process_event_type gpe ' \
                           'ON gp.process_id = gpe.process_id ' \
                           'JOIN info_grid gr ' \
                           'ON gr.id = gp.grid_id WHERE gpe.event_type = {}'.format(self.caseType)
            # 从数据库获取数据
            mysql_data = MysqlData().get_params(get_data_sql, 1)
            # 网格
            TestCaseManageService.gridSerial = mysql_data[0]['serial']
            # 调用检查接口
            res = set_request(self, data, 'post')
            print(res.request.body)
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
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
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/case_manage_service/case_list.yaml'))
    def test_case_list(self, data):
        '''
        查询事件列表接口测试
        :param data:
        :return:
        '''
        log().info('查询事件列表接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
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
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/case_manage_service/case_starred_case_id.yaml'))
    def test_case_starred_case_id(self, data):
        '''
        根据事件id添加事件关注
        :param data:
        :return:
        '''
        log().info('添加事件关注接口测试开始')
        res = set_request(self, data, 'put', address_id=self.caseId)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/case_manage_service/case_unstarred_case_id.yaml'))
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

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/case_manage_service/case_timershaft_case_id.yaml'))
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
