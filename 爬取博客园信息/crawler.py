import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_web(page_index):

    url = "https://www.cnblogs.com/AggSite/AggSitePostList"

    headers = {"authority": "www.cnblogs.com",
                "method": "POST",
                "path": "/AggSite/AggSitePostList",
                "scheme": "https",
                "accept": "text/plain, */*; q=0.01",
                "accept-encoding": "gzip, deflate, br",
                "accept-language":"en-US,en;q=0.9",
                "cache-control": "no-cache",
                "content-length": "140",
                "content-type": "application/json; charset=UTF-8",
                "cookie": "_ga=GA1.2.1983235547.1681893255; __gads=ID=57202e38c43322f3:T=1681893254:S=ALNI_MbSLDifJzRxsTOSyAS19lmmsZspOw; .AspNetCore.Antiforgery.b8-pDmTq1XM=CfDJ8M-opqJn5c1MsCC_BxLIULkPY_nPmQX9CVb2EbL5BGT-omKCFPT8mmL8y6MyOla8xoss0QVbcSiTCAljZGDAshuVuFmnxYR7RZF098IlqNc2C8_tqqeXGPPfYe9zgESve27XbiXzi80VhM5AHTmwtr0; Hm_lvt_866c9be12d4a814454792b1fd0fed295=1681893255,1682400545,1683420145; _gid=GA1.2.811202701.1683557649; Hm_lpvt_866c9be12d4a814454792b1fd0fed295=1683642199; __gpi=UID=00000bf9fced9ca7:T=1681893254:RT=1683642193:S=ALNI_MbLrWKQT7TdNVdQsr9x1dPjaCQ83g",
                "origin": "https://www.cnblogs.com",
                "pragma": "no-cache",
                "referer": "https://www.cnblogs.com/",
                "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"}

    data = {"CategoryType":"SiteHome","ParentCategoryId":0,"CategoryId":808,"PageIndex":page_index,"TotalPostCount":4000,"ItemListActionName":"AggSitePostList"}

    # 需要查看 initiator里面的aggSite.loadPostList, 查看data原先是以json形式被加载的而不是以字典形式被加载的
    resp = requests.post(url, data = json.dumps(data), headers = headers)
    
    soup = BeautifulSoup(resp.text, "html.parser")
    articles = soup.find_all("article", class_ = "post-item")
    datas = []

    for article in articles:
        link = article.find("a", class_ = "post-item-title")
        title = link.get_text()
        href = link.get("href")
            
        author = article.find("a", class_ = "post-item-author").get_text()
        
        icon_digg = 0
        icon_comment = 0 
        icon_views = 0

        for a in article.find_all("a"):
            if "icon_digg" in str(a):
                icon_digg = a.find("span").get_text()
            if "icon_comment" in str(a):
                icon_comment = a.find("span").get_text()
            if "icon_views" in str(a):
                icon_views = a.find("span").get_text()

        datas.append([title, href, author, icon_digg, icon_comment, icon_views])

    return datas

if __name__ == "__main__":

    all_datas = []
    number = 200

    for page in range(number):
        print("currently crawling:", page)
        datas = scrape_web(0)
        all_datas.extend(datas)

    file_name = "博客园200页文章信息.xlsx"
    dir = "D:/Python Tutorial/web_crawler/爬取博客园信息/"

    file_path = os.path.join(dir, file_name)

    df = pd.DataFrame(all_datas, columns = ["title", "href", "author", "icon_digg", "icon_comment", "icon_views"])
    df.to_excel(file_path, index = False)


            
