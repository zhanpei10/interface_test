'''
新建一个链表 的节点对象
    存在两个信息
        1、data数据本身
        2、next 指向下一个节点的引用信息
'''


class LinkNode:

    def __init__(self, init_data):
        '''

        :param init_data: 创建节点的初始值
        '''
        self.data = init_data
        self.next = None  # 下一个节点信息

    def get_data(self):
        '''
        获得实际的值
        :return:
        '''
        return self.data

    def get_next(self):
        '''
        获取下一个节点的引用
        :return:
        '''
        return self.next

    def set_data(self, new_data):
        '''
        设置实际的值
        :return:
        '''
        self.data = new_data

    def set_next(self, new_next):
        '''
        设置下一个节点
        :param new_next:
        :return:
        '''
        self.next = new_next
