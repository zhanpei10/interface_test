'''
有序链表创建
'''
from study_test.data_structure.link_list.linknode import LinkNode


class LinkListSort:

    def __init__(self):
        '''
        初始化链表
        '''
        self.head = None

    def is_empty(self):
        '''
        判断链表是否为空
        :return:
        '''
        return self.head is None

    def add_item(self, item):
        '''
        新增一个节点
            1、判断第一个比插入节点大的数
            2、当找到时，在新增的节点插入到他的前面
        :param item:
        :return:
        '''
        current = self.head
        # 记录当前元素的前一个元素 ，当新增的元素插入到last_current 后面
        last_current = None
        # 查到之后，标记为True, 将新增的元素添加到后面
        found = False
        while (current is not None) and (not found):
            if current.get_data() > item:
                found = True
            else:
                last_current = current
                current = current.get_next()
        node = LinkNode(item)
        # 当last_current为none时，说明插入的是元素最小的，可以直接进行插入
        if last_current is None:
            # 将新插入的数据接到新节点之后
            node.set_next(self.head)
            # 将head指向新节点
            self.head = node
        else:
            node.set_next(last_current.get_next())
            last_current.set_next(node)

    def search(self, item):
        '''
        查看元素时，当找到的
        :param item:
        :return:
        '''
        current = self.head
        # 查找时，如果节点当中的值大于当前值还没找到时，可以直接停止
        stop = False
        found = False
        while (current is not None) and (not found) and (not stop):
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_next()
        if found:
            return True
        else:
            return False

    def size(self):
        '''
        统计链表的长度
        '''
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count


if __name__ == '__main__':
    l = LinkListSort()
    l.add_item(22)
    l.add_item(33)
    l.add_item(44)
    print(l.is_empty())
    print(l.size())
    print(l.search(33))
