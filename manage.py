# coding=utf-8
# author: Zeng YueTian
# manage script of hera system
# how to use it: nohup python manage.py runserver --host 0.0.0.0 >/dev/null 2>&1 &
# please see run.sh

import os
import threading
from flask import Flask, render_template
from flask_script import Manager
from flask_script import Shell
from app import create_app, db
from app.main.views import *
from app.main.threads_function import *


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# 使用命令行选项来控制启动参数
manager = Manager(app)


def make_shell_context():
    """
    回调函数，在shell命令中自动执行某些操作(注册程序，数据库实例以及模型)
    :return:
    """
    return dict(app=app)

# 注册一个make_shell_context回调函数
manager.add_command("shell", Shell(make_context=make_shell_context))

app = Flask(__name__)

if __name__ == '__main__':
    # define some working threads
    threads = []

    # get jenkins build failure data
    t_build_failure = threading.Thread(target=get_jenkins_build_failure_data)
    threads.append(t_build_failure)

    t_testlink_info = threading.Thread(target=get_test_link_case_info)
    threads.append(t_testlink_info)

    t_zentao_info = threading.Thread(target=get_zentao_bug_info)
    threads.append(t_zentao_info)

    t_jenkins_info = threading.Thread(target=get_ut_info)
    threads.append(t_jenkins_info)

    # now we get threads as [t_build_failure, t_testlink_info, t_zentao_info, t_jenkins_info]
    for t in threads:
        t.setDaemon(True)
        t.start()
        if t == threads[-2]:
            time.sleep(10)
    manager.run()

