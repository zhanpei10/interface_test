'''
环境信息转装饰器
'''
from functools import wraps
from common.common_method import *


def environment(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        
        res = function(*args, **kwargs)
        return res

    return wrapper
