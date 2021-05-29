import copy


def cmp(test_data, old_data, path="", path_list=None):
    """
    对比引擎
    :param test_data:
    :param old_data:
    :param path:
    :param path_list:
    :return:
    """
    if isinstance(test_data, dict):
        for key in old_data:
            if key not in test_data:
            """深度复制，防止原始数据被篡改"""
            path1 = copy.deepcopy(path)
            path1 = path1 + "." + key
    """少于原始数据，路径保存"""
    path_list["less"].append(path1)
    for key in test_data:
        path1 = copy.deepcopy(path)
    path1 = path1 + "." + key
    if key in old_data:
        if test_data[key] == old_data[key]:
            pass
    else:
        cmp(test_data[key], old_data[key], path=path1, path_
    list = path_list)
    else:
    """多于原始数据,路径保存"""
    path_list["more"].append(path1)
    elif isinstance(test_data, (list, tuple)):
    if len(test_data) != len(old_data):
        print("list len: '{}' != '{}'".format(len(test_data), len(old_data)))
    if len(test_data) > len(old_data):
        for j in range(0, len(test_data)):
            if str(test_data[j]) not in [str(i) for i in old_data]:
            path1 = copy.deepcopy(path)
    path1 = path1 + "[{}]".format(j)
    path_list["more"].append(path1)
    elif len(test_data) < len(old_data):
    for j in range(0, len(old_data)):
        if str(old_data[j]) not in [str(i) for i in test_data]:
            path1 = copy.deepcopy(path)
    path1 = path1 + "[{}]".format(j)
    path_list["less"].append(path1)
    else:
    list2 = list(zip(test_data, old_data))
    for i in range(0, len(list2)):
        path1 = copy.deepcopy(path)
    path1 = path1 + "[{}]".format(i)
    cmp(list2[i][0], list2[i][1], path1, path_list)
    else:
    if test_data != old_data:
        """字段value值不同，路径保存"""
    path_list["difference"].append(path)

    def filter_by_url(test_url, old_url):

    """
    URL 校验接口
    :param test_url:
    :param old_url:
    :return:
    """
    return True if test_url == old_url else False

    """
    Body 校验接口
    :param test_body:
    :param old_body:
    :return:
    """
    return True if test_body == old_body else False

    def filter_by_env(test_env, old_env):

    """
    ENV 校验接口
    :param test_env:
    :param old_env:
    :return:
    """
    return True if test_env == old_env else False
