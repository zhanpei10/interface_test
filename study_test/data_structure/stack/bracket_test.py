'''
栈之括号的使用
'''
from study_test.data_structure.stack.stack_class import MyStack


def bracket_test1(bracket):
    '''
    匹配单括号
    :return:
    '''
    stack = MyStack()
    index = 0
    Balance = True
    while index < len(bracket) and True:
        if bracket[index] == '(':
            stack.push(bracket[index])
        else:
            stack.pop()
        index = index + 1
    if stack.is_empty():
        return Balance
    else:
        return False


def bracket_test2(bracket):
    '''
    匹配多种类型的括号
    :return: 
    '''
    stack = MyStack()
    index = 0
    balance = True
    while index < len(bracket) and balance:
        r_stack = bracket[index]
        if r_stack in '([{':
            stack.push(r_stack)
        else:
            c_stack = stack.pop()
            if not compare(c_stack, r_stack):
                balance = False
        index = index + 1
    if stack.is_empty():
        return True
    else:
        return False


def compare(start, end):
    '''
    判断符号是不是成对出现，不是，则不是规则的
    :param start:
    :param end:
    :return:
    '''
    t1 = '([{'
    t2 = ')]}'
    return t1.index(start) == t2.index(end)


if __name__ == '__main__':
    print(bracket_test2('(((({(})))))'))
