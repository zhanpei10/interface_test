'''
模拟流程

1、创建队列对象
2、模拟主要流程
    按概率生成打印作业，加入打印队列
    判断打印机是否空闲，且队列是否为空
    如果打印机忙，按打印速度进行1秒打印
    打印完成，打印机进入空闲
    几个概念；
        1、作业等待时间
            生成作业时，记录作业的时间戳
            开始打印时，当前 时间减去生成时间即可
        2、作业的打印时间
            生成作业时，记录作业的页页数
            开始打印时，页面除以打印的速度
3、时间用尽计算拼接等待时间
'''
import random
from study_test.data_structure.queue.queue_class import MyQueue
import time


class Printer:
    '''
    打印机类
    '''

    def __init__(self, ppm):
        '''
        定义打印机相关参数
        :param ppm:  打印的速度 ，每分钟打印多少次
        '''
        self.page_rate = ppm  # 打印速度
        self.current_task = None  # 打印任务
        self.timeRemaining = 0  # 任务倒计时， 为0是打印结束  任务的执行时间 根据作业的打印时间决定

    def tick(self):
        '''
        开始每秒执行打印
        :return:
        '''
        if self.current_task != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        '''
        打印新任务
        :param new_task:
        :return:
        '''
        # 获得一个打印任务
        self.current_task = new_task
        # 计算打印时长，根据打印模式计算打印时长
        self.timeRemaining = new_task.get_page_size() * 60 / self.page_rate


class Task:
    '''
    打印任务类
    '''

    def __init__(self, time1):
        self.start_time = time1  # 保存打印任务的开始时间 用于计算等待时间
        self.page_size = random.randint(1, 21)  # 随机生成打印页数，在1到20页之间

    def get_start_time(self):
        '''
        返回打印任务开始的生成时间
        :return:
        '''
        return self.start_time

    def get_page_size(self):
        '''
        返回打印页数
        :return:
        '''
        return self.page_size

    def make_wait_time(self, curr):
        '''
        返回打印的等待时间 当前时间减去任务的开始时间
        :return:
        '''
        return curr - self.get_start_time()


def if_task():
    '''
    根据概率生成打印任务
    :return:
    '''
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def begin(cycle, model):
    '''
    开始模拟打印流程
    :param cycle:  任务的执行周期
    :param model: 打印的模式
    :return:
    '''
    print1 = Printer(model)  # 生成一个打印机
    queue = MyQueue()  # 生成一个打印队列
    wait_time_list = []  # 等待时间列表
    for i in range(cycle):
        # i表示当前的时间
        # 根据概率判断是否生成打印任务
        if if_task():
            t1 = Task(i)
            queue.enqueue(t1)
        # 判断打印机是否在忙，且打印队列是否为空，不为空生成一个新的打印任务并执行
        if (not print1.busy()) and (not queue.is_empty()):
            print1.start_next(queue.dequeue())
            # 计算等待时间
            wait_time_list.append(t1.make_wait_time(i))
        # 开始进行每秒打印
        print1.tick()
    # 计算打印时间

    print(sum(wait_time_list) / len(wait_time_list), end='  ')
    print('还未打印的任务 {}个'.format(queue.size()))


if __name__ == '__main__':
    for i in range(10):
        begin(3600, 20)
