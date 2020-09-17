from . import login_blu
from flask import render_template, request, redirect, url_for, session
from models import db
from models.user import User


# 用蓝图的路由装饰视图函数
@login_blu.route('/login', methods=['GET', 'POST'])
def login():
    # 如果是post请求就做登录逻辑处理
    if request.method == 'POST':
        # 获取用户输入的用户名密码
        name = request.form.get('Username')
        password = request.form.get('Password')
        # 查询数据库里的数据,判断用户名密码是否正确
        user = db.session.query(User).filter(User.user_name == name, User.user_password == password).first()
        if user:
            # 保存session
            session['user_id'] = user.user_id
            # 返回主页
            return render_template('profile.html', user=user)
        else:
            # 返回数据给页面
            return "登录失败"
    # 如果是get请求，就返回登录页面
    else:
        # 返回数据给页面
        return render_template('login.html')



