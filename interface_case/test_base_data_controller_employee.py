# 员工增删改查接口测试
import pytest
from common.common_method import *
from api_keyword.interface_keyword import InterfaceKey
import random
import os
import sys


class TestEmployee:

    @classmethod
    def setup_class(cls):
        '''
        类级别的前置方法
        :return:
        '''
        log().info('-------------员工增删改查相关接口测试开始-------------')
        set_class_common(cls)
        cls.keywords = None
        cls.username = 'autoTest' + str(random.randint(1, 10))
        cls.name = 'autoTest' + str(random.randint(11, 15))
        cls.id = None
        cls.userId = None
        cls.realName = 'kobeTest' + str(random.randint(1, 10))
        cls.login_id = None

    @classmethod
    def teardown_class(cls):
        log().info('--------员工相关接口测试完成----------')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/base_data_controller/employee/create_employee_data.yaml'))
    def test_create_employee(self, data):
        '''
        :param data:
        :return:
        '''
        log().info('新增用户接口开始执行----》')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        TestEmployee.keywords = self.name

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/base_data_controller/employee/query_employee_data.yaml'))
    def test_query_employee(self, data):
        '''
        根据关键字查询员工信息
        :param data:
        :return:
        '''
        log().info('查询员工信息开始----------》')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        TestEmployee.id = get_data_by_json(res.text, 'id')
        TestEmployee.userId = get_data_by_json(res.text, 'userId')
        TestEmployee.username = get_data_by_json(res.text, 'username')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/base_data_controller/employee/employee_detail_data.yaml'))
    def test_employee_detail(self, data):
        '''
        查询员工的详情信息
        :return:
        '''
        log().info('查询用户详情信息接口开始运行-------------》')
        res = set_request(self, data, 'get', address_id=self.id)
        make_assert(text=res.text, keyword='userId', assert_data=self.userId)

        @pytest.mark.parametrize('data', get_data_by_yaml(
            filename() + '/data/base_data_controller/employee/user_userId_reset_pwd.yaml'))
        def test_user_id_reset_pwd(self, data):
            '''
            重置用户密码接口测试
            :param data:
            :return:
            '''
            log().info('重置用户密码接口测试开始')
            url = data['url'] + str(self.userId) + '/reset-pwd'
            headers = set_value(self, **data['headers'])
            res = InterfaceKey().do_put(path=url, headers=headers)
            make_assert(text=res.text, keyword='errorMsg', assert_data='成功')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/base_data_controller/employee/update_employee_data.yaml'))
    def test_update_employee(self, data):
        '''
        对员工信息进行编辑
        :param data:
        :return:
        '''
        log().info('编辑员工接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/base_data_controller/employee/user_update_status.yaml'))
    def test_user_update_status(self, data):
        '''
        修改员工的禁用或者启动状态接口测试
        :param data:
        :return:
        '''
        log().info('修改员工的禁用或者启动状态接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/base_data_controller/employee/delete_employee_data.yaml'))
    def test_delete_employee(self, data):
        '''
        删除员工接口测试  伪删除
        :param data:
        :return:
        '''
        log().info('删除员工接口测试开始')
        print(self.id)
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/base_data_controller/vehicle/uums_token.yaml'))
    def test_uums_token(self, data):
        '''
        根据token获取登录用户的详细信息接口测试
        :param data:
        :return:
        '''
        log().info('根据token获取登录用户的详细信息接口测试开始')
        url = data['url'] + self.accessToken
        headers = set_value(self, **data['headers'])
        res = InterfaceKey().do_get(path=url, headers=headers)
        make_assert(text=res.text, keyword='errorMsg', assert_data='成功')
        TestEmployee.login_id = get_data_by_json(res.text, 'userId')

    @pytest.mark.parametrize('data',
                             get_data_by_yaml(filename() + '/data/base_data_controller/vehicle/uums_users_self.yaml'))
    def test_uums_users_self(self, data):
        '''
        更改登录用户的个人信息
        :param data:
        :return:
        '''
        log().info('更改登录用户的个人信息接口测试开始')
        headers = set_value(self, **data['headers'])
        request_data = set_value(self, **data['data'])
        res = InterfaceKey().do_put(path=data['url'], headers=headers, json=request_data)
        make_assert(text=res.text, keyword='errorMsg', assert_data='成功')

    @pytest.mark.parametrize('data', get_data_by_yaml(
        filename() + '/data/base_data_controller/vehicle/uums_users_self_modify-pwd.yaml'))
    def test_uums_users_self_modify_pwd(self, data):
        '''
        修改登录用户的密码接口测试
        :param data:
        :return:
        '''
        headers = set_value(self, **data['headers'])
        data['data']['id'] = self.login_id
        res = InterfaceKey().do_put(path=data['url'], headers=headers, json=data['data'])
        make_assert(text=res.text, keyword='errorMsg', assert_data='新密码与旧密码不能相等')


if __name__ == '__main__':
    pytest.main(['./test_base_data_controller_employee.py::TestEmployee'])
