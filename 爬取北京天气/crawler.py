import requests
import pandas as pd
import os

class Scraper:
    def __init__(self, url, headers):
        self._url = url
        self._headers = headers
        
    def get_url(self):
        return self._url
    
    def get_headers(self):
        return self._headers
        
    def craw_table(self, year, month):

        params = {
                "areaInfo[areaId]": 54511,
                "areaInfo[areaType]": 2,
                "date[year]": year,
                "date[month]": month
                }
        
        url = self.get_url()
        headers = self.get_headers()

        resp = requests.get(url, headers = headers, params = params)
        data = resp.json()["data"]
        # 返还一个size为1的list, 将list的内容取出
        df = pd.read_html(data)[0]

        return df

if __name__ == "__main__":

    scraper = Scraper(url = 'https://tianqi.2345.com/Pc/GetHistory', headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})

    df_list = []

    for year in range(2012, 2023):
        for month in range(1, 13):
            print("currently crawling:", year, month)
            df = scraper.craw_table(year, month)
            df_list.append(df)

    file_path = "D:/Python Tutorial/web_crawler/爬取北京天气/北京10年天气数据.xlsx"

    pd.concat(df_list).to_excel(file_path, index = False)



