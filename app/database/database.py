# coding=utf-8
# feature test db lib
from flask_sqlalchemy import SQLAlchemy
from manage import app

MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "rootPass"
MYSQL_DB = "hera"

# dialect+driver://username:password@host:port/database?charset=utf8
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{0}:{1}@{2}:{3}/{4}".format(MYSQL_USER, MYSQL_PASSWORD,
                                                                             MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True   # 每次請求結束后都會自動提交數據庫中的變動

db = SQLAlchemy(app)     # db表示正在使用的數據庫


# 用於跟蹤測試進度的表
# 用來增刪改查該表
class Features(db.Model):
    __tablename__ = 'feature_test_progress'

    id = db.Column(db.Integer, primary_key=True)    # 自增id
    feature_name = db.Column(db.String(60))         # 任務名   task_name
    demand = db.Column(db.String(1))                # 需求    requirement
    test_schema = db.Column(db.String(1))           # 方案    concept
    review = db.Column(db.String(1))                # 评审    review
    achieve = db.Column(db.String(1))               # 实现    implement
    environment = db.Column(db.String(1))           # 环境    environment
    execute = db.Column(db.String(1))               # 执行    execute
    report = db.Column(db.String(1))                # 报告    report
    archive = db.Column(db.String(1))               # 归档    archive
    storing = db.Column(db.String(1))               # 入库    check-in

    def __init__(self, feature_name, demand="0", test_schema="0", review="0", achieve="0", environment="0",
                 execute="0", report="0", archive="0", storing="0"):
        self.feature_name = feature_name
        self.demand = demand
        self.test_schema = test_schema
        self.review = review
        self.achieve = achieve
        self.environment = environment
        self.execute = execute
        self.report = report
        self.archive = archive
        self.storing = storing

    def __repr__(self):
        return '{0} {1} {2}{3}{4}{5}{6}{7}{8}{9}{10}'.format(self.id, self.feature_name, self.demand, self.test_schema,
                                                             self.review, self.achieve, self.environment,
                                                             self.execute, self.report, self.archive,
                                                             self.storing)


class Machines(db.Model):
    __tablename__ = 'machines_info'
    ip = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(60))
    passwd = db.Column(db.String(30))
    cpu = db.Column(db.Integer)
    memory = db.Column(db.Integer)

    def __init__(self, ip, username, passwd, cpu, memory):
        self.ip = ip
        self.username = username
        self.passwd = passwd
        self.cpu = cpu
        self.memory = memory

    def __repr__(self):
        return '<Machine {0} {1} {2} {3} {4}>'.format(self.ip, self.username, self.passwd, self.cpu, self.memory)


if __name__ == "__main__":
    feature_tests_info = Features.query.all()
    print "1", feature_tests_info

    feature = Features.query.get_or_404('Httpdns')
    print "2", feature
