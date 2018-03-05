# just for function test !!!!

from manage import app
from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy.orm as orm

MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_UE_USER = "root"
MYSQL_PASSWORD = "rootPass"
MYSQL_DB = "hera"

# dialect+driver://username:password@host:port/database?charset=utf8
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{0}:{1}@{2}:{3}/{4}".format(MYSQL_UE_USER, MYSQL_PASSWORD,
                                                                             MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
db = SQLAlchemy(app)
# engine = get_engine(app)
# DBSession = orm.sessionmaker(bind=engine)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    passwd = db.Column(db.String(30))

    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def __repr__(self):
        return '<User %r>' % self.name


class Machines_info(db.Model):
    ip = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(60))
    passwd = db.Column(db.String(30))
    cpu = db.Column(db.Integer)
    memory = db.Column(db.Integer)

    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def __repr__(self):
        return '%s,%s,%s,%d,%d' % (self.ip, self.username, self.passwd, self.cpu, self.memory)


def get_machines_list():
    """
    body_data = [
            {"ip": "192.168.1.153", "username": "root", "passwd": "rootPass", "cpu": 8, "memory": 16},
            {"ip": "192.168.1.154", "username": "root", "passwd": "rootPass", "cpu": 8, "memory": 16}
        ]
    return body_data
    """
    body_data = []
    machines_list = Machines_info.query.all()
    print machines_list
    for single_pc in machines_list:
        tmp_dict = dict()
        tmp_dict["ip"] = single_pc.ip
        tmp_dict["username"] = single_pc.username
        tmp_dict["passwd"] = single_pc.passwd
        tmp_dict["cpu"] = single_pc.cpu
        tmp_dict["memory"] = single_pc.memory
        body_data.append(tmp_dict)

    return body_data


def delete_machines_info(ip):
    """

    :param ip:
    :return:
    """
    delete_obj = Machines_info.query.filter_by(ip=ip).first()
    db.session.delete(delete_obj)
    db.session.commit()
    db.session.close()


if __name__ == "__main__":
    users = User.query.all()
    print users
