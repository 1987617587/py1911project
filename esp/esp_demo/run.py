# author : liuShiHao
# Date : 2020/4/18 15:38
import time

from flask import Flask, request, render_template

# 创建实例
app = Flask(__name__)
# 开启调试模式，修改代码不需要重启
app.debug = True


def swith():
    import json
    import requests

    url = 'https://www.vip3070.com/App_Ashx/IOTDevice_NetControl.ashx'

    data = {
        'Executeway': 'switch_upstate',
        'ExecuteData': '585443315|IO02'
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Length': '54',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # NET_SessionId有时效性
        'Cookie': 'Member_login=name=171886efa9b&openid=DC870BE4CD103FEA7D0AFBF9DF83A04A; ASP.NET_SessionId=bmhcflt5ry0bt2lcu5rvqweu',
        'Host': 'www.vip3070.com',
        'Origin': 'https://www.vip3070.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.vip3070.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    response = requests.post(url, data=data, headers=headers)
    print(response)
    print(response.text)
    print("切换状态成功")


@app.route('/',methods=["GET", "POST"])
def hello_world():
    # return '<h1>Hello, World!</h1>'
    # 使用静态文件模板
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        status = request.form.get("status")
        sleeptime = request.form.get("sleeptime")
        waittime = request.form.get("waittime")

        print(status)
        print(sleeptime)
        if sleeptime:
            time.sleep(int(sleeptime))
            # 清楚输入框
            sleeptime = 0
        if waittime:
            print(waittime)
            now = time.strftime("%H:%M:%S", time.localtime(time.time()))
            print(now)  # 2013--10--10 23:40:00
            # 获取时间差，进行延迟等待，到达指定时间，进行状态切换
            while True:
                now = time.strftime("%H:%M:%S", time.localtime(time.time()))
                print(now)
                if now == waittime:
                    print(now,waittime)
                    swith()
                    print("切换状态")
                    # 清楚输入框
                    waittime = 0
                    return render_template('index.html')
                time.sleep(1)

        swith()
        print("切换状态")
        return render_template('index.html')


@app.route('/work', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # return "<h1>GET</h1>"
        # 使用静态文件模板 并传参
        return render_template('work.html', worklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username="zzy")

    elif request.method == "POST":
        return "<h1>POST</h1>"


if __name__ == "__main__":
    # http: // 127.0.0.1: 5000 / 是默认的IP和端口
    app.run()
    # 如果要自定义端口则需要使用
    # app.run(host="0.0.0.0", port=19011)