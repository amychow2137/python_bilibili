'''
1、已知目标
已知要获取什么数据,并知道数据在哪里(URL)
url--网络资源定位服务
涉及到网络架构的问题
2、构建思路
解析目标的数据结构,选择技术
3、爬取数据
编写代码，保存数据

html技术,<p>标签
打开XPath Helper--专门针对lxml去使用的
'''
#怎么去发送
#pip install requests（安装一个requests的模块）
import requests
#处理格式
#pip install lxml
from lxml import etree 
#发送给谁
url = "https://www.dldalu.cc/xiaoshuo/douluodalu/1.html"
#希望以浏览器的方式去访问，而不是代码的方式，代码的方式属于异常访问，可能拒绝访问
#如何才能瞒过呢？
#user-agent:（用户代理）
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

while True:
#伪装自己
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'    
    }
    #发送请求
    resp = requests.get(url,headers=headers)
    #设置编码
    resp.encoding = 'utf-8'
    #响应信息;.text是以字符串的方式打印
    #print(resp.text)
    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]
    url = f"https://www.dldalu.cc/{e.xpath('//td[2]/a/@href')[0]}"
    #print(title)
    #print(info)
    #保存
    with open("斗罗大陆.txt","a",encoding='utf-8') as f:
        f.write(title+r"\n\n"+info+r"\n\n")
    #resp2 = requests.get(next_url,headers=headers)
    if url == 'https://www.dldalu.cc/xiaoshuo/douluodalu/':
        break
    '''
    退出循环 break
    if url == "https://www.dldalu.cc/xiaoshuo/douluodalu/"
    '''
