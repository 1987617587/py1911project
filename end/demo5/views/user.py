from flask import Blueprint, request
from flask import render_template, request, flash
from werkzeug.utils import redirect

# 新建用户模块蓝图
user_bp = Blueprint("user", __name__)


@user_bp.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        # return "请先登录"
        return render_template('regist.html')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = None
        if not username:
            error = "用户名必填"
        elif not password:
            error = "密码必填"
        elif not password2:
            error = "重复密码必填"
        elif password != password2:
            error = "密码不一致"
        if error:
            flash(error, category=error)
            return redirect('/regist')
        return redirect('/')


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        flash({

        })
        # return "请先登录"
        return render_template('login.html')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        error = None
        if not username:
            error = "用户名必填"
        elif not password:
            error = "密码必填"
        elif username != "admin" or password != "123456":
            error = "用户名或密码错误"
        # 需要在本次请求中将信息写入session （前提必须配置secret_key）
        # flash("提示内容")
        # 下次请求中取获取、并且从session移除
        # get_flashed_messages()
        if error:
            # flash(error, category=error)
            flash({
                "error": error,
                "username": username,
                "password": password,
            })
            return redirect('/login')
        # return render_template('booklist.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username=username)
        return redirect('/')
