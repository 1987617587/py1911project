# author:lsh
# datetime:2020/4/14 14:11 
'''
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
                                                                                                     
            '''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 4))
print(df)
# Dataframe 写入到 csv 文件
df.to_csv('./data/a.csv', sep=',', header=True, index=True)
# 第一个参数是说把 dataframe 写入到 D 盘下的 a.csv 文件中，参数 sep 表示字段之间用’,’分
# 隔，header 表示是否需要头部，index 表示是否需要行号。
# Dataframe 写入到 json 文件
df.to_json('./data/a.json')
# Dataframe 写入到 html 文件
df.to_html('./data/a.html')
# Dataframe 写入到剪贴板中
df.to_clipboard()
# Dataframe 写入到数据库中
# df.to_sql('tableName', con=dbcon, flavor='mysql')
# 第一个参数是要写入表的名字，第二参数是 sqlarchmy 的数据库链接对象，第三个参数表
# 示数据库的类型，“mysql”表示数据库的类型为 mysql。
