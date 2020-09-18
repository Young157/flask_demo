from sqlalchemy import or_

from . import login_blu
from flask import render_template, request, redirect, url_for, session, jsonify
from models import db
from models.user import User
import json


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


# 注册功能
@login_blu.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 用户提交注册信息
        user = request.form.get('user')
        email = request.form.get('email')
        password = request.form.get('password')
        verify = request.form.get('verify')
        # 判断逻辑
        if user and email and password and verify:
            in_user = db.session.query(User).filter(or_(User.user_name == user, User.email == email)).first()
            if not in_user:
                print('注册成功')
                new_user = User(user_id='', user_name=user, email=email, user_password=password)
                db.session.add(new_user)
                db.session.commit()
                ret = {
                    "status": 0,
                    "errmsg": "注册成功"
                }
                return jsonify(ret)
            else:
                print('用户已经注册过')
                ret = {
                    "status": 1,
                    "errmsg": "用户已经注册过"
                }
                return jsonify(ret)
        else:
            print('漏填信息')
            ret = {
                "status": 1,
                "errmsg": "漏填信息"
            }
            return jsonify(ret)
    else:
        # 请求注册页面
        return render_template('register.html')
