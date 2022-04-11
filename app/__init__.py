from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session
from config import config_map

db = SQLAlchemy()


def create_app(config_name):
    # config_name: 选择环境的参数
    app = Flask(__name__)

    config_class = config_map.get(config_name)
    app.config.from_object(config_class)  # 从一个类中直接获取配置参数

    db.init_app(app)  # 实例化数据库

    Session(app)  # 将app中的session数据全部读出来

    """注册蓝图"""
    from .api import user, admin
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(admin, url_prefix='/admin')
    return app
