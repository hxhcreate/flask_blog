from config import SERVER_PORT

from app import create_app
from app import db

app = create_app("develop")  # 生产环境
# app = create_app("product")  线上环境

from flask_script import Manager  # 追踪数据库的更新
from flask_migrate import Migrate, MigrateCommand  # 管理数据库需要的一些脚本

manager = Manager(app)  # 代理管理app
Migrate(app, db)  # 把app和db的信息绑定起来并且进行追踪
manager.add_command("db", MigrateCommand)  # 绑定额外的命令
"""
python manage.py runserver

python manage.py db init
python manage.py db migrate -m "message" 提交变更
python manage.py db upgrade 升级变更
python manage.py db downgrade 降级变更
"""

if __name__ == '__main__':
    # app.run(host="localhost", port=SERVER_PORT, debug=True)  已经代理了该app 直接使用manager来运行
    manager.run()
