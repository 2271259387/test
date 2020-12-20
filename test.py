from operator import and_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://root:root@localhost/python_db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app, use_native_unicode='utf8')


class User(db.Model):
    __tablename__ = 'user_list'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return '<User 用户名：%r 密码：%r>' % (self.username, self.password)


def add_object(user):  # 增加
    db.session.add(user)
    db.session.commit()
    print("添加 {0} 完成".format(user.username))


def delete_object(user):  # 删除
    result = user.query.filter(user.username == '11111').all()
    db.session.delete(result)
    db.sesstion.commit()


def updata_object(username):  # 修改
    result = user.query.fillter(username == '111111').all()
    result.title = 'success2018'
    db.session.commit()


def query_object(user, query_condition_u, query_condition_p):  # 查询
    result = user.query.filter(and_(user.username == query_condition_u, user.password == query_condition_p))
    print("查询%r完成" % user.__repr__())


# Here is a Demo
user = User()
user.username = input("请输入用户名:")
user.password = input("请输入密码：")
add_object(user)
query_object(user, user.username, user.password)
