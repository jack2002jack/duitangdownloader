import sys

import requests
from lxml import etree
def get_pic(year,month,count,subfix):
    #down search



    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"}
    ny = year
    nm = month
    nc = count
    while 1:
        if nm >=10:
            url = f"https://cuddlyoctopus.com/wp-content/uploads/{ny}/{nm}/{nc}"+ subfix
        else:
            url = f"https://cuddlyoctopus.com/wp-content/uploads/{ny}/0{nm}/{nc}"+ subfix
        response = requests.get(url=url, headers=header)
        print("开始任务 ",url)
        if response.status_code==404:
            print("获取链接失败")
            nc-=1
            if nc<count-10:
                if nm==1:
                    return get_pic(year-1, 12, nc+11, subfix)
                else:
                    return get_pic(year,month-1,nc+10,subfix)
        else:
            with open(f"{nc}{subfix}",'wb') as fp:
                fp.write(response.content)
                print(f"下载{nc}{subfix}成功")
                year=ny
                month=nm
                nc-=1
                count=nc


if __name__ == '__main__':
    month=5
    get_pic(2017,4,165,".png")