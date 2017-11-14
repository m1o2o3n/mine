# coding:utf-8
from urllib import request,parse
from bs4 import BeautifulSoup
import json
import time
import requests

def saveimg(url,n):
    try:
        print('正在下载第',str(n+1),'张图片')
        pic = requests.get(url,timeout=100)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
    string = 'picture\\'+ str(n) + '_' + '.jpg'
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()



url = 'https://baike.baidu.com/item/%E6%BC%AB%E7%94%BB/178351?fr=aladdin'
req = request.urlopen(url)
content = req.read().decode('utf-8')
##获取完毕

soup = BeautifulSoup(content,'html5lib')
results = soup.find_all('img')

i = 2 
for result in results:
    saveimg(result.attrs['src'],i)
    print("url是---->",result.attrs['src'])
    i+=1
## 网络容易有问题，记得添加提醒


#————————————————————————————————————————————————————————————————————————#
# soup = BeautifulSoup(content)
# results = soup.find_all(class_='yiyi-st')
# for result in results :
#     print('内容是',result.attrs['id'],'标签内部的文字是',result.contents)
#     for dd in result.strings:
#         print('string显示内容',dd)
    ##可以使用soup.h1.p 这种叠加方式，估计find方法也有
    ##result.name soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称
    ##result.attrs 是显示标签属性，用json显示
    ##result.contents 是显示标签内的内容使用,contents是一个数组
    ##result.strings 是显示标签内内容使用，与contents的区别在于，只显示括号的文字
    ##上面几项没有值返回none
    ## 参考 http://cuiqingcai.com/1319.html
 

