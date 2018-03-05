# coding=utf-8
# author: zengyuetian
# Flask 用 蓝图（blueprints） 的概念来在一个应用中或跨应用制作应用组件和支持通用的模式。

from flask import Blueprint

main = Blueprint('main', __name__)

# 放在末尾是为了避免循环导入依赖
from . import views, errors