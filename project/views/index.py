from . import index_blu
from flask import render_template, request, session, url_for, redirect
from models import db
from models.user import User


# 用蓝图的路由装饰视图函数
@index_blu.route('/')
def index():
    # 获取session数据
    user_id = session.get('user_id')
    # 判断用户是否已经登录
    if not user_id:
        # 没有登录就返回登录页面
        return redirect(url_for('login.login'))
    else:
        # 登录了就根据session里的user_id查询用户数据，返回用户主页
        user = db.session.query(User).filter(User.user_id == user_id).first()
        return render_template('profile.html', user=user)


# 登出功能
@index_blu.route('/logout')
def logout():
    # 清除session
    session.clear()
    # 跳转到登录页面
    return redirect(url_for('login.login'))


