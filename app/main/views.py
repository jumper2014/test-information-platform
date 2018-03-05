# coding=utf-8
# author: zengyuetian
# add sqlalchemy function by dh

import json
import pickle


from flask import render_template, redirect, url_for, request, flash, jsonify
from lib import get_root_path, sort_by_status
from const import EVERY_PAGE_SIZE
from app.database.database import db, Machines, Features
import threads_function
from . import main

daily_case = {}


# 路由装饰器由蓝本提供
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/help')
def help():
    return render_template('help.html')


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@main.route('/bug_status')
def get_bugs_status():
    """

    :return:
    """
    # global bug_status
    # print "bug_status", threads_function.bug_status
    return render_template('bug_status.html', bug_status=threads_function.bug_status)


@main.route('/bug_info')
def get_bug_info():
    """

    :return:
    """
    # global newly_bug
    # print "newly_bug", threads_function.newly_bug
    sorted_bug_info = sorted(threads_function.newly_bug.iteritems(), key=lambda d: d[0], reverse=False)
    # print "sorted_bug_info", sorted_bug_info
    return render_template('bug_info.html', bug_info=sorted_bug_info)


@main.route('/regression_progress')
def get_test_progress():
    """
    test_plan_info: [{'name': 'FunctionTest', 'total': 356, 'non-exec': 20}, ...]
    :return:
    """
    # global test_plan_progress
    # print "test_plan_progress:{0}".format(threads_function.test_plan_progress)
    # test_data = [{'name': 'ab', 't': 3}, {'name': 'ggg', 't': 5}]
    # print "type:", type(test_data)
    return render_template('regression_progress.html', test_plan_progress=threads_function.test_plan_progress)


@main.route('/auto_rate')
def auto_rate():
    """

    :return:
    """
    auto_case_num = 0
    manual_case_num = 0
    case_distribution = {}

    global daily_case
    for key in daily_case:
        auto_case_num += daily_case[key]
    for category in threads_function.manual_case:
        manual_case_num += category['number']
    case_distribution['auto_case_num'] = auto_case_num
    case_distribution['manual_case_num'] = manual_case_num
    # print "auto_case_num", auto_case_num
    # print "manual_case_num", manual_case_num
    # if auto_case_num != 0:
    #     auto_case_rate = float(auto_case_num) / (auto_case_num + manual_case_num)
    # print "auto_case_rate:", auto_case_rate
    return render_template('auto_rate.html', case_distribution=case_distribution)


@main.route('/auto_test', methods=['GET', 'POST'])
def auto_test():
    """
    for example:
    dailycase: {u'platform_collect_sdk': 2, u'stats': 41, u'panel': 94}
    After sorting it will be a list.
    :return:
    """
    pkl_file = get_root_path() + "/app/data/auto_test.pkl"
    if request.method == 'POST':
        # save the value to file
        data = request.get_json()
        fil = open(pkl_file, "wb")
        pickle.dump(data, fil)
        fil.close()
        # print data
        return str(data)
    else:
        fil = open(pkl_file, "rb")
        data = pickle.load(fil)
        fil.close()
        global daily_case
        daily_case = json.loads(data)
        # print "dailycase:", daily_case
        sorted_daily_case = sorted(daily_case.iteritems(), key=lambda d: d[1], reverse=True)
        # print "sorted_daily_case:", sorted_daily_case
        return render_template("dailytest_case_info.html", daily_case=sorted_daily_case)


@main.route('/jenkins')
def get_jenkins_builds_status():
    """
    :return:
    """
    # global failed_build_dict
    # print "failed_build_dict from get_jenkins_builds_status:", threads_function.failed_build_dict
    json_data = json.dumps(threads_function.failed_build_dict)
    return json_data


@main.route('/unit_test')
def get_ut_data():
    """
    :return:
    """
    # global ut_info
    # print ut_info
    return render_template('unit_test.html', ut_info=threads_function.ut_info)


@main.route('/jenkins_builds')
def display_jenkins_failed_builds():
    """
    :return:
    """
    return render_template('json_data.html')


@main.route('/manual_test')
def display_test_link_cases():
    """
    test_link_case: [{'name': 'FunctionTest', 'number': 356}, {'name': 'PerformanceTest', 'number': 25}]
    :return:
    """
    # global manual_case
    # print "manual_case:", manual_case
    # print "type:", type(manual_case)
    return render_template('test_link_case_info.html', test_case=threads_function.manual_case)


@main.route('/feature_test_progress')
def features():
    """

    :return:
    """
    """
    data version style
    0: 未完成
    1: 进行中
    2: 已完成
    feature_tests = [
        {'name': 'HttpDns', 'id': '6', 'value': '21000000'},
        {'name': 'Opt_Report', 'id': '7', 'value': '22220000'},
        {'name': 'kafka-flume', 'id': '8', 'value': '00000000'}
    ]
    """
    # if request.method == "POST":
    #     forms = request.form
    #     # print forms.get()
    #     name_list = forms.to_dict().keys()
    #     print "features:POST", name_list[0]
    #f
    #     new_feature = Features(name_list[0])
    #     db.session.add(new_feature)
    #     db.session.commit()

    page = request.args.get('page')
    # print "page:", type(page), page

    if page is None:
        page = 1
    else:
        page = int(page)

    # 拿一页的数据
    slice_start = (page - 1) * EVERY_PAGE_SIZE
    slice_stop = page * EVERY_PAGE_SIZE

    feature_tests_info = Features.query.all()
    db.session.close()     # MUST to close session to make data not cached
    all_feature_tests = []

    for single_feature in feature_tests_info:
        tmp_feature_dict = dict()
        # print "single_feature", type(single_feature)
        tmp_feature_dict['id'] = str(single_feature.id)
        tmp_feature_dict['name'] = str(single_feature.feature_name)
        # print type(single_feature.id), type(single_feature.feature_name), type(single_feature.demand)
        tmp_feature_dict['value'] = \
            str(single_feature.demand) + str(single_feature.test_schema) + str(single_feature.review) \
            + str(single_feature.achieve) + str(single_feature.environment) + str(single_feature.execute) \
            + str(single_feature.report) + str(single_feature.archive) + str(single_feature.storing)

        all_feature_tests.append(tmp_feature_dict)

    # print "all_feature_tests:", all_feature_tests
    page_info = dict()
    page_info["total_page"] = (len(all_feature_tests) - 1) / EVERY_PAGE_SIZE + 1
    page_info["current_page"] = page

    sorted_feature_tests = sort_by_status(all_feature_tests)
    sorted_feature_tests = sorted_feature_tests[slice_start:slice_stop]
    # print "features: ", sorted_feature_tests
    # print "sorted_feature_tests:", sorted_feature_tests
    return render_template('feature_test_progress.html',
                           sorted_feature_tests=sorted_feature_tests,
                           page_info=page_info)


@main.route('/add-feature', methods=['GET', 'POST'])
def add_feature_test():
    """
    :return:
    """

    # forms = request.form
    # # print forms.get()
    # name_list = forms.to_dict().keys()
    # print name_list[0]
    # print type(request.form['featurename'])
    new_feature_name = str(request.form['featurename'])
    # print "new_feature_name", new_feature_name
    new_feature = Features(new_feature_name)
    #
    db.session.add(new_feature)
    db.session.commit()
    db.session.close()

    return redirect(url_for('main.features'))


@main.route('/remove-feature', methods=['GET', 'POST'])
def remove_feature_test():
    """
    :return:
    """
    if request.method == "POST":
        forms = request.form
        # print forms
        key_list = forms.to_dict().keys()
        feature_id = key_list[0]
        feature = Features.query.filter_by(id=feature_id).first()
        #  print "feature:", feature
        db.session.delete(feature)
        db.session.commit()
        db.session.close()

    return jsonify({'ok': True})


@main.route('/change-feature-name', methods=['GET', 'POST'])
def modify_feature_name():
    """
    :return:
    """
    if request.method == "POST":
        forms = request.form
        # print forms
        json_dict = forms.to_dict()
        feature_id = json_dict['feature_id']
        new_feature_name = json_dict['name']
        # print "modify feature_id:", feature_id
        # print "new_feature_name", new_feature_name
        feature = Features.query.filter_by(id=feature_id).first()
        # print "feature:", feature
        feature.feature_name = new_feature_name
        db.session.commit()
        db.session.close()

    return jsonify({'ok': True})


@main.route('/update-feature', methods=['GET', 'POST'])
def update_feature_status():
    """
    :return:
    """
    if request.method == "POST":
        forms = request.form
        # print forms
        json_dict = forms.to_dict()
        flow = json_dict['flow']
        feature_id = json_dict['feature_id']
        value = json_dict['value']

        feature = Features.query.filter_by(id=feature_id).first()
        # print "feature:", feature
        if flow == 'demand':
            feature.demand = value
        elif flow == 'test_schema':
            feature.test_schema = value
        elif flow == 'review':
            feature.review = value
        elif flow == 'achieve':
            feature.achieve = value
        elif flow == 'environment':
            feature.environment = value
        elif flow == 'execute':
            feature.execute = value
        elif flow == 'report':
            feature.report = value
        elif flow == 'archive':
            feature.archive = value
        elif flow == 'storing':
            feature.storing = value
        db.session.commit()
        db.session.close()

    return jsonify({'ok': True})


@main.route('/machines_info', methods=['GET', 'POST'])
def machines():
    """
    :return:
    """
    # print "machines_info"
    machines_info = Machines.query.all()
    return render_template('machines_info.html', machines_info=machines_info)


@main.route('/pc_info', methods=['GET', 'POST'])
def pcs():
    """
    :return:pc
    """
    # print "pc_info"
    machines_info = Machines.query.all()
    return render_template('pc_info.html', machines_info=machines_info)


@main.route('/add-machines', methods=['GET', 'POST'])
def add_machines():
    """
    :return:
    """
    form = request.form
    ip = form.get('IP')
    username = form.get('Username')
    passwd = form.get('Passwd')
    cpu = form.get('CPU')
    memory = form.get('Memory')

    if not ip:
        flash('IP不能为空!')
        return redirect(url_for('main.machines'))

    machine = Machines(ip, username, passwd, cpu, memory)

    db.session.add(machine)
    db.session.commit()
    db.session.close()

    return redirect(url_for('main.machines'))


@main.route('/delete-machines/<string:ip>')
def delete_machines(ip):
    """
    :return:
    """
    machine = Machines.query.get_or_404(ip)
    db.session.delete(machine)
    db.session.commit()
    db.session.close()
    return redirect(url_for('main.pcs'))


