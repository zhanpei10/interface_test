'''
回文词判定
 概念：顺着读和倒着读都一致
'''
from study_test.data_structure.deque.deque_class import MyDeque


def deque_test(value):
    '''
    回文词练习
    :param value:
    :return:
    '''
    deque = MyDeque()
    # 将数据加入的队列当中
    for i in value:
        deque.add_front(i)
    # 是不是回文词标识
    is_a = True
    # 循环从两端读取字符，判断是否相等，存在不相等，则不是，直到队列长度大于1
    while (deque.size() > 1) and is_a:
        front = deque.remove_front()
        rear = deque.remove_rear()
        if front != rear:
            is_a = False
    return is_a


if __name__ == '__main__':
    print(deque_test('12d3211'))
