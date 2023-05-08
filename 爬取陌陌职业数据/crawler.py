import requests
import json

url = "https://maimai.cn/sdk/web/content/get_list"

# 用session去保存用户访问url时留下的cookie
session = requests.Session()

headers = {
    "useer-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "cookie": "seid=s1683516345087; guid=Gx0fBBkcBBsSHAQbEx1WBxgbHhkfEx4ZExxWHBkEHRkfBUNYS0xLeQoaBBoEGgQTGhsFT0dFWEJpCgNFQUlPbQpPQUNGCgZmZ35iYQIKHBkEHRkfBV5DYUhPfU9GWlprCgMeHFIKER4cREN9ChEaBBobCn5kClldRU5EQ30CChoEHwVLRkZDUEVn; csrftoken=7MdJuMJc-HQR3YEuDkPWuMXHJL-Ip-ZAjDYA; AGL_USER_ID=90d15de2-8e57-4cd2-a337-c0896d433a53; _buuid=e2deb25c-9e6f-4d67-9ee6-00652de4b78f; browser_fingerprint=DEF3C5AE; gdxidpyhxdE=TbKND5Krgqxm8mGuIrRNeimTpZP8/CfdVOfUnyAzZECWsxqphNMl5bO5RbNNYas92AbdnTbx5lWQu2s\0J+AkaE1gQnWLZHYzEVNoi6bCK1c1mda7s7EcVbe8MAKiAUIz+LYJ5OdaurOMrhirAu7H6f4T8jlqMjrnqs1J\I2o5mmwE2A:1683517316722; YD00198168557789:WM_NI=Ji72Dmny3canb1VvsicD2NeXsBxWYCB/al6e8rlM8vb8E5wkNXPx2/DA+YMMQlD0yGOK80egtR98fRl17GIT5HnUfaUNzpWYSQYCaKJdobN0Mip6iuKynyWYbemWJUpFRWY=; YD00198168557789:WM_NIKE=9ca17ae2e6ffcda170e2e6eed1d5398d8aa4abcd5e92b08fb7d85f978e8f87c841b2aa9c86d745fc8f8385e52af0fea7c3b92a8ab7f9d3c767aea7fd84e466a2ef9a97f263a19cfeafe854b19eb8b8dc4982f1af8db56ffcaea4aebb7ea2e88bd6f6618e88a099b125889fe5bad04793b48cd1fc4d8d95f8d1e86db88ef7d9e55ab0eff9a8cc60f798a2b6e56b9792b691d653918f97a4e4418abca183cd3c8fb7c0d7ec7f89a7a29ad653a2bba3b8c95fb49a9eb8dc37e2a3; YD00198168557789:WM_TID=viU5sncxQdZBAUEUBAfFfrvTPHOtEZce; u=239310533; u.sig=CvdGi1NR_N_zG9voaUZszZUcLHU; access_token=1.46c6ff6e58df32102b6cae57053788e9; access_token.sig=cin3UEcKE4txwRAI7ffyeHUYk_U; u=239310533; u.sig=CvdGi1NR_N_zG9voaUZszZUcLHU; access_token=1.46c6ff6e58df32102b6cae57053788e9; access_token.sig=cin3UEcKE4txwRAI7ffyeHUYk_U; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiItU3N2UENvdDc3MkhNd0V0SzZpakNwd3IiLCJ1IjoiMjM5MzEwNTMzIiwiX2V4cGlyZSI6MTY4MzYwMjkzNzQzNCwiX21heEFnZSI6ODY0MDAwMDB9; session.sig=AxnjdoQXawB5gUFI0AYPDXSjh1w",
    "referer": "https://maimai.cn/gossip_list",
    "x-csrf-token": "7MdJuMJc-HQR3YEuDkPWuMXHJL-Ip-ZAjDYA",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors"

}

def craw_page(page_number):

    params = {
        "api": "gossip/v3/square",
        "u": "239310533",
        "page": page_number,
        "before_id": 0
        }

    resp = session.get(url, params = params, headers = headers)
    data = json.loads(resp.text)
    datas = []
    for text in data["list"]:
        datas.append((text["text"]))
    return datas

if __name__ == "__main__":

    with open ("D:/Python Tutorial/web_crawler/爬取陌陌职业数据/脉脉结果.txt", "w") as f:
        for page in range(1, 10 + 1):
            print("current page being crawlled:", page)
            datas = craw_page(page)
            f.write("\n".join(datas) + "\n")



