# coding=utf-8
# author: zengyuetian
# common lib for hera

import os
import inspect
import sys


def get_root_path():
    """
    获得自动测试框架根目录
    :return:
    """
    file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    main_path = os.path.dirname(file_path)
    app_path = os.path.dirname(main_path)
    root_path = os.path.dirname(app_path)
    return root_path


def sort_by_status(ori_list):
    """
    sort feature progress
    :param ori_list:
    :return:
    """
    for i in range(len(ori_list) - 1):
        for j in range(len(ori_list) - 1 - i):
            if compare_two_features(ori_list[j], ori_list[j + 1]):
                ori_list[j], ori_list[j + 1] = ori_list[j + 1], ori_list[j]

    return ori_list


def compare_two_features(feature_a, feature_b):
    """
    sort by value first, if value is same, sort by id.
    :param feature_a:
    :param feature_b:
    :return:
    """
    # ordered by complement
    # status_a = feature_a['value']
    # status_b = feature_b['value']

    # odered by id
    status_a = 0
    status_b = 0

    id_a = feature_a['id']
    id_b = feature_b['id']

    if status_a > status_b:
        return True
    elif status_a < status_b:
        return False
    elif status_a == status_b:
        if id_a < id_b:
            return True
        else:
            return False
