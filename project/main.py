from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from views import index_blu
from models import db

# 创建app
app = Flask(__name__)
# 注册蓝图
app.register_blueprint(index_blu)
# 对app进行初始化
db.init_app(app)
# 对app进行配置
app.config.from_pyfile("config.ini")

# 添加数据库迁移工具
# 创建要管理的对象，应用的启动交给了flask_script
manager = Manager(app)
# 生成migrate对象 用来数据库迁移
migrate = Migrate(app, db)
# 添加db命令
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    # app.run(port=8899)
    manager.run()  # 使用manager的run
