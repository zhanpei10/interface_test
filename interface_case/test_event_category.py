# 新增事件小类的操作
import pytest
from common.get_config import *
from common.assert_myself import *


class TestEventCategory:

    @classmethod
    def setup_class(cls):
        '''
        前置类方法，配置相关的参数
        :return:
        '''
        log().info('------------------新增事件类别接口测试开始-----------------------')
        set_class_common(cls)
        # 大类id
        cls.parentId = None
        # 小类id
        cls.id = None
        cls.ids = []

    @classmethod
    def teardown_class(cls):
        log().info('------------------新增事件类别接口测试结束-----------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/event_category/event_category_create_dl.yaml'))
    def test_event_category_create_dl(self, data):
        '''
        新增事件小类接口测试
        :param data:
        :return:
        '''
        log().info('新增事件大类接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/event_category/event_category_tree.yaml'))
    def test_event_category_tree(self, data):
        '''
        获取事件类型树
        :param data:
        :return:
        '''
        log().info('获取事件类型树接口测试开始')
        res = set_request(self, data, method='get')
        ids = get_data_by_json(text=res.text, key='id')
        TestEventCategory.parentId = ids[len(ids) - 1]
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/event_category/event_category_create_xl.yaml'))
    def test_event_category_create_xl(self, data):
        '''
        新增事件小类
        :param data:
        :return:
        '''
        log().info('新增事件小类接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/event_category/event_category_page.yaml'))
    def test_event_category_page(self, data):
        '''
        分页获取事件列表接口测试
        :param data:
        :return:
        '''
        log().info('分页获取事件列表接口测试开始')
        res = set_request(self, data, 'post')
        get_id = get_data_by_json(res.text, 'id')
        TestEventCategory.ids.append(get_id[0])
        TestEventCategory.id = get_id[0]
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/event_category/event_category_by_id.yaml'))
    def test_event_category_by_id(self, data):
        '''
        获取事件分类详情接口测试
        :param data:
        :return:
        '''
        log().info('获取事件分类详情接口测试开始')
        res = set_request(self, data, 'get', address_id=self.id)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/event_category/event_category_delete_xl.yaml'))
    def test_event_category_delete_xl(self, data):
        '''
        删除事件小类
        :param data:
        :return:
        '''
        log().info('删除事件小类接口测试开始')
        res = set_request(self, data, 'post')
        TestEventCategory.ids[0] = self.parentId
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/event_category/event_category_delete_dl.yaml'))
    def test_event_category_delete_dl(self, data):
        '''
        删除事件大类
        :param data:
        :return:
        '''
        log().info('删除事件大类接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_event_category.py'])