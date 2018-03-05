# coding=utf-8
# author: zengyuetian
# 使用工厂函数延迟创建程序实例

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    """
    工厂函数
    :param config_name: 配置名
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 在扩展对象上完成初始化过程
    config[config_name].init_app(app)
    db.init_app(app)

    # 附加路由和自定义的错误页面

    # 使用蓝图（蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正成为程序的一部分
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

