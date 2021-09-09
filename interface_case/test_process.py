# 事件流程相关接口测试
import pytest
from common.get_config import *
from common.assert_myself import *


class TestProcess:

    @classmethod
    def setup_class(cls):
        '''
        流程相关接口测试前置方法
        :return:
        '''
        log().info('---------------------事件流程相关接口测试开始----------------------------')
        set_class_common(cls)

    @classmethod
    def teardown_class(cls):
        log().info('---------------------事件流程相关接口测试结束----------------------------')
