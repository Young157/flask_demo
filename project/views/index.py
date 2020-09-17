from . import index_blu
from flask import render_template
from models import db
from models.user import User


# 用蓝图的路由装饰视图函数
@index_blu.route('/')
def index():
    # 查询数据库里的数据
    user = db.session.query(User).first()
    # 返回数据给页面
    return render_template('profile.html', user=user)
