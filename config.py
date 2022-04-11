SERVER_PORT = 5000

BASE64_SALT = "test2022#%*"
MD5_SALT = "test2022#%*"

import redis

redis_store = redis.Redis(host='127.0.0.1', port=6379, db=1)  # 操作的redis配置


# ADMIN_USERNAME = "hxh"
# ADMIN_PASSWORD = "123456"
# ADMIN_AVATAR = "https://mnp-1300173558.cos.ap-shanghai.myqcloud.com/default/20200708202410.jpg"
# ADMIN_POWER = "超级管理员"
# ADMIN_PHONE = "18513360528"

# 基础环境
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secret"
    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理 加密混淆
    PERMANENT_SESSION_LIFETIME = 100  # session数据的有效期，单位秒


# 开发环境
class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskblog'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379, db=1)
    DEBUG = True


# 线上环境
class ProductionConfig(Config):
    """生产环境配置信息"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flaskblog'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379, db=1)


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}
