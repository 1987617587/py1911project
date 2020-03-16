# 引入模块
from flask import Flask
# 引入蓝图所在
from views.user import *

# 实例化WSGI应用
app = Flask(__name__)
# 注册蓝图
app.register_blueprint(user_bp)
if __name__ == '__main__':
    app.run()
