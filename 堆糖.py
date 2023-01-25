import random
import time
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
import requests
from lxml import etree
option = ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument("user-data-dir=D:\programer\chromedriver_win32")
#option.add_argument("headless")

s=Service("D:\programer\chromedriver_win32\chromedriver.exe")
srclst=[]


def get_blog_id(start_page,end_page,kw):
    blog_id = []
    bro = webdriver.Chrome(options=option, service=s)
    for i in range(start_page,end_page+1):
        bro.get(f'https://www.duitang.com/search/?kw={kw}&type=feed')
        print(f'正在爬取第{i}页')
        bro.get(f'https://www.duitang.com/search/?kw={kw}&type=feed#!s-p{i}')
        for _ in range(15):
            time.sleep(random.uniform(0.8,1))
            bro.execute_script("window.scrollTo(0,100000)")
        tree=etree.HTML(bro.page_source)
        blog_id+=tree.xpath('//a[@class="a"]/@href')
        time.sleep(3)
    bro.close()
    return blog_id
header={'user-agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'referer':'https://www.duitang.com/search/?kw=%E9%AC%BC%E5%88%83&type=feed',
        'accept-encoding':'gzip, deflate, br',
        'cache-control': 'no-cache'
        }
cookie={'cookie':'sessionid=28d43521-87a3-483c-938a-4ad5ef8d90cb; dt_auth=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTUyMDU4MDQsInN1YiI6Im1j55qEbm90Y2giLCJpZCI6MTYwODcxMjMsInBsYXRmb3JtIjoiV0VCIiwidmVyc2lvbiI6MX0.qmpJO3SBk_K-fDzM7Ap82GRXi-1z20bwIVkNcFCpXb0; _auth_user_id=16087123; username=mc%E7%9A%84notch'}

for i in get_blog_id(1,1,'anmi'):
    print(f'获取{i}直链中')
    url="https://www.duitang.com"+i
    content=requests.get(headers=header,
    url=url)
    tree=etree.HTML(content.text)
    srclst+=tree.xpath('//a[@class="img-out"]/@href')
    time.sleep(random.random())
print(f'直链获取完成，共爬取了{len(srclst)}个图片')
for i in range(len(srclst)-1):
    with open(f"{i}.jpg",'wb') as fp:
         print(f'正在下载第{i+1}个图片')
         fp.write(requests.get(headers=header,url=srclst[i]).content)
         time.sleep(random.uniform(0,2))
