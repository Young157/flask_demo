from . import db


class User(db.Model):
    # 对应MySQL表里的名字
    __tablename__ = 'user'

    # 创建字段
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    head_img = db.Column(db.String(200))
    short_description = db.Column(db.String(300))
    email = db.Column(db.String(50), nullable=False)
