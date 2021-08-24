''''
使用列表创建一个栈 列表末尾作为栈顶
'''
import time


class MyStack:

    def __init__(self):
        self.demo = []

    def is_empty(self):
        '''
        判断栈是否为空
        :return:
        '''
        return self.demo == []

    def push(self, data):
        '''
        向栈当中插入数据
        :return:
        '''
        self.demo.append(data)

    def pop(self):
        '''
        获取栈中的数据
        :return:
        '''
        return self.demo.pop()

    def len(self):
        '''
        获取栈的长度
        :return:
        '''
        return len(self.demo)

    def look_all(self):
        '''
        查看栈的所有内容
        :return:
        '''
        # print(self.demo)
        return self.demo

    def look_first(self):
        '''
        查看栈顶元素
        :return:
        '''
        # print(self.demo[len(self.demo) - 1])
        return self.demo[len(self.demo) - 1]


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.look_first()
    stack.look_all()
    time.sleep(2)
    stack.push(2)
    stack.look_first()
    stack.look_all()
    time.sleep(2)
    stack.push(3)
    stack.look_first()
    stack.look_all()
    time.sleep(2)
    stack.push(4)
    stack.look_first()
    stack.look_all()
    time.sleep(2)
    stack.pop()
    stack.look_first()
    stack.look_all()
    time.sleep(2)
    stack.pop()
    stack.look_first()
    stack.look_all()
    time.sleep(2)
    stack.pop()
    stack.look_first()
    stack.look_all()
    time.sleep(2)
