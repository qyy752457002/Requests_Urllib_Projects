import requests
import urllib
from bs4 import BeautifulSoup
import os

url = "https://pic.netbian.com/4kmeinv/"

headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Cookie": "__yjs_duid=1_5d91212898a32f469878e0cd30cd72791683416209831; Hm_lvt_c59f2e992a863c2744e1ba985abaea6c=1683416221; zkhanecookieclassrecord=,54,66,; PHPSESSID=b7gs9t26frerl44ijfpu9jct91; zkhanmlusername=qq436361168341; zkhanmluserid=6986185; zkhanmlgroupid=1; zkhanmlrnd=Js5cLyOOaNoRhBhDie17; zkhanmlauth=b0a39ea9fc3aec617f84c32999417cd0; yjs_js_security_passport=54dad339077d7a269ff60d86fdab8aafa1a89cd1_1683419997_js; Hm_lpvt_c59f2e992a863c2744e1ba985abaea6c=1683420002" 
            }

# 用session去保存用户访问url时留下的cookie
session = requests.Session()

resp = session.get(url, headers = headers)
resp.encoding = "gbk"
html = resp.text

soup = BeautifulSoup(html, "html.parser")
imgs = soup.find_all("img")

for img in imgs:
    # get the image src
    src = img.get("src")
    if "/uploads/" not in src:
        continue
    src = f"https://pic.netbian.com{src}"

    print("current image being crawlled:", src)

    # The `os.path.basename` method is a useful tool for extracting the file name from a given file path in Python
    filename = os.path.basename(src)

    # 使用urllib解决图片裂开的问题: https://www.cnblogs.com/aotumandaren/p/14192014.html
    with open(f"D:/Python Tutorial/web_crawler/爬取美女图片/image/{filename}", "wb") as f:
        req = urllib.request.Request(src, headers = headers)
        res = urllib.request.urlopen(req)
        img = res.read()
        f.write(img)