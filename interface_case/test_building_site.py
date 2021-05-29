# 渣土车管控相关接口测试
# 根据车牌号判断渣土车是否取得处置证，true：是，false：否  未实现接口
# 渣土车当天轨迹 未实现接口
import pytest
from common.common_method import *
import time
import random


class TestBuilding:

    @classmethod
    def setup_class(cls):
        '''
        建筑工地相关接口测试
        :return:
        '''
        log().info('-----------------建筑工地相关接口测试开始------------------')
        set_class_common(cls)
        # 设置查询时间
        cls.startTime0 = time.strftime('%Y-%m-%d %H:%M:%S')
        time_c = time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'))
        cls.startTime1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_c + 15 * 24 * 60 * 60))
        cls.endTime0 = time.strftime('%Y-%m-%d %H:%M:%S')
        cls.endTime1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_c + 15 * 24 * 60 * 60))
        cls.serial = "PD20200930002"
        # 渣土车查询参数
        cls.minCase = random.randint(1, 10)
        cls.maxCase = random.randint(20, 30)
        cls.keywords = '沪A11111'
        # 事件列表参数
        cls.startTime = int(time.time() * 1000 - 15*24*60*60)
        cls.endTime = int(time.time() * 1000)
        # 查看告警图片
        cls.alarmId = None

    @classmethod
    def teardown_class(cls):
        '''
        :return:
        '''
        log().info('-----------------建筑工地相关接口测试结束------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/building_site/list.yaml'))
    def test_building_site_list(self, data):
        '''
        建筑工地列表查询接口测试
        :param data:
        :return:
        '''
        log().info('建筑工地列表查询接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/building_site/serial.yaml'))
    def test_building_site_serial(self, data):
        '''
        查询工地详情
        :param data:
        :return:
        '''
        log().info('查看工地详情接口测试开始')
        res = set_request(self, data, 'get', address_id=self.serial)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/process_service/building_site/report_record.yaml'))
    def test_building_site_report_record(self, data):
        '''
        查看申报记录接口测试
        :param data:
        :return:
        '''
        log().info('查看申报记录接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/refill/list.yaml'))
    def test_refill_list(self, data):
        '''
        回填点列表接口查询
        :param data:
        :return:
        '''
        log().info('回填点列表接口查询接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/refill/serial.yaml'))
    def test_refill_serial(self, data):
        '''
        回填点详情接口测试
        :param data:
        :return:
        '''
        log().info('回填点详情接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/process_service/truck/list.yaml'))
    def test_building_site_truck_list(self, data):
        '''
        渣土车辆管控运输车辆接口测试
        :param data:
        :return:
        '''
        log().info('渣土车辆管控运输车辆接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/detail.yaml'))
    def test_truck_detail(self, data):
        '''
        渣土车档案详情
        :param data:
        :return:
        '''
        log().info('渣土车档案详情接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/list_records.yaml'))
    def test_truck_list_records(self, data):
        '''
        查看历史申报记录接口测试
        :param data:
        :return:
        '''
        log().info('查看历史申报记录接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/track.yaml'))
    def test_truck_track(self, data):
        '''
        查看渣土车轨迹详情
        :param data:
        :return:
        '''
        log().info('查看渣土车轨迹详情接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/case/list.yaml'))
    def test_truck_case_list(self, data):
        '''
        渣土车事件列表详情接口
        :param data:
        :return:
        '''
        log().info('渣土车事件列表详情接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/list_capture.yaml'))
    def test_truck_list_capture(self, data):
        '''
        获取渣土车抓拍列表
        :return:
        '''
        log().info('获取渣土车抓拍列表接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        if not TestBuilding.alarmId:
            TestBuilding.alarmId = get_data_by_json(res.text, 'alarmId')[0]

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/ams_alarms.yaml'))
    def test_truck_ams_alarms(self, data):
        '''
        渣土车电子抓拍详情
        :param data:
        :return:
        '''
        log().info('渣土车渣土车电子抓拍详情详情接口测试开始')
        res = set_request(self, data, 'get', address_id=self.alarmId)
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/newest_capture.yaml'))
    def test_truck_newest_capture(self, data):
        '''
        最新抓拍图片接口
        :param data:
        :return:
        '''
        log().info('最新抓拍和最新事件接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/search_capture.yaml'))
    def test_truck_search_capture(self, data):
        '''
        搜抓拍接口
        :param data:
        :return:
        '''
        log().info('搜抓拍接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/dashboard.yaml'))
    def test_truck_dashboard(self, data):
        '''
        车辆统计相关
        :param data:
        :return:
        '''
        log().info('车辆统计相关接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/list_route.yaml'))
    def test_truck_list_route(self, data):
        '''
        查看渣土车路线接口测试
        :param data:
        :return:
        '''
        log().info('查看渣土车路线接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/driving.yaml'))
    def test_truck_driving(self, data):
        '''
        百度路线规划接口测试
        :param data:
        :return:
        '''
        log().info('百度路线规划接口测试测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/truck/capture_day_count.yaml'))
    def test_truck_capture_day_count(self, data):
        '''
        抓拍按天统计当天
        :param data:
        :return:
        '''
        log().info('抓拍按天统计当天接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/process_service/case/statistics_subject.yaml'))
    def test_case_statistics_subject(self, data):
        '''
        事件概括接口测试
        :param data:
        :return:
        '''
        log().info('事件概括接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')


if __name__ == '__main__':
    pytest.main(['./test_building_site.py::TestBuilding'])