# 进制之间的相互转换
from study_test.data_structure.stack.stack_class import MyStack


def bin_dec(num):
    '''
    十进制转换为二进制
    :param num:
    :return:
    '''
    stack = MyStack()
    while num > 0:
        stack.push(num % 2)
        num = num // 2
    bin_str = ''
    while not stack.is_empty():
        bin_str = bin_str + str(stack.pop())
    return bin_str


def bin_test1(num, seq):
    '''
    多进制之间的转换
    :param num:
    :param seq:
    :return:
    '''
    str1 = '0123456789ABCDE'
    stack = MyStack()
    while num > 0:
        i = num % seq
        stack.push(str1[i])
        num = num // seq
    str2 = ''
    while not stack.is_empty():
        str2 = str2 + str(stack.pop())
    return str2


if __name__ == '__main__':
    print(bin_test1(1234, 16))
