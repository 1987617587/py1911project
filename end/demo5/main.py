from factory import creat_app
from models import db

if __name__ == '__main__':
    # http: // 127.0.0.1: 5000 / 是默认的IP和端口
    app = creat_app()
    # 首次创建数据库
    # db.drop_all()
    # db.create_all()

    app.run()
    # 如果要自定义端口则需要使用
    # app.run(host="0.0.0.0", port=19011)
