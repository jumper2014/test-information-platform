# coding=utf-8
# author: dh
# common functions


import time
from app.main.jenkins_ut import *
from app.main.robot_parser import *
from app.main.test_link_parser import *
from app.main.zentao_parser import *


# threads variable
failed_build_dict = dict()
newly_bug = dict()
bug_status = dict()
ut_info = dict()
manual_case = list()
test_plan_progress = list()


def get_jenkins_build_failure_data():
    """
    thread to get jenkins data for the display
    :return:
    """
    while True:
        jenkins_handle = init_jenkins()
        global failed_build_dict
        failed_build_dict = get_failed_data_set(jenkins_handle)
        # print "failed_build_dict from threads:", failed_build_dict
        # release cpu
        time.sleep(10)


def get_test_link_case_info():
    """
    thread to get test_link data for the display
    :return:
    """
    while True:
        global manual_case
        global test_plan_progress
        manual_case = get_manual_case_info()
        test_plan_progress = test_progress()
        # release cpu
        time.sleep(60)


def get_zentao_bug_info():
    while True:
        global newly_bug
        global bug_status
        newly_bug = get_newly_bug_info()
        bug_status = get_all_bugs_status()
        # release cpu
        time.sleep(600)


def get_ut_info():
    while True:
        global ut_info
        ut_info = get_ut_num()
        # print "ut_info", ut_info
        # release cpu
        time.sleep(600)
