# 车辆管理相关接口测试
import pytest
from common.get_config import *
from common.assert_myself import *
import random
import time


class TestVehicle:

    @classmethod
    def setup_class(cls):
        '''
        车辆相关接口测试
        :return:
        '''
        log().info('-------------------车辆相关接口测试开始--------------------')
        set_class_common(cls)
        # 新增车辆相关参数
        cls.orgId = None  # 部门
        cls.powerType = None  # 动力
        cls.color = None  # 颜色
        cls.licensePlateNumber = '沪ATES' + str(random.randint(11, 99))  # 车牌号码
        cls.backUrls = None
        cls.driveUrls = None
        cls.frontUrls = None
        cls.leftUrls = None
        cls.rightUrls = None
        cls.annualReviewTime = time.strftime('%Y-%m-%d', time.localtime(time.time() + 60*24*60*60))
        cls.buyDate = time.strftime('%Y-%m-%d', time.localtime(time.time() - 60*24*60*60))
        cls.driveLicenseExpireDate = time.strftime('%Y-%m-%d', time.localtime(time.time() + 60*24*60*60))
        cls.transportCerfificateExpireDate = time.strftime('%Y-%m-%d', time.localtime(time.time() + 60*24*60*60))
        cls.ids = None
        cls.id = None

    @classmethod
    def teardown_class(cls):
        log().info('-------------------车辆相关接口测试结束--------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/vehicle_record_controller/create.yaml'))
    def test_create(self, data):
        '''
        新增车辆接口测试
        :param data:
        :return:
        '''
        log().info('>>>>新增车辆接口测试开始')
        # 获取部门信息
        if 'orgs' in data['url']:
            TestVehicle.orgId = get_parameter_by_interface(self, data, 'get', 'orgId', data['context'])[0]
        elif 'POWER_TYPE' in data['url']:
            TestVehicle.powerType = get_parameter_by_interface(self, data, 'get', 'content', data['context'])[0]
        elif 'VEHICLE_COLOR' in data['url']:
            TestVehicle.color = get_parameter_by_interface(self, data, 'get', 'content', data['context'])[0]
        elif 'upload' in data['url']:
            photo_name = {
                'backUrls': '/common/import_file/car_photo/car_back.png',
                'driveUrls': '/common/import_file/car_photo/car_driver.png',
                'frontUrls': '/common/import_file/car_photo/car_front.png',
                'leftUrls': '/common/import_file/car_photo/car_left.png',
                'rightUrls': '/common/import_file/car_photo/car_right.png',
            }
            for key, address in photo_name.items():
                with open(filename() + address, mode='rb') as f1:
                    files = {
                        'file': f1
                    }
                    if key == 'backUrls':
                        TestVehicle.backUrls = \
                        get_parameter_by_interface(self, data, 'post', 'data', data['context'], files)[0]
                    elif key == 'driveUrls':
                        TestVehicle.driveUrls = \
                        get_parameter_by_interface(self, data, 'post', 'data', data['context'], files)[0]
                    elif key == 'frontUrls':
                        TestVehicle.frontUrls = \
                        get_parameter_by_interface(self, data, 'post', 'data', data['context'], files)[0]
                    elif key == 'leftUrls':
                        TestVehicle.leftUrls = \
                        get_parameter_by_interface(self, data, 'post', 'data', data['context'], files)[0]
                    else:
                        TestVehicle.rightUrls = \
                        get_parameter_by_interface(self, data, 'post', 'data', data['context'], files)[0]
        else:
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/vehicle_record_controller/import.yaml'))
    def test_import(self, data):
        '''
        批量导入车辆接口测试
        :param data:
        :return:
        '''
        log().info('>>>>批量导入车辆接口测试开始')
        with open(filename() + '/common/import_file/car_import.xlsx', mode='rb') as f1:
            files = {
                'file': f1,
            }
            res = set_request(self, data=data, method='post', import_file=files)
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/vehicle_record_controller/page.yaml'))
    def test_page(self, data):
        '''
        查询车辆所有页
        :param data:
        :return:
        '''
        log().info('>>>查询车辆所有页接口测试开始')
        res = set_request(self, data, method='post')
        if 'keywords' in data['data'].keys():
            if '不存在的车牌号' == data['data']['keywords']:
                make_assert_list_len(text=res.text, keyword='dataList', context=data['context'], len_list=0)
            else:
                make_assert_list_len(text=res.text, keyword='dataList', context=data['context'])
                res_data = get_data_by_json(res.text, key='id')
                if type(res_data) is list:
                    TestVehicle.ids = res_data
                    TestVehicle.id = res_data[0]
                else:
                    TestVehicle.id = res_data
        else:
            make_assert_list_len(text=res.text, keyword='dataList', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/vehicle_record_controller/detail.yaml'))
    def test_detail(self, data):
        '''
        获得车辆详情接口测试
        :param data:
        :return:
        '''
        log().info('>>>获得车辆详情接口测试开始')
        res = set_request(self, data=data, method='get')
        make_assert(text=res.text, keyword='id', assert_data=self.id, context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/vehicle_record_controller/update.yaml'))
    def test_update(self, data):
        '''
        修改车辆接口测试
        :param data:
        :return:
        '''
        log().info('>>>修改车辆接口测试开始')
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/vehicle_record_controller/delete.yaml'))
    def test_delete(self, data):
        '''
        删除车辆接口测试
        :param data:
        :return:
        '''
        log().info('>>>删除车辆接口测试开始')
        for delete_id in self.ids:
            data['data']['id'] = delete_id
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])


if __name__ == '__main__':
    pytest.main(['./test_vehicle.py::TestVehicle'])
