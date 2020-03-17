"""
flask:应用工厂，负责应用相关所有的内容

"""
import sqlite3

from flask import render_template, request, flash
from werkzeug.utils import redirect

# 引入模块
from flask import Flask

# from views.book import books_bp
# from views.other import get404_bp
# from views.user import user_bp
from views import *


def creat_app():
    # 实例化WSGI应用
    app = Flask(__name__)
    # 开启调试模式，修改代码不需要重启
    app.debug = True
    # 必须配置secret_key
    app.secret_key = "3\x83\xea\xeeeB?\xa9\x03Q\x83+\xa8\x11\x1bZ2iS\xe2?Q\xca"

    # 404针对整个项目，不能加入蓝图
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

    @app.template_filter(name="myupper")
    def myupper(value):
        return value.upper()

    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(get404_bp)

    # @app.before_first_request
    # def first_request_do_something():
    #     print("这是第一次请求，创建数据库")
    #     try:
    #         con = sqlite3.connect("demo5.db")
    #         cur = con.cursor()
    #         cur.execute("DROP TABLE IF EXISTS user;")
    #         cur.execute(
    #             "CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT,"
    #             "username TEXT UNIQUE NOT NULL,password TEXT NOT NULL,"
    #             "created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, "
    #             "is_admin INTEGER DEFAULT 0, is_active INTEGER DEFAULT 1 )")
    #         con.commit()
    #         cur.close()
    #         con.close()
    #     except:
    #         print("出错了")
    #
    #     return "这是第一次请求"

    return app
