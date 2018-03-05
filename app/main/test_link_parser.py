# coding=utf-8
# author: zengyuetian
# get test case and plan info from test link

from testlink import *
url = 'http://sub.site.com/lib/api/xmlrpc/v1/xmlrpc.php'  # ip地址为安装的testlink ip
key = 'a16641a2cea5d780ae685beea32dcef1'  # API key


def get_manual_case_info():
    """
    get test suite and case number
    :return: test_case_info
    """
    test_case_info = []
    test_link_obj = TestlinkAPIClient(url, key)
    # get all test suites and their case number
    projects = test_link_obj.getProjects()
    # print projects
    animbus = projects[0]
    top_suites = test_link_obj.getFirstLevelTestSuitesForTestProject(animbus['id'])
    # print top_suites
    # suite = top_suites[0]
    for suite in top_suites:
        # print suite['id'], suite['name']
        test_case_dict = {}
        test_cases = test_link_obj.getTestCasesForTestSuite(suite['id'], 10, "")
        test_case_dict['name'] = suite['name']
        test_case_dict['number'] = len(test_cases)
        test_case_info.append(test_case_dict)
        # print len(test_cases)

    # print "test_case_info:", test_case_info
    return test_case_info


def test_progress():
    """
    test_plan_info: [{'name': 'ios_3.9发布测试 RC2', 'total': 356, 'non_exec': 20}, ...]
    :return:
    """
    test_progress_info = []
    test_link_obj = TestlinkAPIClient(url, key)
    # get all test suites and their case number
    projects = test_link_obj.getProjects()
    # print projects
    animbus = projects[0]
    test_plans = test_link_obj.getProjectTestPlans(animbus['id'])
    for test_plan in test_plans:
        if test_plan['active'] == '1':
            try:
                test_plan_result = test_link_obj.getTotalsForTestPlan(test_plan['id'])
                # print test_plan_result
            except Exception:
                continue
            test_progress_info.append(process_plan_result(test_plan['name'], test_plan_result))
            # print "Plan:{0}, cases:{1}".format(test_plan, test_cases_result)

    return test_progress_info


def process_plan_result(plan_name, plan_result_dict):
    """

    :param plan_result_dict:
    :param plan_name:
    A data structure example:
    {
    'with_tester': 	{
        '6': {
            'p': {'platform_id': 6, 'status': 'p', 'exec_qty': 0},
            'f': {'platform_id': 6, 'status': 'f', 'exec_qty': 0},
            'b': {'platform_id': 6, 'status': 'b', 'exec_qty': 0},
            'n': {'platform_id': '6', 'status': 'n', 'exec_qty': '43'}}},
    'total': {
        '6': {'platform_id': '6', 'qty': '43'}},
    'platforms': ''}
    and may like:
    {
    'with_tester': [{
        'p': {'platform_id': '0', 'status': 'p', 'exec_qty': '6'},
        'f': {'platform_id': 0, 'status': 'f', 'exec_qty': 0},
        'b': {'platform_id': 0, 'status': 'b', 'exec_qty': 0},
        'n': {'platform_id': '0', 'status': 'n', 'exec_qty': '110'}}],
    'total': [{'platform_id': '0', 'qty': '116'}],
    'platforms': ''}
    :return:
    """
    # print plan_result_dict
    key_list = ['with_tester', 'total', 'platforms']
    total_case_number = 0
    non_exec_number = 0
    plan_progress = {}

    # print plan_result_dict
    for test_platform in plan_result_dict[key_list[0]]:
        if isinstance(test_platform, dict):
            non_exec_number += int(test_platform['n']['exec_qty'])
        elif isinstance(test_platform, str):
            non_exec_number += int(plan_result_dict[key_list[0]][test_platform]['n']['exec_qty'])

    # print "non_exec_number:", non_exec_number

    for test_platform in plan_result_dict[key_list[1]]:
        if isinstance(test_platform, dict):
            total_case_number += int(test_platform['qty'])
        elif isinstance(test_platform, str):
            total_case_number += int(plan_result_dict[key_list[1]][test_platform]['qty'])
        pass

    # print "total_case_number:", total_case_number
    plan_progress['name'] = plan_name
    plan_progress['total'] = total_case_number
    plan_progress['non_exec'] = non_exec_number

    return plan_progress

if __name__ == "__main__":
    print test_progress()
    # tlc = TestlinkAPIClient(url, key)  # initialize TestlinkAPIClient object named tlc
    # # 下面这些是获得制定test plan的case和每个case的进度
    # tp = tlc.getTestPlanByName("Test Case", "ios_3.9 发布测试计划")
    # print "tp:", tp
    #
    # totals = tlc.getTotalsForTestPlan(3026)
    # print totals
    #
    # tcs = tlc.getTestCasesForTestPlan(3026)
    # print tcs
    # print len(tcs)

