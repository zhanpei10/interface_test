'''
热土豆练习
'''
from study_test.data_structure.queue.queue_class import MyQueue


def photo_test(name_list, time):
    '''

    :param name_list:  名称列表
    :param time: 循环传递的的次数
    :return:
    '''
    # 获得队列对象
    queue = MyQueue()
    # 将姓名添加到队列当中
    for name in name_list:
        queue.enqueue(name)
    # 当队列当中只剩下一个人时，便是最后幸存的人
    while queue.size() > 1:
        # 循环传递， 最后一个从队列中剔除
        for i in range(7):
            # 队首第一个人出队，然后重新进入队列，直到最后获得土豆的人出队

            queue.enqueue(queue.dequeue())
        # 最后一个人出队
        name = queue.dequeue()
    return queue.dequeue()


if __name__ == '__main__':
    print(photo_test(['name1', 'name2', 'name3', 'name4', 'name5', 'name6'], 7))
