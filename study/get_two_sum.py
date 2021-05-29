# 获取列表当中两个数之和等于目标数的下标

def sum_num(sum_list, target):
    j = -1
    for i in range(len(sum_list)):
        num2 = target - sum_list[i]
        if num2 in sum_list:
            if (sum_list.count(num2) == 1) and (num2 == sum_list[i]):
                continue
            else:
                j = sum_list.index(num2, i)
                break
    if j > 0:
        return [i, j]
    else:
        return []


def sum_num2(sum_list, target):
    '''
    优化1： 每次不找全部的数据，只找i之前 或者之后的数据，减少检索量
    :param sum_list:
    :param target:
    :return:
    '''
    for i in range(len(sum_list)):
        j = -1
        print(sum_list[i])
        num2 = target - sum_list[i]
        find_list = sum_list[:i]
        if num2 in find_list:
            j = find_list.index(num2)
            break
    if j > 0:
        return [i, j]
    else:
        return []


def sum_test3(sum_list, target):
    '''
    优化3：使用字典的方式进行查找，字典的查找效率高于列表
    :param sum_list:
    :param target:
    :return:
    '''
    my_dict = {}
    for i, n in enumerate(sum_list):
        my_dict[n] = i
    for ind, num in enumerate(sum_list):
        j = my_dict.get(target - num)
        if j is not None and ind != j:
            return [ind, j]


if __name__ == '__main__':
    print(sum_test3([1, 3, 5, 7, 9], 8))
