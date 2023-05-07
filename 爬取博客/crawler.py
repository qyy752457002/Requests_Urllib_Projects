import sys
sys.path.append('D:/Python Tutorial/web_crawler')

from utils import url_manage
import requests
from bs4 import BeautifulSoup
import re

def main():

    root_url = "http://www.crazyant.net/"

    urls = url_manage.UrlManager()
    urls.add_new_url(root_url)

    fout = open("craw_all_pages.txt", "w")

    while urls.has_new_url():
        # get current url
        curr_url = urls.get_url()
        # get request response object
        r = requests.get(curr_url, timeout=3)
        if r.status_code != 200:
            print("error, return status_code is not 200")
            continue
        # establish soup object
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string

        fout.write("%s\t%s\n"%(curr_url, title))
        fout.flush()
        print("success: %s, %s, %d"%(curr_url, title, len(urls.new_urls)))

        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href is None:
                continue
            pattern = r'^http://www.crazyant.net/\d+.html$'
            if re.match(pattern, href):
                urls.add_new_url(href)

    fout.close()

if __name__ == "__main__":
    main()


