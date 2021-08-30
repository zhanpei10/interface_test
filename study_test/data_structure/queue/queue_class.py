'''
创建一个列表类
'''


class MyQueue:

    # 定义一个空队列
    def __init__(self):
        self.queue = []

    # 判断队列是否为空
    def is_empty(self):
        return self.queue == []

    # 插入队列 在队首进行插入 时间复杂度为O(n)
    def enqueue(self, value):
        self.queue.insert(0, value)

    # 获取队首的首个元素
    def dequeue(self):
        return self.queue.pop()

    # 返回队列的长度
    def size(self):
        return len(self.queue)
