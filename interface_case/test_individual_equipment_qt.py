# 单兵装备接口增删改差测试
import pytest
from common.get_config import *
from common.assert_myself import *
import random
import time


class TestIndividualEquipmentQT:

    @classmethod
    def setup_class(cls):
        '''
        单兵装备接口测试类前置方法
        :return:
        '''
        log().info('--------------其他装备接口测试开始-------------------')
        set_class_common(cls)
        cls.equipmentName = None
        cls.ids = []
        cls.id = None

    @classmethod
    def teardown_class(cls):
        log().info('--------------其他装备接口测试结束-------------------')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/individualEquipmentController_qt/create_qt.yaml'))
    def test_create_qt(self, data):
        '''
        新增其他装备接口测试
        :param data:
        :return:
        '''
        log().info('新增其他装备接口测试开始')
        if data['data']['equipmentType'] == 10001:
            TestIndividualEquipmentQT.equipmentName = 'autoTest_bxs_' + str(random.randint(1, 10))
        elif data['data']['equipmentType'] == 10002:
            TestIndividualEquipmentQT.equipmentName = 'autoTest_cj_' + str(random.randint(1, 10))
        elif data['data']['equipmentType'] == 10003:
            TestIndividualEquipmentQT.equipmentName = 'autoTest_qt_' + str(random.randint(1, 10))
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
        time.sleep(6)

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/individualEquipmentController_qt/import_qt.yaml'))
    def test_import_qt(self, data):
        '''
        导入其他装备的接口测试
        :param data:
        :return:
        '''
        log().info('导入其他装备的接口测试开始')
        with open(filename() + '/common/import_file/qtzb.xlsx', mode='rb') as f1:
            files = {
                'file': f1
            }
            res = set_request(self, data=data, method='post', import_file=files)
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/individualEquipmentController_qt/page_qt.yaml'))
    def test_page_qt(self, data):
        '''
        获取其他装备列表接口测试
        :param data:
        :return:
        '''
        log().info('获取其他装备列表接口测试开始')
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])
        if 'keywords' in data['data'].keys():
            TestIndividualEquipmentQT.ids = get_data_by_json(res.text, key='id')
            TestIndividualEquipmentQT.id = get_data_by_json(res.text, key='id')[0]

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/individualEquipmentController_qt/detail_qt.yaml'))
    def test_detail_qt(self, data):
        '''
        查看其他装备详情接口测试
        :param data:
        :return:
        '''
        log().info('查看其他装备详情接口测试')
        res = set_request(self, data=data, method='get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/individualEquipmentController_qt/update_qt.yaml'))
    def test_update_qt(self, data):
        '''
        修改其他装备接口测试
        :param data:
        :return:
        '''
        log().info('修改其他装备接口测试开始')
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/individualEquipmentController_qt/delete_qt.yaml'))
    def test_delete_qt(self, data):
        '''
        删除其他装备接口测试
        :param data:
        :return:
        '''
        log().info('删除其他装备接口测试开始')
        for delete_id in TestIndividualEquipmentQT.ids:
            data['data']['id'] = delete_id
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])


if __name__ == '__main__':
    pytest.main(['./test_individual_equipment_qt.py::TestIndividualEquipmentQT'])
