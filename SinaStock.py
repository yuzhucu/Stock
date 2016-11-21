# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

url='http://hq.sinajs.cn/list=sh601006'
res=requests.get(url)
#res.encoding='gbk'
text1=res.text
#print text1.decode('ascii').encode('gbk'),type(text1)
soup=BeautifulSoup(res.text,'html.parser')
a=soup.select('.hq_str_sh601006')
print a
print type( res.text.strip().strip("var hq_str_sh601006="))

#unicode1= res.text.strip().strip('var hq_str_sh601006=')
#utf8=unicode1.decode("utf-8")

stock= res.text.strip("").strip('var hq_str_sh601006=')
stock_str=re.split(',',stock)
print stock,len(stock_str)
for n in range(0,len(stock_str)):
     print stock_str[n]