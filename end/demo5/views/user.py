from flask import Blueprint, request

# 新建用户模块蓝图
user_bp = Blueprint("user", __name__)


@user_bp.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return "进入注册页面"
    elif request.method == "POST":
        return "验证注册参数"


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return "进入登录页面"
    elif request.method == "POST":
        return "验证登录参数"
