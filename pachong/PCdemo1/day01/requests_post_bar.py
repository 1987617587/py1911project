# 案例：贴吧爬虫
# https://tieba.baidu.com
# 需求：制作爬虫爬取指定贴吧一定页码范围的的信息
# 输入：起始页码，结束页码，贴吧名称
# 提取帖子回复量，标题，链接，作者，保存到tieba.csv文件


import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
# 带参查询
# https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=300
url = "https://tieba.baidu.com/f?"
try:
    pn = input("请输入页数：")
    # 根据浏览器反馈操作
    pn = (int(pn)-1)*50
    params = {
        "kw": "python",
        "ie": "utf-8",
        "pn": pn
    }
    response = requests.get(url, params=params, headers=headers)

    html = response.content
    with open('post_bar.html', 'wb') as file:
        file.write(response.content)

    print(html)
    # 提取数据
    html = etree.HTML(html)
    print(html)

    print("+++")
    # 分析结果，编写xpath匹配表达式
    # //ul[@class='mi_ul']/span/a

    # ls = html.xpath("//li[contains(@class ,'j_thread_list clearfix')]")
    ls = html.xpath("//div[@class='t_con cleafix']/a")

    print('len', len(ls))
    # for item in ls:
    #     title = item.xpath('.//text()')[0]
    #     print('title', title)
    #     detail_url = item.xpath('./@href')[0]
    #     print('detail_url', detail_url)

except:
    print("未找到相应数据")