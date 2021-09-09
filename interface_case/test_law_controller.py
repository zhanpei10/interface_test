# 法律法规相关接口测试
import pytest
from common.get_config import *
from common.assert_myself import *
from api_keyword.interface_keyword import InterfaceKey
import random
import time


class TestLawController:

    @classmethod
    def setup_class(cls):
        '''
        类前置方法，设置相关公共参数
        :return:
        '''
        log().info('-------------------法律法规相关接口测试开始----------------------')
        set_class_common(cls)
        # 新建法律法规参数
        cls.behaviorName = 'behaviorName_' + 'autoTest' + str(random.randint(1, 10))
        cls.classification = 'classification_' + 'autoTest' + str(random.randint(1, 10))
        cls.library = ' library_' + 'autoTest_' + str(random.randint(1, 10))
        cls.regulations = 'regulations_' + 'autoTest_' + str(random.randint(1, 10))
        cls.terms = 'terms_' + 'autoTest' + str(random.randint(1, 10))
        # 查询参数
        cls.keywords = cls.behaviorName
        cls.id = None
        # 修改法律法规参数
        cls.createTime = None
        cls.updateTime = int(time.time()) * 1000
        cls.lawId = None
        # 删除法律法规参数
        cls.lawIds = None

    @classmethod
    def teardown_class(cls):
        log().info('-------------------法律法规相关接口测试结束----------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/law_controller/law_create.yaml'))
    def test_law_create(self, data):
        '''
        新建法律法规接口测试
        :param data:
        :return:
        '''
        log().info('新建法律法规接口测试开始')
        url = self.host + data['url']
        headers = set_value(self, **data['headers'])
        set_data = set_value(self, **data['data'])
        res = self.kw.do_post(path=url, headers=headers, json=set_data)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/law_controller/law_list.yaml'))
    def test_law_list(self, data):
        '''
        查询法律法规列表接口测试
        :param data:
        :return:
        '''
        log().info('查询法律法规列表详情接口测试开始')
        url = self.host + data['url']
        headers = set_value(self, **data['headers'])
        set_data = set_value(self, **data['data'])
        res = self.kw.do_post(path=url, headers=headers, json=set_data)
        TestLawController.id = get_data_by_json(res.text, 'id')
        TestLawController.lawId = get_data_by_json(res.text, 'id')
        TestLawController.lawIds = get_data_by_json(res.text, 'id')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/law_controller/law_by_id.yaml'))
    def test_law_by_id(self, data):
        '''
        根据id查询法律法规接口测试
        :param data:
        :return:
        '''
        log().info('根据id查询法律法规详情接口测试开始')
        url = self.host + data['url'] + str(self.id)
        headers = set_value(self, **data['headers'])
        res = self.kw.do_get(path=url, headers=headers)
        TestLawController.createTime = get_data_by_json(res.text, 'createTime')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/law_controller/law_update.yaml'))
    def test_law_update(self, data):
        '''
        修改法律法规接口测试
        :param data:
        :return:
        '''
        log().info('修改法律法规接口测试开始')
        url = self.host + data['url']
        headers = set_value(self, **data['headers'])
        set_data = set_value(self, **data['data'])
        res = self.kw.do_post(path=url, headers=headers, json=set_data)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/law_controller/law_batch_delete.yaml'))
    def test_law_batch_delete(self, data):
        '''
        删除法律法规接口测试
        :param data:
        :return:
        '''
        log().info('删除法律法规接口测试开始')
        url = self.host + data['url']
        headers = set_value(self, **data['headers'])
        params = set_value(self, **data['data'])
        res = self.kw.do_delete(path=url, headers=headers, params=params)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_law_controller.py::TestLawController'])
