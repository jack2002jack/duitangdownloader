import json
import random
import time
import requests
from lxml import etree
root_url="https://cuddlyoctopus.com/shop/"
max_pages=39
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"}

def get_pageurl(page):
    lst = []
    if page<max_pages:
        for i in range(1,page+1):
            time.sleep(random.random())
            response = requests.get(url=root_url+f"page/{i}/", headers=header)
            tree = etree.HTML(response.text)
            obj=tree.xpath(
                "//a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']/@href")
            lst+=obj
        with open("url.json", 'w') as fp:
            json.dump(lst, fp)
    else:
        print("超过最大页数")
def get_picurl():
    with open("url.json",'r') as fp:
        urls=json.load(fp)
    for url in urls:
        response = requests.get(url=url, headers=header)
        tree = etree.HTML(response.text)
        obj = tree.xpath(
                "//form[@class='variations_form cart']/@data-product_variations")
        json_string=obj[0]
        jsonobj=json.loads(json_string)[0]
        print(jsonobj["image"]["url"])
if __name__ == '__main__':
    get_picurl()
