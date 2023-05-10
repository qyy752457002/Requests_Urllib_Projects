import requests
from bs4 import BeautifulSoup
import os

import multiprocessing

def novel_scraper(target_url, directory):

    def get_novel_chapters():

        r = requests.get(target_url)
        r.encoding = "gbk"

        soup = BeautifulSoup(r.text, "html.parser")

        data = []

        for dd in soup.find_all("dd"):
            # under current dd node, there is no html node with tag "a"
            link = dd.find("a")
            if not link:
                continue

            data.append(("http://www.89wx.cc%s"%link.get("href"), link.get_text()))

        return data
    
    def get_chapter_content(url):
        r = requests.get(url)
        r.encoding = "gbk"
        soup = BeautifulSoup(r.text, "html.parser")
        content = soup.find('div', id = "content").get_text()

        return content
    
    for chapter in get_novel_chapters():
    
        url, title = chapter

        title = title.replace("*", "")
        
        file_name = "%s.txt"%title

        if file_name in os.listdir(directory):
            continue

        file_path = os.path.join(directory, file_name)

        print("currently crawling: ", title)

        with open(file_path, "w", encoding = "gbk") as fout:
            content = get_chapter_content(url).replace('\xa0', '')
            fout.write(content)
    
if __name__ == "__main__":

    diba_dir = "D:/Python Tutorial/web_crawler/爬取小说/帝霸"
    jidao_dir = "D:/Python Tutorial/web_crawler/爬取小说/极道天魔"
    daotian_dir = "D:/Python Tutorial/web_crawler/爬取小说/盗天仙途"

    diba_url = "http://www.89wx.cc/3/3307/"
    jidao_url = "http://www.89wx.cc/39/39809/"
    daotian_url = "http://www.89wx.cc/38/38506/"

    # novel_scraper(jidao_url, jidao_dir)

    p1 = multiprocessing.Process(target = novel_scraper, args=(diba_url, diba_dir))
    p2 = multiprocessing.Process(target = novel_scraper, args=(jidao_url, jidao_dir))
    p3 = multiprocessing.Process(target = novel_scraper, args=(daotian_url, daotian_dir))

    # start process 1
    p1.start()
    # starting process 2
    p2.start()
    # starting process 3
    p3.start()

    # main process waits for process 1 and process 2 to complete
    p1.join()
    p2.join()
    p3.join()

    # both processes finished
    print("Done!")






