# 单兵装备接口增删改差测试
import pytest
from common.get_config import *
from common.assert_myself import *
import random
import time


class TestIndividualEquipment:

    @classmethod
    def setup_class(cls):
        '''
        单兵装备接口测试类前置方法
        :return:
        '''
        log().info('--------------单兵装备接口测试开始-------------------')
        set_class_common(cls)
        cls.equipmentName = None
        cls.ids = []
        cls.id = None

    @classmethod
    def teardown_class(cls):
        log().info('--------------单兵装备接口测试结束-------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/individualEquipmentController/create.yaml'))
    def test_create(self, data):
        '''
        新建单兵装备
        :param data:
        :return:
        '''
        log().info('新建单兵接口测试开始')
        if data['data']['equipmentType'] == 3:
            TestIndividualEquipment.equipmentName = 'autoTest_jly_' + str(random.randint(11, 17))
        elif data['data']['equipmentType'] == 4:
            TestIndividualEquipment.equipmentName = 'autoTest_zfzd_' + str(random.randint(11, 17))
        elif data['data']['equipmentType'] == 5:
            TestIndividualEquipment.equipmentName = 'autoTest_djj_' + str(random.randint(11, 17))
        elif data['data']['equipmentType'] == 6:
            TestIndividualEquipment.equipmentName = 'autoTest_lyb_' + str(random.randint(11, 17))
        elif data['data']['equipmentType'] == 101:
            TestIndividualEquipment.equipmentName = 'autoTest_qt_' + str(random.randint(11, 17))
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])
        time.sleep(5)

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/individualEquipmentController/import.yaml'))
    def test_import(self, data):
        '''
        导入文件接口测试
        :param data:
        :return:
        '''
        log().info('导入文件接口测试开始')
        with open(filename() + '/common/import_file/test_dbzb.xlsx', mode='rb') as f1:
            files = {
                'file': f1,
            }
            res = set_request(self, data=data, import_file=files)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/individualEquipmentController/page.yaml'))
    def test_page(self, data):
        '''
        查看单兵装备列表
        :param data:
        :return:
        '''
        log().info('查看单兵列表开始')
        res = set_request(self, data=data, method='post')
        make_assert(keyword='errorMsg', text=res.text, assert_data='ok', context=data['context'])
        if 'keywords' in data['data'].keys():
            TestIndividualEquipment.ids = get_data_by_json(res.text, key='id')
            TestIndividualEquipment.id = TestIndividualEquipment.ids[0]

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/individualEquipmentController/update.yaml'))
    def test_update(self, data):
        '''
        根据id去修改单兵装备
        :param data:
        :return:
        '''
        log().info('修改单兵装备开始')
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/individualEquipmentController/detail.yaml'))
    def test_detail(self, data):
        '''
        查看单兵装备详情接口
        :param data:
        :return:
        '''
        log().info('查看单兵装备详情接口测试开始')
        res = set_request(self, data=data, method='get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/individualEquipmentController/delete.yaml'))
    def test_delete(self, data):
        '''
        删除单兵装备接口测试
        :param data:
        :return:
        '''
        log().info('删除单兵装备接口测试开始')
        for delete_id in TestIndividualEquipment.ids:
            data['data']['id'] = delete_id
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])


if __name__ == '__main__':
    pytest.main(['./test_individual_equipment.py::TestIndividualEquipment'])
