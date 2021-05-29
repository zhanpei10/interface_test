# 会议通知接口测试
import pytest
from common.common_method import *
import time
import random


class TestMeetingNotice:
    '''
    会议通知相关接口测试
    '''

    @classmethod
    def setup_class(cls):
        '''
        会议通知的前置方法
        :return:
        '''
        log().info('----------会议通知相关接口测试开始------------')
        set_class_common(cls)
        cls.userIds = None
        # 会议主题
        cls.subject = 'autoTest_' + str(int(random.randint(1, 10)))
        cls.subject_cg = 'autoTest_' + str(int(random.randint(10, 20)))
        # 设置会议的开始和截止时间
        cls.endTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() + 49 * 60 * 60))
        cls.startTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() + 48 * 60 * 60))
        # 附件列表
        cls.annexs = []
        # 查询接口相关参数  设置查询的起止时间
        cls.endTime_cx = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() + 20 * 60))
        cls.startTime_cx = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - 30 * 24 * 60 * 60))
        # 保存会议的id信息
        cls.id = None
        cls.id_cgs = None
        # 我的日程查看会议通知列表
        cls.date = time.strftime('%Y-%m-%d', time.localtime(time.time() + 48 * 60 * 60))

    @classmethod
    def teardown_class(cls):
        '''
        会议通知的后置方法
        :return:
        '''
        log().info('----------会议通知相关接口测试结束------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/meeting_notice_controller/annex_upload.yaml'))
    def test_annex_upload(self, data):
        '''
        上传会议附件接口测试
        :param data:
        :return:
        '''
        log().info('附件上传接口测试')
        with open(filename() + '/common/import_file/meeting/{0}'.format(data['file_name']), mode='rb') as f1:
            files = {
                'file': f1
            }
            res = set_request(self, data=data, method='post', import_file=files)
            make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/meeting_notice_controller/create_publish.yaml'))
    def test_create_publish(self, data):
        '''
        现建并推送会议管理
        :param data:
        :return:
        '''
        log().info('>>>新建并推送会议管理开始')
        # 获取用户id
        if 'users' in data['url']:
            TestMeetingNotice.userIds = get_parameter_by_interface(self, data, 'post', 'userId', data['context'])
        # 上传文件接口调用
        elif 'upload' in data['url']:
            with open(filename() + '/common/import_file/meeting/word_test.docx', mode='rb') as f1:
                files = {
                    'file': f1
                }
                address = get_parameter_by_interface(self, data, 'post', 'data', data['context'], files)[0]
                files_dic = {'annexName': 'word_test.docx', 'annexUrl': address, 'fileType': 3}
                TestMeetingNotice.annexs.append(files_dic)
        else:
            res = set_request(self, data=data, method='post')
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/meeting_notice_controller/notice_save.yaml'))
    def test_notice_save(self, data):
        '''
        保存为草稿接口测试
        :param data:
        :return:
        '''
        log().info('保存会议通知为草稿接口测试')
        data['data']['subject'] = self.subject_cg
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/meeting_notice_controller/page.yaml'))
    def test_page(self, data):
        '''
        查询会议通知接口测试
        :param data:
        :return:
        '''
        log().info('查询会议通知接口测试')
        data['data']['endTime'] = self.endTime_cx
        data['data']['startTime'] = self.startTime_cx
        res = set_request(self, data=data, method='post')
        print('-----------------------------------------')
        print(res.request.body)
        make_assert_list_len(text=res.text, keyword='dataList', context=data['context'])
        if data['data']['status'] == 2:
            TestMeetingNotice.id = get_data_by_json(res.text, 'id')[0]
        elif data['data']['status'] == 1:
            TestMeetingNotice.id_cgs = get_data_by_json(res.text, 'id')
            print(self.id_cgs)

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/meeting_notice_controller/notice_update.yaml'))
    def test_notice_update(self, data):
        '''
        修改草稿箱接口测试
        :param data:
        :return:
        '''
        log().info('修改草稿箱接口测试开始')
        data['data']['id'] = self.id_cgs[0]
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/meeting_notice_controller/detail.yaml'))
    def test_detail(self, data):
        '''
        查询会议通知详情
        :param data:
        :return:
        '''
        log().info('查询会议通知详情接口测试')
        # 查询草稿箱详情
        if '草稿' in data['context']:
            res = set_request(self, data=data, method='get', address_id=self.id_cgs[0])
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])
        else:
            res = set_request(self, data=data, method='get', address_id=99)
            make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/meeting_notice_controller/update_publish.yaml'))
    def test_update_publish(self, data):
        '''
        更新发布会议通知接口测试
        :param data:
        :return:
        '''
        log().info('更新发布会议通知接口测试开始')
        res = set_request(self, data=data, method='post')
        print(res.request.body)
        print(res.text)

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/meeting_notice_controller/notice_delete.yaml'))
    def test_notice_delete(self, data):
        '''
        删除草稿箱接口测试
        :param data:
        :return:
        '''
        log().info('删除草稿箱接口测试开始')
        data['data']['id'] = self.id_cgs[1]
        res = set_request(self, data=data, method='post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/meeting_notice_controller/notice_urge.yaml'))
    def test_notice_urge(self, data):
        '''
        催办接口测试
        :param data:
        :return:
        '''
        log().info('>>>催办接口测试')
        res = set_request(self, data=data, method='post')
        print(res.request.body)
        print(res.text)

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/meeting_notice_controller/notice_cancel.yaml'))
    def test_notice_cancel(self, data):
        '''
        取消会议通知提醒
        :param data:
        :return:
        '''
        log().info('取消会议通知提醒')
        res = set_request(self, data=data, method='post')
        print(res.request.body)
        print(res.text)

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/meeting_notice_controller/notice_export.yaml'))
    def test_notice_export(self, data):
        '''
        导出会议通知
        :param data:
        :return:
        '''
        log().info('导出会议通知测试开始')
        data['data']['endTime'] = self.endTime_cx
        data['data']['startTime'] = self.startTime_cx
        res = set_request(self, data=data, method='post')
        print(res.request.body)
        make_assert(text=res.text, assert_data='ok', keyword='errorMsg', context=data['context'])

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/meeting_notice_controller/notice_schedule.yaml'))
    def test_notice_schedule(self, data):
        '''
        我的日程当中展示会议列表
        :param data:
        :return:
        '''
        log().info('我的日程当中展示会议列表接口测试开始')
        res = set_request(self, data=data, method='post')
        # print(res.text)
        make_assert_list_len(text=res.text, keyword='data', context=data['context'])


if __name__ == '__main__':
    pytest.main(['./test_meeting_notice.py::TestMeetingNotice::test_detail'])
