from bs4 import BeautifulSoup

with open("web_crawler/bs4_test/test.html") as fin:
    html_doc = fin.read()

soup = BeautifulSoup(html_doc, "html.parser")

# find a div node with id equal to content
div_node = soup.find("div", id = "content")

try:
    # find all html content with a tag
    inks = div_node.find_all("a")
except:
    print("html not found")
finally:
    print("finally")

# find all content with img tag
img = soup.find("img")
print(img["src"])


# for link in links:
#     print(link.name, link["href"], link.get_text())

