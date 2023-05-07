# 构造分页数字列表
import requests
from bs4 import BeautifulSoup
import pandas as pd

page_indexs = range(0, 250, 25)

def download_all_htmls():

    headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
   }

    htmls = []
    # iterate over each page's html
    for idx in page_indexs:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        r = requests.get(url, headers = headers)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)

    return htmls

def parse_single_html(html):

    soup = BeautifulSoup(html, 'html.parser')
    article_items = (
        soup.find("div", class_ = "article")
            .find("ol",  class_ = "grid_view")
            .find_all("div", class_ = "item")
    )

    datas = []

    for article_item in article_items:
        rank = article_item.find("div", class_ = "pic").find("em").get_text()
        info = article_item.find("div", class_ = "info")
        title = info.find("div", class_ = "hd").find("span", class_ = "title").get_text()
        stars = (
            info.find("div", class_ = "bd")
                .find("div", class_ = "star")
                .find_all("span")
        )
        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()

        datas.append(
            {"rank": rank,
            "title": title,
            "rating_star": rating_star.replace("rating", "").replace("-t",""),
            "rating_num":rating_num,
            "comments":comments.replace("人评价", "")}
        )

    return datas

if __name__ == "__main__":

    all_datas = []

    htmls = download_all_htmls()

    for html in htmls:
        all_datas.extend(parse_single_html(html))

    file_path = "D:/Python Tutorial/web_crawler/爬取豆瓣电影/豆瓣电影top250.xlsx"

    df = pd.DataFrame(all_datas)
    df.to_excel(file_path, index = False)
    