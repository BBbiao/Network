
''' 
version: v 1.1
author : BBbiao
descripe: 实现对指定网页的联网操作，并对返回页面信息进行判定，是否成功
            cookie无需自己实现采集一次，使用现成的第三方包。
'''
import requests    #主要功能的包  post请求
import re   #正则，用来在整个网页信息里提取出自己想要的东西

session = requests.Session()
url = 'http://ngw.bupt.edu.cn/login' #登录网址

#cookies的前半部分，他的前面的一段是固定不变的，但是session部分是随时间变换的。所以cookies要用后面拼接而成
cookie = {
    'Hm_lvt_41e71a1bb3180ffdb5c83f253d23d0c0': '1540346356,1540346737,1540776370,1542023063',
}

#连接请求头，有些是可以被去掉的，我这里没有进行删除
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ngw.bupt.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ngw.bupt.edu.cn/index',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

#用户的数据
data = {
  'user': '20xxxxxxxx',
  'pass': 'xxxxxxxx',
  'line': ''   #连接线路 校园网
}
#先向网址发送一个GET请求，获取session值，然后拼接到Cookies里，得到一个完整的cookies
r = session.get(url)
cookies = cookie.copy()
cookies.update(session.cookies.get_dict())
#print(cookies)

s = session.post(url, headers=headers, cookies=cookies, data=data)  #发送post请求
page = requests.get(url)        #get返回页面进行
#正则方式取出判断字符 “登陆成功”，从而判断是佛建立连接 
re_extract = re.compile('<h3 class="center title">(.*)<\/h3>[\S\s].*<div class="notice-content">')
item_match = re.findall(re_extract, page.text)
if item_match[0] == '登录成功':
    exit(5)     #用作给bat脚本返回值，加以判断显示
else:
    exit(2)

