#!/usr/bin/env python
# coding: utf-8

# In[27]:


#安裝兩個套件
get_ipython().system('pip install requests')
get_ipython().system('pip install beautifulsoup4')

#輸入requests
import requests
from bs4 import BeautifulSoup 

#將想要抓的網頁抓下來
r = requests.get("https://oursogo.com/forum.php?mod=viewthread&tid=2119507&page=1&authorid=616477l")

#繁體中文編碼因此改設定成big-5
r.encoding="Big-5"

#印出HTML
print(r.text) 

#將網頁資料以html.parser以檢閱html標頭
soup = BeautifulSoup(r.text,"html.parser") 
print(soup.prettify())
print(soup) #檢查用而已


#發現所有內文在標頭'td.t_f'底下
sel = soup.select('td.t_f') 
print(sel)

#取得文字、去除左右的空格
for j in sel:
     f=j.get_text().strip() 
print(f)

#存成可檢閱檔案
print(f, file=open('HWWWWW.txt', 'w'))