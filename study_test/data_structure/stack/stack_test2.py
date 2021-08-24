'''
中序表达式转后序表达式
'''
from study_test.data_structure.stack.stack_class import MyStack


def str_test1(str1):
    # 定义操作符优先级
    pre = {
        '(': 1,
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3,
    }
    # 定义空列表保存发转后的表达式
    after = []
    # 将表达式变为列表
    tokenList = str1.split()
    # 添加一个栈保存操作符
    stack = MyStack()
    for token in tokenList:
        # 如果token不是运算符，将token到列表当中
        if token in 'QWERTYUIOPLKJHGFDSAZXCVBNM' or token in '1234567890':
            after.append(token)
        # 当token是(，将(压入栈顶，直到遇到和他匹配的)才弹出
        elif token == '(':
            stack.push('(')
        # 当token是),从栈当中循环取值，直到遇到和他匹配的(
        elif token == ')':
            get_token = stack.pop()
            # 直到遇到和它匹配的值之前，把栈当中的所有运算符取出
            while get_token != '(':
                after.append(get_token)
                get_token = stack.pop()
        # 如果获取到的是运算符，将运算符压入栈顶，但压入之前要比较优先级，优先级大的或者等于的，要先取出
        else:
            # 判断栈是否为空，且栈顶元素优先级是否大于当前元素的优先级， 是，取出对应的元素
            while (not stack.is_empty()) and (pre[stack.look_first()] >= pre[token]):
                after.append(stack.pop())
            # 否 压入栈当中
            stack.push(token)
    # 最后把栈当中所有剩余的元素取出
    while not stack.is_empty():
        after.append(stack.pop())
    return ''.join(after)


def str_test2(str1):
    '''
    计算后序表达式
    :param str1:
    :return:
    '''
    #
    zx_r = str_test1(str1)
    # 定义一个栈
    stack = MyStack()
    for i in zx_r:
        # 判断i是否是数字，是数则压入栈中
        if i in '1234567789':
            stack.push(int(i))
        else:
            # 当遇到操作符时，从栈当中读取两个数据
            num1 = stack.pop()
            num2 = stack.pop()
            # 调用计算函数进行计算
            add_num = math_add(num1, num2, i)
            # 将计算得到的结果重新压入栈中，进行后续计算
            stack.push(add_num)
    return stack.pop()


def math_add(num1, num2, js):
    if js == '*':
        return num1 * num2
    # 当为除数时，要换位置
    elif js == '/':
        return num2 / num1
    elif js == '+':
        return num1 + num2
    else:
        return num1 - num1


if __name__ == '__main__':
    str2 = '( 1 / 4 ) + 3'
    print(str_test1(str2))
    print(str_test2(str2))
    print(1 / 4)
