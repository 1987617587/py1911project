# author:lsh
# datetime:2020/4/18 10:20 
"""
                                 .::::.                                               _oo0oo_
                               .::::::::.                                            o8888888o
                              :::::::::::                                            88" . "88
                           ..:::::::::::'                                            (| -_- |)
                        '::::::::::::'                                               0\  =  /0
                          .::::::::::                                              ___/`---'\___
                     '::::::::::::::..                                           .' \\|     |# '.
                          ..::::::::::::.                                       / \\|||  :  |||# \
                        ``::::::::::::::::                                     / _||||| -:- |||||- \
                         ::::``:::::::::'        .:::.                        |   | \\\  -  #/ |   |
                        ::::'   ':::::'       .::::::::.                      | \_|  ''\---/''  |_/ |
                      .::::'      ::::     .:::::::'::::.                     \  .-\__  '-'  ___/-. /
                     .:::'       :::::  .:::::::::' ':::::.                 ___'. .'  /--.--\  `. .'___
                    .::'        :::::.:::::::::'      ':::::.            ."" '<  `.___\_<|>_/___.' >' "".
                   .::'         ::::::::::::::'         ``::::.         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               ...:::           ::::::::::::'              ``::.        \  \ `_.   \_ __\ /__ _/   .-` /  /
              ```` ':.          ':::::::::'                  ::::..      `-.____`.___ \_____/___.-`___.-'
                                 '.:::::'                    ':'````..                `=---='
                            女神保佑         永无BUG                            佛祖保佑         永无BUG
                                                                                                     
"""
import json

import requests

# url = 'http://user.kziot.net/system_users/UserKziot/lication/User_Core/App_Ashx/User_Control.ashx'
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
    'Cookie': 'Member_login=name=171886efa9b&openid=DC870BE4CD103FEA7D0AFBF9DF83A04A; ASP.NET_SessionId=sbtkg2xvna1kvrprvk2noug2',
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
