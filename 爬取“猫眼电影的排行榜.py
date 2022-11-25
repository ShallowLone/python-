"""
爬取“猫眼电影的排行榜”
"""

import requests
from bs4 import BeautifulSoup
import os

headers = {
    "User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
}

# 获取当前根目录
getcwd = os.getcwd()

for j in range(10):
    # 进入当前跟目录
    os.chdir(getcwd)

    # 在根目录中船舰文件夹“第1页”
    os.mkdir(f"第{j+1}页")

    # 改变当前目录
    os.chdir(f"第{j+1}页")

    response = requests.get(f"https://maoyan.com/board/4?offset={j*10}", headers=headers)

    if response.status_code == 200:
        # 解析网页
        soup = BeautifulSoup(response.text, "lxml")
        imgTag = soup.find_all("img",attrs={"class":"board-img"})
        for imgTag in imgTag:
            name = imgTag.get("alt")
            src = imgTag.get("data-src")
            resp = requests.get(src,headers=headers)
            with open(f"{name}.png","wb") as f:
                f.write(resp.content)
            print(f"{name}{src}保存成功")

