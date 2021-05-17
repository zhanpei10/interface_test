import requests

import json


class InterfaceKey:

    # get请求
    def do_get(self, path, params=None, headers=None, **kwargs):
        '''

        :param path:   请求的路径
        :param params:   请求的参数
        :param headers:  请求头部
        :param kwargs:  get请求的其他参数
        :return:  返回请求的得到的报文
        '''
        return requests.get(url=path, params=params, headers=headers, **kwargs)

    # post请求
    def do_post(self, path, data=None, json=None, **kwargs):
        '''

        :param path:
        :param data:  post的普通类型参数
        :param json:  json格式的参数
        :param kwargs:
        :return:
        '''
        return requests.post(url=path, data=data, json=json, **kwargs)

    # put请求
    def do_put(self, path, data=None, json=None, **kwargs):
        '''

        :param path:
        :param data:
        :param json:
        :param kwargs:
        :return:
        '''
        return requests.put(url=path, data=data, json=json, **kwargs)

    # delete请求
    def do_delete(self, path, data=None, json=None, **kwargs):
        '''

        :param path:
        :param data:
        :param json:
        :param kwargs:
        :return:
        '''
        return requests.delete(url=path, params=None, **kwargs)



