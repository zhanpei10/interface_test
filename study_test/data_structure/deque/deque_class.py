# 自定义一个双端队列
class MyDeque:
    def __init__(self):
        '''
        定义一个空的队列
        列表的开头是队尾
        列表的结束是队首
        '''
        self.deque = []

    def add_front(self, value):
        '''
        从队首添加元素 复杂度是O(1)
        :return:
        '''
        self.deque.append(value)

    def add_rear(self, value):
        '''
        从队尾添加元素 复杂度是O(n)
        :return:
        '''
        self.deque.insert(0, value)

    def remove_front(self):
        '''
        从队首取元素 复杂度是O(1)
        :return:
        '''
        return self.deque.pop()

    def remove_rear(self):
        '''
        从队首取元素 复杂度是O(n)
        :return:
        '''
        return self.deque.pop(0)

    def is_empty(self):
        '''
        判断队列是否为空
        :return:
        '''
        return self.deque == []

    def size(self):
        '''
        返回队列的长度
        :return:
        '''
        return len(self.deque)
