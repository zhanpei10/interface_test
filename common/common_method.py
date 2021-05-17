# 公共的方法
import yaml
import jsonpath
import json
import configparser
from config.log_dict import LOGGING_DIC
from logging import config
import logging


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
        data = yaml.load(f1, yaml.FullLoader)
    return data


def get_url(name, key):
    '''
    读取配置文件当中的接口地址信息
    :param name:
    :param key:
    :return: 返回获取到的接口地址
    '''
    conn = configparser.ConfigParser()
    conn.read(r'..\config\api_config.ini')
    path = conn.get(name.upper(), key)
    return path


def log():
    '''
    读取日志配置文件，格式化输出日志
    :return: 返回日志对象
    '''
    config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger('interface_case')
    return logger
