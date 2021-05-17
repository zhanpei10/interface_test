# 对日志的读写级别进行配置
"""
logging配置
"""

import os
import time

# 1、定义三种日志输出格式，日志中可能用到的格式化串如下
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息

# 2、强调：其中的%(name)s为getlogger时指定的名字
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

# 3、日志配置字典
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # log文件的目录
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
LOG_NAME = time.strftime('%Y%m%d') + '_interface_auto_case.log'
LOG_DIR = os.path.join(LOG_DIR, LOG_NAME)

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    # 日志格式
    'formatters': {
        # 自定义的格式 可以是多个，stand simple test 名称可以修改
        'standard': {
            # 格式的基本样式，
            'format': standard_format  # 可以先用变量进行定义
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    # 控制日志输出的位置 日志的接收者
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',
            # 可以定制日志文件路径
            'filename': LOG_DIR,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M  文件的大小
            'backupCount': 5,  # 保存几份
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 'other': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',  # 保存到文件
        #     'formatter': 'test',
        #     'filename': 'a2.log',
        #     'encoding': 'utf-8',
        # },
    },
    # 负责产生者
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
    },
}

if __name__ == '__main__':
    print(os.path.dirname(os.path.dirname(__file__)))
    print(LOG_NAME)
    print(LOG_DIR)
