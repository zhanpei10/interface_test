# 公共的方法
from api_keyword.interface_keyword import InterfaceKey
from common.get_config import *
import requests
import pymysql


def get_access_token():
    # url = 'http://10.111.32.82:10219/uums/auth/token'
    url = get_url() + 'uums/auth/token'
    data = {
        "grantType": "password",
        "identifyCode": "",
        "password": "kobe8888",
        "username": "kobekq1",
    }
    res = InterfaceKey().do_post(path=url, json=data)
    data = get_data_by_json(res.text, 'accessToken')
    if data:
        return data
    else:
        print(res.text)
        raise '登陆失败，无无法获取token'


def set_value(obj, **kwargs):
    '''
    给参数进行赋值
    :param obj:  测试用例对象
    :param kwargs:  当前用例请求的参数
    :return:  返回赋值好的字典
    '''
    for key, value in kwargs.items():
        if type(value) is dict:
            set_value(obj, **value)
        elif not value and type(value) is not bool and value != 0:
            if hasattr(obj, key):
                kwargs[key] = getattr(obj, key)
            else:
                kwargs[key] = None
    return kwargs


def set_value_two(obj, data):
    '''
    :param obj:
    :param data:
    :return:
    '''
    if type(data) is list:
        for i in data:
            set_value_two(obj, i)
    else:
        set_value(obj, **data)


def set_class_common(cls):
    '''
    类前置方法公共参数配置
    :param cls:
    :return:
    '''
    cls.kw = InterfaceKey()
    # 设置环境
    cls.host = get_url()
    # 设置token
    cls.accessToken = get_access_token()


def set_request(obj, data, method=None, address_id=None, import_file=None):
    '''
    设置url 请求头 请求参数
    :param file_obj:  文件对象
    :param import_file: 是否导入文件
    :param method:  发送什么请求 （post , get delete put）
    :param address_id:   拼接地址时加上id
    :param obj:  当前用例参数对象
    :param data:  需要赋值的数据
    :return:
    '''
    # 拼接url
    if address_id:
        url = obj.host + 'whale-openapi' + data['url'] + str(address_id)
    else:
        url = obj.host + 'whale-openapi' + data['url']
    # 设置请求头
    if 'headers' in data.keys():
        headers = set_value(obj, **data['headers'])
    else:
        headers = None
    # 设置参数
    if 'data' in data.keys():
        set_data = set_value(obj, **data['data'])
    else:
        set_data = None
    # 发送请求
    if not import_file:
        if method == 'post':
            if 'Content-Type' in headers.keys():
                res = obj.kw.do_post(path=url, headers=headers, data=set_data)
            else:
                res = obj.kw.do_post(path=url, headers=headers, json=set_data)
        elif method == 'get':
            res = obj.kw.do_get(path=url, headers=headers, params=set_data)
        elif method == 'delete':
            res = obj.kw.do_delete(path=url, headers=headers, params=set_data)
        else:
            res = obj.kw.do_put(path=url, headers=headers, json=set_data)
    else:
        res = obj.kw.do_import_file(path=url, headers=headers, data=set_data, files=import_file)
    return res


def get_parameter_by_interface(obj, data, method, key, context=None, import_file=None, ):
    '''
    调用关联的接口，给相关的参数赋值
    :param import_file:  是否是导入文件
    :param context: 说明
    :param obj:  用例对象
    :param data:  调用接口的参数
    :param method:  接口的方法
    :param key: 想要活动值的key  可以获取多个值
    :return:  返回获取值的列表或者字典
    '''
    log().info('>>>>>{}开始'.format(context))
    # 调用想要获取值的接口
    res = set_request(obj, data=data, method=method, import_file=import_file)
    # print(res.text)
    try:
        assert_date = get_data_by_json(res.text, 'errorMsg')
        assert assert_date == 'ok'
        # 判断想要获取几个值
        if type(key) is not list:
            # 单个值时，直接去返回的数据当中找  返回一个列表
            get_data = get_data_by_json(text=res.text, key=key)
            return_data = []
            # get_data为单个值时，将数据添加到列表当中返回
            if type(get_data) is not list:
                return_data.append(get_data)
                return return_data
            return get_data
        # 多个值时，返回字典  字典返回对应值的列表
        else:
            return_dic = {}
            for k in key:
                get_data = get_data_by_json(text=res.text, key=k)
                if type(get_data) is not list:
                    # 将值添加到列表当中再保存在字典当中
                    return_data = [0]
                    return_data[0] = get_data
                    return_dic[k] = return_data
                else:
                    return_dic[k] = get_data
            return return_dic
    except AssertionError as e:
        log().debug('--------***赋值接口值获取失败***----------')


def put_photo(token):
    '''
    调用上传图片的接口，返回图片路径
    :return:
    '''
    # 82环境的图片地址路径
    # url = 'http://10.111.32.82:10219/whale-general-service/generalservice/put'
    # 164
    url = get_url() + 'whale-general-service/generalservice/put'
    headers = {
        'accessToken': token
    }
    with open(filename() + '/common/import_file/put_photo.png', mode='rb') as f1:
        files = {
            'objectFile': f1
        }
        res = requests.put(url=url, headers=headers, files=files)
        try:
            assert get_data_by_json(text=res.text, key='errorMsg') == 'ok'
            log().info('>>>>>>>图片上传成功')
            return get_data_by_json(res.text, 'data')
        except AssertionError as e:
            raise e
            log().debug('--------*********上传图片接口调用失败*********----------')


if __name__ == '__main__':
    print(get_mysql_config('SIT_MYSQL'))
    conn = pymysql.connect(**get_mysql_config('SIT_MYSQL'))
    c = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from {0} where {1}={2}'.format('info_case', 'id', 1251)
    count = c.execute(sql)
    print(count)
