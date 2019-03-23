'''
获取python 100的URL
1. python100 url
2. 练习的url
'''
import requests
from bs4 import BeautifulSoup


url = 'http://www.runoob.com/python/python-100-examples.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
#发送请求
r = requests.get(url,headers=headers).content.decode('utf-8')
# print(r)
#解析html文档
soup = BeautifulSoup(r,'lxml')
# print(type(soup))

#查找每个练习的a链接的href属性获取对应的链接地址
re_a = soup.find(id='content').ul.find_all('a')  #返回的是100个a标签的列表
for i in re_a:
    print(i.attrs['href'])







