from flask import Flask

# 创建flask对象,传入参数__name__
app = Flask(__name__)


# 使用路由装饰视图
@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    # 运行app，指定端口，和debug=True：表示当代码修改后框架自动重启
    app.run(port=9988, debug=True)
