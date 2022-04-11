from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(32))
    address = db.Column(db.String(64))


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    power = db.Column(db.Enum("admin", "superadmin"), nullable=False, default='admin')
    phone = db.Column(db.String(11))
    email = db.Column(db.String(32))
    address = db.Column(db.String(64))


try:
    db.create_all()  # 建立表格 如果已经存在 则不创建表 注意这里
except:
    pass
