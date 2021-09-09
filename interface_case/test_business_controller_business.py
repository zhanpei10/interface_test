# 商户相关接口测试  导入商户和按id进行查询接口页面未使用
import pytest
from common.assert_myself import *
from common.get_config import *
import random
import time
import uuid


class TestBusiness:

    @classmethod
    def setup_class(cls):
        '''
        类前置方法 设置关联参数
        :return:
        '''
        log().info('-----------商户相关接口测试开始-------------')
        set_class_common(cls)
        # 商户名称
        cls.name = 'autoTest' + str(uuid.uuid1())
        # 商户负责人
        cls.responsiblePerson = 'auto_people' + str(random.randint(100, 300))
        #
        cls.keyword = None
        cls.serial = None
        cls.serials = None
        cls.keywords = None
        # 图片路径
        cls.images = [put_photo(cls.accessToken)]
        # 视频源信息
        cls.resourceSerials = None
        # 商户相关的事件类型
        cls.caseTypes = None
        # 网格信息
        cls.gridSerial = None
        cls.gridSerials = None
        # 商户关联事件更新时间设置 为近7天
        cls.eventRefreshStartTime = int(time.time()) * 1000 - (30 * 24 * 60 * 60 * 1000)
        cls.eventRefreshEndTime = int(time.time()) * 1000

    @classmethod
    def teardown_class(cls):
        log().info('--------商户相关接口测试完成----------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/create_business.yaml'))
    def test_create_business(self, data):
        '''
        新建商户接口测试
        :param data:
        :return:
        '''
        log().info('新增商户接口测试开始-------------》')
        res = set_request(self, data, 'post')
        TestBusiness.keyword = self.name
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/business_list.yaml'))
    def test_business_list(self, data):
        '''
        查询商户列表接口
        :param data:
        :return:
        '''
        log().info('显示商户列表接口开始测试')
        res = set_request(self, data, 'post')
        make_assert_list_len(text=res.text, keyword='dataList', context=data['context'])
        if 'keyword' in data['data'].keys() and data['data']['keyword'] is not None:
            res_data = get_data_by_json(res.text, 'serial')
            if type(res_data) is list:
                TestBusiness.serial = res_data[0]
                TestBusiness.serials = res_data
            else:
                TestBusiness.serial = res_data

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/business_statistics.yaml'))
    def test_business_statistics(self, data):
        '''
        统计商户信息接口测试
        :param data:
        :return:
        '''
        log().info('统计接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(res.text, keyword='errorMsg', assert_data='ok')

    # @pytest.mark.parametrize('data', get_data_by_yaml(r'../data/business_controller/query_business_by_id.yaml'))
    # def test_query_business_by_id(self, data):
    #     '''
    #     根据id查询商户接口测试
    #     :param data:
    #     :return:
    #     '''
    #     url = self.host + data['url'] + str(self.business_id)
    #     headers = set_value(self, **data['headers'])
    #     res = self.kw.do_get(path=url, headers=headers)
    #     make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/business_serial.yaml'))
    def test_query_business_by_serial(self, data):
        '''
        根据商户编码查询商户接口测试
        :param data:
        :return:
        '''
        log().info('根据商户编码查询商户接口测试开始')
        res = set_request(self, data, 'get', address_id=self.serial)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/update_business.yaml'))
    def test_update_business(self, data):
        '''
        修改商户接口测试
        :param data:
        :return:
        '''
        log().info('修改商户接口测试开始')
        res = set_request(self, data, 'put')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/business_relevancy.yaml'))
    def test_business_relevancy(self, data):
        '''
        关联视频源操作
        :param data:
        :return:
        '''
        log().info('商户关联视频源接口测试')
        if 'resources' in data['url']:
            # 获取视频源信息
            resourceSerial_data = get_parameter_by_interface(self, data, 'post', 'resourceSerial', data['context'])
            TestBusiness.resourceSerials = resourceSerial_data[1:3]
        else:
            data['data']['businessSerial'] = self.serial
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/delete_business.yaml'))
    def test_update_business(self, data):
        '''
        删除商户接口测试
        :param data:
        :return:
        '''
        log().info('>>>删除商户接口测试开始')
        # 根据商户编号，判断删除一个还是删除多个
        if self.serials is None:
            res = set_request(self, data, 'delete', address_id=self.serial)
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
        else:
            for s in self.serials:
                res = set_request(self, data, 'delete', address_id=s)
                make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/business_controller/business_case_list.yaml'))
    def test_business_case_list(self, data):
        '''
        商户违法事件查询接口
        :param data:
        :return:
        '''
        log().info('商户违法事件查询接口测试开始')
        # 获取商户相关的事件类型
        if 'event-category' in data['url']:
            TestBusiness.caseTypes = get_parameter_by_interface(self, data, 'get', 'value', data['context'])
        # 查询网格信息，根据网格信息查询违法事件
        elif '/grid/tree' in data['url']:
            # 获得网格的父节点
            if data['data']['gridSerial'] is not None:
                TestBusiness.gridSerial = get_parameter_by_interface(self, data, 'post', 'gridSerial')[1]
            # 查询父节点下的所有网格
            else:
                TestBusiness.gridSerials = get_parameter_by_interface(self, data, 'post', 'gridSerial', data['context'])
        else:
            if 'cameras' in data['data'].keys():
                data['data']['cameras'] = self.resourceSerials
            res = set_request(self, data, 'post')
            print(res.request.body)
            make_assert_list_len(text=res.text, keyword='dataList', context=data['context'])


if __name__ == '__main__':
    pytest.main(['./test_business_controller_business.py::TestBusiness'])
