from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

# 解码网站
# https://tool.chinaz.com/tools/urlencode.aspx

url = "https://life.httpcn.com/xingming.asp"

def get_score(xing, ming):

    data = {
        "isbz": 1,
        "xing": xing.encode("gb2312"),
        "ming": ming.encode("gb2312"),
        "sex": 1,
        "data_type": 0,
        "year": 1998,
        "month": 4,
        "day": 24,
        "hour": 20,
        "minute": 20,
        "pid": "浙江".encode("gb2312"),
        "cid": "舟山".encode("gb2312"),
        "wxxy": 0,
        "xishen": "金".encode("gb2312"),
        "yongshen": "金".encode("gb2312"),
        "check_agree": "agree",
        "act": "submit",
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    resp = requests.post(url, data = urlencode(data), headers = headers)

    # print(resp.status_code)
    resp.encoding = "gb2312"
    # print(resp.text)

    soup = BeautifulSoup(resp.text, "html.parser")

    divs = soup.find_all("div", class_ = "chaxun_b")

    bazi, wuge = 0, 0

    for div in divs:
        if "姓名五格评分" not in div.get_text():
            continue
        fonts = div.find_all("font")
        bazi = fonts[0].get_text().replace("分", "").strip()
        wuge = fonts[1].get_text().replace("分", "").strip()

    return "%s%s"%(xing, ming),bazi,wuge

if __name__ == "__main__":

    with open("D:/Python Tutorial/web_crawler/爬虫给宝宝打名字/input.txt", encoding='utf-8') as fin, open("D:/Python Tutorial/web_crawler/爬虫给宝宝打名字/output.txt", "w") as fout:
        for line in fin:
            print(line)
            line = line.strip()
            xingming, bazi, wuge = get_score("裴", line)
            fout.write("%s\t%s\t%s\n"%(xingming, bazi, wuge))


