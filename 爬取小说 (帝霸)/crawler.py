import requests
from bs4 import BeautifulSoup
import os

def get_novel_chapters():

    root_url = "http://www.89wx.cc/3/3307/"

    r = requests.get(root_url)
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

if __name__ == "__main__":

    novel_dir = "D:/Python Tutorial/web_crawler/爬取小说 (帝霸)/novel/"

    for chapter in get_novel_chapters():

        url, title = chapter

        title = title.replace("*", "")
        
        file_name = "%s.txt"%title

        if file_name in os.listdir(novel_dir):
            continue

        file_path = os.path.join(novel_dir, file_name)

        print("currently crawling: ", title)

        with open(file_path, "w", encoding = "gbk") as fout:
            content = get_chapter_content(url).replace('\xa0', '')
            fout.write(content)

