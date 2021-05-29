# # 车载装备相关接口测试
# import pytest
# from common.common_method import *
#
#
# class TestVehicleDevice:
#
#     @classmethod
#     def setup_class(cls):
#         '''
#         车载装备相关接口测试前置方法
#         :return:
#         '''
#         log().info('-------------------车载装备相关接口测试开始------------------------')
#         set_class_common(cls)
#
#     @classmethod
#     def teardown_class(cls):
#         '''
#
#         :return:
#         '''
#         log().info('-------------------车载装备相关接口测试结束------------------------')
#
#     @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/vehicle_zdevice_controller/create.yaml'))
#     def test_create(self, data):
#         '''
#         新建车载装备接口测试
#         :param data:
#         :return:
#         '''
#         log().info('>>>新建车载装备接口测试开始')
#         pass
#
#
# if __name__ == '__main__':
#     pytest.main(['./test_vehicle_device.py::TestVehicleDevice'])
