# 请假申请相关接口测试
import pytest
from common.get_config import *
from common.assert_myself import *
import time


class TestLeave:
    '''
    请假相关接口测试类
    '''

    @classmethod
    def setup_class(cls):
        '''

        :return:
        '''
        log().info('-----------------请假相关接口测试开始-------------------')
        set_class_common(cls)
        cls.attachments = [{
            'fileName': 'put_photo.png',
            'type': 1,
            'url': put_photo(cls.accessToken),
        }]
        cls.configIds = None
        cls.endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 24 * 60 * 60))
        cls.startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cls.length = int(((int(time.time() + 24 * 60 * 60) * 1000) - (int(time.time()) * 1000)) / 3600 / 1000)

    @classmethod
    def teardown_class(cls):
        log().info('----------------请假相关接口测试结束-----------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/leave_controller/save.yaml'))
    def test_save(self, data):
        '''
        请假申请
        :param data:
        :return:
        '''
        log().info('新增请假申请测试开始')
        # 获取请假类型id
        if 'query' in data['url']:
            # TestLeave.configIds = get_parameter_by_interface(self, data, 'post', 'id', data['context'])
            TestLeave.configIds = [51]
            print(self.configIds)
        else:
            # 传入请假类型id
            for configId in self.configIds:
                data['data']['configId'] = configId
                res = set_request(self, data=data, method='post')
                print(res.request.body)
                print(res.text)

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/leave_controller/commit.yaml'))
    def test_commit(self, data):
        '''
        提交审核申请
        :param data:
        :return:
        '''
        log().info('这是请假审核信息')
        res = set_request(self, data=data, method='post')
        print(res.request.body)
        print(res.text)


if __name__ == '__main__':
    pytest.main(['./test_leave.py::TestLeave::test_save'])
