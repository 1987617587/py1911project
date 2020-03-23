"""
案例：双色球爬虫：
http://zst.aicai.com/ssq/openInfo/
爬取期号，日期，红色球，蓝色球，总投注额数，一等奖注数，一等奖奖金，二等奖注数：，二等奖奖金，奖池滚存（元）
保存为ssq.txt文件
"""
import requests
from lxml import etree

# 最基本的反反爬
# 设置请求头User_Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
url = 'http://zst.aicai.com/ssq/openInfo/'
response = requests.get(url, headers=headers)
html = response.content.decode(response.apparent_encoding)
# print(html)
# 提取数据
html = etree.HTML(html)

#
print("表头")

ls = html.xpath("//table[@class='fzTab nbt']/tbody/tr/th")
print('len', len(ls))
for item in ls:
    title = item.xpath('.//text()')[0]
    print('title', title)

print("表中数据")
ls = html.xpath("//table[@class='fzTab nbt']/tbody/tr/td")
print('len', len(ls))
i = 0
for item in ls:
    i += 1
    title = item.xpath('.//text()')[0]
    if i % 15 == 1:
        print('期号:', title)
        this_num = title
    elif i % 15 == 2:
        print(f"期号{this_num}开奖时间:", title)
    elif i % 15 == 3:
        print(f"期号{this_num}红球1:", title)
    elif i % 15 == 4:
        print(f"期号{this_num}红球2:", title)
    elif i % 15 == 5:
        print(f"期号{this_num}红球3:", title)
    elif i % 15 == 6:
        print(f"期号{this_num}红球4:", title)
    elif i % 15 == 7:
        print(f"期号{this_num}红球5:", title)
    elif i % 15 == 8:
        print(f"期号{this_num}红球6:", title)
    elif i % 15 == 9:
        print(f"期号{this_num}篮球:", title)
    elif i % 15 == 10:
        print("期号{this_num}总投注额:", title)
    elif i % 15 == 11:
        print(f"期号{this_num}一等奖注数:", title)
    elif i % 15 == 12:
        print(f"期号{this_num}一等奖奖金:", title)
    elif i % 15 == 13:
        print(f"期号{this_num}二等奖注数:", title)
    elif i % 15 == 14:
        print(f"期号{this_num}二等奖奖金:", title)
    else:
        print(f"期号{this_num}奖池滚存:", title)
