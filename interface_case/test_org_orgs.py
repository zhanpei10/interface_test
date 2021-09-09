# 部门相关接口测试
import pytest
from common.get_config import *
from common.assert_myself import *
from api_keyword.interface_keyword import InterfaceKey
import random


class TestOrg:

    @classmethod
    def setup_class(cls):
        '''
        部门接口测试前置方法
        :return:
        '''
        log().info('-------------------部门相关接口测试开始----------------------')
        # cls.kw = InterfaceKey()
        # cls.host = cls.host = get_url('skyline_sit', 'sit_host')
        # cls.accessToken = get_access_token()
        set_class_common(cls)
        # 新增部门相关参数值设置
        cls.address = 'address_' + str(random.randint(1, 100000))
        cls.area = random.randint(1, 1000)
        cls.organName = 'organName_' + str(random.randint(1, 100000))
        cls.orgName = None
        cls.id = None
        cls.organId = None
        cls.parentOrgId = None

    @classmethod
    def teardown_class(cls):
        '''
        后置函数
        :return:
        '''
        log().info('-------------------部门相关接口测试结束----------------------')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/gms_org_controller/org_orgs_create.yaml'))
    def test_org_orgs_create(self, data):
        '''
        新增部门接口测试
        :param data:
        :return:
        '''
        log().info('新增部门接口测试开始')
        res = set_request(self, data, 'post')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        TestOrg.orgName = self.organName

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/gms_org_controller/org_orgs.yaml'))
    def test_org_orgs(self, data):
        '''
        根据部门名称查询部门
        :param data:
        :return:
        '''
        log().info('根据部门名称查询部门接口测试开始')
        res = set_request(self, data, 'get')
        make_assert(text=res.text, keyword='errorMsg', assert_data='ok')
        TestOrg.id = get_data_by_json(res.text, 'orgId')
        TestOrg.organId = get_data_by_json(res.text, 'orgId')
        TestOrg.parentOrgId = get_data_by_json(res.text, 'parentId')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/gms_org_controller/uums_orgs_by_id.yaml'))
    def test_uums_orgs_by_id(self, data):
        '''
        根据部门id查看部门详情接口测试
        :param data:
        :return:
        '''
        log().info('根据部门id查看部门详情接口测试开始')
        url = data['url'] + str(self.id)
        headers = set_value(self, **data['headers'])
        res = InterfaceKey().do_get(path=url, headers=headers)
        make_assert(text=res.text, keyword='errorMsg', assert_data='成功')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/gms_org_controller/update_orgs_by_id.yaml'))
    def test_update_orgs_by_id(self, data):
        '''
        根据部门id修改部门信息
        :param data:
        :return:
        '''
        log().info('根据部门id修改部门信息接口测试开始')
        url = data['url'] + str(self.id)
        headers = set_value(self, **data['headers'])
        update_data = set_value(self, **data['data'])
        res = InterfaceKey().do_put(path=url, headers=headers, json=update_data)
        make_assert(text=res.text, keyword='errorMsg', assert_data='成功')

    @pytest.mark.parametrize('data', get_data_by_yaml(filename() + '/data/gms_org_controller/detete_orgs_by_id.yaml'))
    def test_detete_orgs_by_id(self, data):
        '''
        根据id删除部门接口测试
        :param data:
        :return:
        '''
        log().info('根据id删除部门接口测试开始')
        url = data['url'] + str(self.id)
        headers = set_value(self, **data['headers'])
        res = InterfaceKey().do_delete(path=url, headers=headers)
        make_assert(text=res.text, keyword='errorMsg', assert_data='成功')


if __name__ == '__main__':
    pytest.main(['./test_org_orgs.py::TestOrg'])
