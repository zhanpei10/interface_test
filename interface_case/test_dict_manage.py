'''
  字典管理操作流程，对字典主类和子类的增删改查
'''
import pytest
from common.common_method import *
from api_keyword.interface_keyword import InterfaceKey
import random
import uuid


class TestDictManage:

    @classmethod
    def setup_class(cls):
        log().info('-------------字典接口测试开始--------------')
        set_class_common(cls)
        # 主类名称
        cls.moduleName = 'tesT' + str(uuid.uuid1())
        # 主类编码
        cls.moduleType = 'BM' + str(uuid.uuid1())
        # 查询关键字
        cls.keyword = None
        # 字典主类id
        cls.id = None
        # 字典主类id
        cls.parentId = None
        #  子类的名称
        cls.subModuleName = 'subTest' + str(uuid.uuid1())
        # 子类的类型
        cls.subModuleType = 'sub_BM' + str(uuid.uuid1())
        # 子类的id
        cls.sub_id = None
        # 主类的id列表
        cls.ids = []
        # 子类的id列表
        cls.sub_ids = []

    @classmethod
    def teardown_class(cls):
        log().info('-----------字典相关接口测试完成--------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/dict_manage.yaml'))
    def test_dict_manage(self, data):
        '''
        新增字典主类操作
        :param data:
        :return:
        '''
        log().info('新增字典主类接口测试开始--')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
        TestDictManage.keyword = self.moduleType

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/get_id_for_dict.yaml'))
    def test_get_id_for_dict(self, data):
        '''
        根据关键字获取字典并获取id
        :param data:
        :return:
        '''
        log().info('获取字典项的id的测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
        TestDictManage.id = get_data_by_json(res.text, 'id')
        TestDictManage.parentId = get_data_by_json(res.text, 'id')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/dict_manage_id.yaml'))
    def test_dict_manage_id(self, data):
        '''
        根据id修改字典主项的操作
        :param data:
        :return:
        '''
        log().info('修改字典主项的测试开始')
        res = set_request(self, data, 'post', address_id=self.id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/list_all.yaml'))
    def test_list_all(self, data):
        '''
        获取所有的字典主类
        :param data:
        :return:
        '''
        log().info('查询所有的字典项接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/list.yaml'))
    def test_list(self, data):
        '''
        根据分页查询字典主项
        :param data:
        :return:
        '''
        log().info('根据页面查询字典接口测试开始')
        res = set_request(self, data, 'post')
        TestDictManage.ids = get_data_by_json(res.text, key='id')[0:2]
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/enable_count.yaml'))
    def test_enable_count(self, data):
        '''
        主类启用状态统计
        :param data:
        :return:
        '''
        log().info('主类启动状态接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/status_update_batch.yaml'))
    def test_status_update_batch(self, data):
        '''
        批量修改字典状态设置
        :param data:
        :return:
        '''
        log().info('批量修改状态接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/sub.yaml'))
    def test_sub(self, data):
        '''
        新增字典子类接口测试
        :param data:
        :return:
        '''
        log().info('新增字典子类接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/sub_list.yaml'))
    def test_sub_list(self, data):
        '''
        查看字典项的接口测试
        :param data:
        :return:
        '''
        log().info('查看字典子项接口测试开始')
        res = set_request(self, data, 'post')
        TestDictManage.sub_id = get_data_by_json(res.text, 'id')
        TestDictManage.sub_ids.append(get_data_by_json(res.text, 'id'))
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/sub_id.yaml'))
    def test_sub_id(self, data):
        '''
        修改字典子项的接口测试
        :param data:
        :return:
        '''
        log().info('修改字典子项接口测试开始')
        data['id'] = self.sub_id
        res = set_request(self, data=data, method='post', address_id=self.sub_id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/sub_status_update_batch.yaml'))
    def test_sub_status_update_batch(self, data):
        '''
        字典子项状态的批量操作
        :param data:
        :return:
        '''
        log().info('批量操作字典子类状态接口测试开始')
        data['ids'] = self.sub_ids
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/dict_manage/sub_batch_delete.yaml'))
    def test_sub_batch_delete(self, data):
        '''
        批量删除子类接口测试
        :param data:
        :return:
        '''
        log().info('批量删除子类接口测试开始')
        url = self.host + data['url']
        headers = set_value(self, **data['headers'])
        # data = self.sub_ids
        res = InterfaceKey().do_post(path=url, headers=headers, json=self.sub_ids)
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])


if __name__ == '__main__':
    pytest.main(['./test_dict_manage.py::TestDictManage'])
