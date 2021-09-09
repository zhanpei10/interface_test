'''
自定义的断言语句
'''
from common.common_method import *


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


def make_assert_is_none(text, keyword, context):
    '''
    判断发挥的数值是不是none
    :param text:
    :param keyword:
    :param context:
    :return:
    '''
    data = get_data_by_json(text=text, key=keyword)
