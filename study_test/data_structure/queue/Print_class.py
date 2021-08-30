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
            if self.timeRemaining <= None:
                self.currentTask = None

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
        self.current_task = new_task
        self.timeRemaining = new_task.getPages() * 60 / self.page_rate