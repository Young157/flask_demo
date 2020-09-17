from flask import Blueprint
# 创建蓝图对象，传入视图文件名
index_blu = Blueprint('index', __name__)

from . import index
