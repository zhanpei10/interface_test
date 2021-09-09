'''
递归练习
  知识点：
    python当中递归调用的默认最大次数是1000
        递归调用栈会占用一定的内存空间来对栈帧进行保存
        可对递归调用的次数进行设置
        import sys
        sys.setrecursionlimit()
'''
import sys


def list_sum(sumList):
    if len(sumList) == 1:
        return sumList[0]
    return sumList[0] + list_sum(sumList[1:])


def to_str(number, base):
    '''
    使用递归进行 任意进制的转换
    :param number:  需要转换的数据
    :param base: 对下的进制
    :return:
    '''
    # 设置对应的进制数字
    str_jz = '0123456789ABCDE'
    # 递归结束条件，如果要转换的数据小于要转换的进制，直接返回对应的位置
    if number < base:
        return str_jz[number]
    else:
        # 拆分问题规模 将问题规模拆分为余数 + 整除之后的值 对整除之后的数值进行重复拆分， 余数直接获取对应的位置
        return to_str(number//base, base) + str_jz[number % base]


if __name__ == '__main__':
    # print(sys.getrecursionlimit())
    # print(list_sum([1, 3, 4, 5]))
    print(to_str(29, 2))
