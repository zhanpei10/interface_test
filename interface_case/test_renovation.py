'''
专项整治相关接口测试
'''
import pytest
from common.get_config import *
from common.assert_myself import *
import random
import time
import os


class TestRenovationController:

    @classmethod
    def setup_class(cls):
        '''
        专项整治相关接口测试前置方法
        :return:
        '''
        log().info('------------------专项整治相关接口测试开始----------------------')
        set_class_common(cls)
        cls.title_draft = 'autoTest11_' + str(random.randint(55, 66))
        cls.title = 'autoTest11_' + str(random.randint(66, 77))
        cls.startTimestamp = int(time.time()) * 1000 + 30 * 24 * 60 * 60 * 1000
        cls.endTimestamp = int(time.time()) * 1000 + 24 * 60 * 60 * 1000
        cls.updateTimestamp = int(time.time()) * 1000 + 30 * 24 * 60 * 60 * 1000
        cls.draft_ids = []
        cls.update_draft = None  # 需要提交的草稿数据
        cls.ids = []
        cls.id = None
        cls.file_address = None
        cls.userIds = []  # 流转绑定的用户id

    @classmethod
    def teardown_class(cls):
        log().info('------------------专项整治相关接口测试结束----------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/create_draft.yaml'))
    def test_create_draft(self, data):
        '''
        新建专项整治接口测试
        :param data:
        :return:
        '''
        log().info('新建专项整治草稿接口测试开始')
        if data['data']['title'] is None:
            data['data']['title'] = self.title_draft
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/page_draft.yaml'))
    def test_page_draft(self, data):
        '''
        获取专项整治草稿列表
        :param data:
        :return:
        '''
        log().info('获取专项整治草稿列表接口测试开始')
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
        TestRenovationController.draft_ids = get_data_by_json(res.text, key='id')[0:2]

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/detail_draft.yaml'))
    def test_detail_draft(self, data):
        '''
        查看草稿详情接口测试
        :param data:
        :return:
        '''
        log().info('查看草稿详情接口测试开始')
        for draft_id in TestRenovationController.draft_ids:
            data['data']['id'] = draft_id
            res = set_request(self, data=data, method='get')
            if draft_id == TestRenovationController.draft_ids[0]:
                TestRenovationController.update_draft = get_data_by_json(text=res.text, key='data')
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/delete_draft.yaml'))
    def test_delete_draft(self, data):
        '''
        删除草稿接口测试
        :param data:
        :return:
        '''
        log().info('删除草稿接口测试开始')
        data['data']['id'] = TestRenovationController.draft_ids.pop()
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/update_draft.yaml'))
    def test_update_draft(self, data):
        '''
        提交草稿箱的内容
        :param data:
        :return:
        '''
        log().info('提交草稿箱的内容接口测试开始')
        TestRenovationController.update_draft['status'] = 1
        data['data'] = TestRenovationController.update_draft
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/create.yaml'))
    def test_create(self, data):
        '''
        新建专项整治接口测试
        :param data:
        :return:
        '''
        log().info('新建专项整治接口测试开始')
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/page.yaml'))
    def test_page(self, data):
        '''
        获取专项整治列表接口测试
        :param data:
        :return:
        '''
        log().info('获取专项整治列表接口测试开始')
        res = set_request(self, data=data, method='post')
        make_assert_list_len(text=res.text, keyword='dataList', context=data['context'])
        if 'title' in data['data'].keys():
            TestRenovationController.ids = get_data_by_json(text=res.text, key='id')
            TestRenovationController.id = get_data_by_json(text=res.text, key='id')[0]

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/detail.yaml'))
    def test_detail(self, data):
        '''
        查看专项详情接口测试
        :param data:
        :return:
        '''
        log().info('查看专项详情接口测试开始')
        res = set_request(self, data=data, method='get')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/collect.yaml'))
    def test_collect(self, data):
        '''
        收藏和取消收藏专项整治
        :param data:
        :return:
        '''
        log().info('收藏和取消收藏专项整治接口测试开始')
        data['data']['renovationId'] = self.id
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/annex_upload.yaml'))
    def test_annex_upload(self, data):
        '''
        上传专项整治附件API接口测试
        :param data:
        :return:
        '''
        log().info('>>>>>>上传专项整治附件API接口测试开始')
        if '/annex/upload' in data['url']:
            with open(filename() + '/common/import_file/renovation_file_1.jpg', mode='rb') as f1:
                files = {
                    'file': f1,
                }
                res = set_request(self, data=data, import_file=files)
                make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])
                TestRenovationController.file_address = get_data_by_json(text=res.text, key='data')
        else:
            log().info('>>>>>>将上传的附件绑定到对应的专项整治')
            data['data']['createTime'] = self.startTimestamp
            data['data']['createTimestamp'] = self.startTimestamp
            data['data']['endTime'] = self.endTimestamp
            data['data']['renovationAnnexReqList'][0]['annexUrl'] = self.file_address
            data['data']['renovationAnnexReqList'][0]['annexName'] = 'renovation_file_1.bmp'
            data['data']['updateTime'] = self.updateTimestamp
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/operation_operate.yaml'))
    def test_operation_operate(self, data):
        '''
        添加事件流转流程接口测试
        :param data:
        :return:
        '''
        log().info('>>>>>添加事件流转流程接口测试开始')
        if 'users' in data['url']:
            log().info('>>>>获取人员信息')
            res = set_request(self, data=data, method='post')
            userIndex = get_data_by_json(res.text, 'username').index('dsad')
            TestRenovationController.userIds.append(get_data_by_json(text=res.text, key='userId')[userIndex])
        else:
            log().info('>>>>根据id去进行专项整治流转')
            data['data']['ccPersons'] = TestRenovationController.userIds
            data['data']['senders'] = TestRenovationController.userIds
            data['data']['renovationId'] = TestRenovationController.id
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/renovationController/delete.yaml'))
    def test_delete(self, data):
        '''
        删除专项整治
        :param data:
        :return:
        '''
        log().info('>>>>删除专项整治接口测试开始')
        for delete_id in self.ids:
            data['data']['id'] = delete_id
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])


if __name__ == '__main__':
    pytest.main(['./test_renovation.py::TestRenovationController'])
