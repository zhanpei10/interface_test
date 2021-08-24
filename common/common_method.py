# 公共的方法
import yaml
import jsonpath
import json
import configparser
from config.log_dict import LOGGING_DIC
from logging import config
import logging
from api_keyword.interface_keyword import InterfaceKey
import os
from api_keyword.interface_keyword import InterfaceKey
import requests
import pymysql


def get_data_by_json(text, key):
    '''
    context: 对接口的返回的json数据进行解析，获取想要的数据
    :param text:  需要解析的文本
    :param key:  想要获取的字段
    :return:  返回查询到的字段
    '''
    text = json.loads(text)
    # 根据路径查找对应的属性值 返回一个列表
    value = jsonpath.jsonpath(text, '$..{0}'.format(key))
    if value:
        if len(value) == 1:
            return value[0]
    return value


def get_data_by_yaml(path):
    '''

    读取yaml文件的内容，进行数据驱动，实现数据和用例的分离
    :param path:  yaml文件的路径
    :return:  返回获取到的yaml数据

    '''
    data = None
    with open(path, mode='rt', encoding='utf-8') as f1:
        data = yaml.load(f1, yaml.FullLoader, )
    return data


def get_url(name, key):
    '''
    读取配置文件当中的接口地址信息
    :param name:
    :param key:
    :return: 返回获取到的接口地址
    '''
    conn = configparser.ConfigParser()
    conn.read(filename() + '/config/api_config.ini')
    path = conn.get(name.upper(), key)
    return path


def get_mysql_config(name):
    conn = configparser.ConfigParser()
    conn.read(filename() + '/config/mysql_config.ini')
    config_dict = {
        'host': None,
        'port': None,
        'user': None,
        'passwd': None,
        'charset': None,
        'database': None,
    }
    for key in config_dict.keys():
        if key == 'port':
            config_dict[key] = int(conn.get(name.upper(), key))
        else:
            config_dict[key] = conn.get(name.upper(), key)
    return config_dict


def log():
    '''
    读取日志配置文件，格式化输出日志
    :return: 返回日志对象
    '''

    config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger('interface_case')
    return logger


def get_access_token():
    url = 'http://10.111.32.82:10219/uums/auth/token'
    data = {
        "grantType": "password",
        "identifyCode": "",
        "password": "kobe8888",
        "username": "kobeAdmin001",
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
    if type(data) is list:
        for i in data:
            set_value_two(obj, i)
    else:
        set_value(obj, **data)


def make_assert(text, keyword, assert_data, context=None):
    '''
    根据接口返回的值设置断言
    :param context:  测试接口说明
    :param text:
    :param keyword:
    :param assert_data:
    :return:
    '''
    data = get_data_by_json(text, keyword)
    try:
        assert data == assert_data
        if context:
            log().info('----------->>>{0}>>>---------------'.format(context))
        log().info('----------------->>>当前接口测试成功>>>-----------------')
        log().info('接口返回的报文内容>>>')
        log().info(text)
    except AssertionError as E:
        log().debug('---------------------->>>当前接口测试失败>>>----------------')
        log().debug('失败接口返回的报文>>>')
        log().debug(text)
        log().debug(E)
        raise E


def make_assert_list_len(text, keyword, context, len_list=1):
    '''
    根据返回的列表长度做断言
    :param len_list:
    :param text:
    :param keyword:
    :param list_len:
    :param context:
    :return:
    '''
    response_data = get_data_by_json(text, keyword)
    try:
        if not len_list:
            assert len(response_data) == 0
        else:
            assert len(response_data) != 0
        if context:
            log().info('----------- >>>{0}>>>---------------'.format(context))
        log().info('----------------->>>当前接口测试成功>>>-----------------')
        log().info('接口返回的报文内容>>>')
        log().info(text)
    except AssertionError as E:
        log().debug('------------>>>{0}--------------'.format(context))
        log().debug('------------------>>>当前接口测试失败,接口返回了空数据>>>----------------')
        log().debug('失败接口返回的报文>>>')
        log().debug(text)
        log().debug(E)
        raise E


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
        url = obj.host + data['url'] + str(address_id)
    else:
        url = obj.host + data['url']
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


def filename():
    '''
    返回项目地址
    :return: 
    '''
    return os.path.dirname(os.path.dirname(__file__))


def set_class_common(cls):
    '''
    类前置方法公共参数配置
    :param cls:
    :return:
    '''
    cls.kw = InterfaceKey()
    cls.host = cls.host = get_url('skyline_sit', 'sit_host')
    # cls.host = cls.host = get_url('SKYLINE_THREE', 'host')
    cls.accessToken = get_access_token()


def get_parameter_by_interface(obj, data, method, key, context=None, import_file=None, ):
    '''
    调用关联的接口，给相关的参数赋值
    :param import_file:  是否是导入文件
    :param context: 说明
    :param obj:  用例对象
    :param data:  调用接口的参数
    :param method:  接口的方法
    :param key: 想要活动值的key
    :return:
    '''
    log().info('>>>>>{}开始'.format(context))
    res = set_request(obj, data=data, method=method, import_file=import_file)
    # print(res.text)
    try:
        assert_date = get_data_by_json(res.text, 'errorMsg')
        assert assert_date == 'ok'
        if type(key) is not list:
            get_data = get_data_by_json(text=res.text, key=key)
            return_data = []
            if type(get_data) is not list:
                return_data.append(get_data)
                return return_data
            return get_data
        else:
            return_dic = {}
            for k in key:
                get_data = get_data_by_json(text=res.text, key=k)
                if type(get_data) is not list:
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
    url = 'http://10.111.32.82:10219/whale-general-service/generalservice/put'
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

