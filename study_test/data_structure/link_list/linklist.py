'''
自定义一个链表
    1、add  添加一个元素
    2、size 获取链表的长度
    3、search  查询链表
    4、remove 删除指定的值
    5、end     获取队尾节点
    6、push   从队尾插入元素
    7、pop  从列表尾部删除元素
'''
from study_test.data_structure.link_list.linknode import LinkNode


class LinkList:

    def __init__(self):
        '''
        初始化表头，指向对一个节点，为空表示一个空列表
        '''
        self.head = None

    def is_empty(self):
        '''
        判断列表是否为空 根据表头进行判断
        :return:
        '''
        return self.head is None

    def add_value(self, item):
        '''
        新增一个值到链表 从链表的头部进行插入
        :return:
        '''
        # 新增节点保存对应的值
        node = LinkNode(item)
        # 将之间的节点移动到新增的节点后面
        node.set_next(self.head)
        # 将头节点指向新增的节点
        self.head = node

    def size(self):
        '''
        返回队列的长度，从列表头部开始遍历，直到遍历到最后一个
        时间复杂度是O(n)
        :return:
        '''
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        '''

        :param item:
        :return:
        '''
        current = self.head
        found = False
        while (not found) and current is not None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        '''
        删除一个节点， 操作，将上一个节点的next 指向删除节点的next,则删除成功
        如果是第一个节点，则直接将head指向空即可
        :param item:
        :return:
        '''
        # 保存当前节点
        current = self.head
        # 保存当前节点的上一个节点
        last_current = None
        # 记录是否找到
        found = False
        while (not found) and (current is not None):
            if current.get_data() == item:
                found = True
            else:
                last_current = current
                current = current.get_next()
        # 当last_current 节点等于null时，说明要删除的是第一个节点
        if last_current is None:
            self.head = current.get_next()
        # 如果找到对应的值，将上一个节点的next 指向 删除节点的next
        if found:
            last_current.set_next(current.get_next())

    def end_current(self):
        '''
        获取队尾元素
            查到最后一个元素，直达next为空，即为最后一个元素 时间复杂度为o(n)
        :return:
        '''
        current = self.head
        # 标记是否找到
        found = False
        while (current is not None) and (not found):
            if current.get_next() is None:
                found = True
            else:
                current = current.get_next()
        return current

    def push(self, item):
        '''
        从链表的尾部获取一个元素
            需要查询出最后一个元素
            将尾部元素的next修改为当前元素  时间复杂度为O(n)
        :return:
        '''
        node = LinkNode(item)
        self.end_current().set_next(node)

    def pop(self):
        '''
        从链表 的尾部删除一个元素
            记录最后一个元素的上一个元素
            找到最后元素 ，最后一个元素的next改为none
        :return:
        '''
        current = self.head
        # 记录最后一个元素的上一个元素
        last_current = None
        found = False
        while (current is not None) and (not found):
            if current.get_next() is None:
                found = True
            else:
                last_current = current
                current = current.get_next()
        # 当last_current为none 说明要删除的元素为第一个元素 或者是个空链表
        # 可以将head直接变为空
        if last_current is None:
            self.head = None
        # 如果找到最后元素，将最后一个元素的next改为None
        if found:
            last_current.set_next(None)
        if current is None:
            return '为空链表'
        else:
            return current.get_data()


if __name__ == '__main__':
    my_link_list = LinkList()
    print(my_link_list.is_empty())
    my_link_list.add_value(10)
    my_link_list.add_value(22)
    my_link_list.add_value(33)
    print(my_link_list.size())
    print(my_link_list.is_empty())
    print(my_link_list.search(22))
    my_link_list.remove(22)
    print(my_link_list.size())
    print(my_link_list.end_current().get_data())
    my_link_list.push(44)
    print(my_link_list.end_current().get_data())
    print(my_link_list.pop())
    print(my_link_list.size())
