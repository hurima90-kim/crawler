# Category: a-clumn.a-span8
# Product: a-carousel-row-inner
# Num: zg-bdg-text
# Title: a-link-normal[1]
# Url: a-link-normal[1]['href']
# Rating: a-link-normal[2]
# Price: a-link-normal.a-text-normal[3]

import requests
from bs4 import BeautifulSoup

soup = requests.get(
    "https://www.amazon.com/bestsellers",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    },
)
html = BeautifulSoup(soup.text, "html.parser")

categories = html.select("div.a-column.a-span8")
category_list = []
for category in categories:
    category_list.append(category.text)

category_list.reverse()

divs = html.select("div.a-carousel-row-inner")
for div in divs:
    print("-" * 50)
    print(category_list[-1])
    print("-" * 50)

    lis = div.select("li.a-carousel-card")
    for li in lis:
        num = li.select_one("span.zg-bdg-text").text
        title = li.select("a.a-link-normal")[1].text
        url = "https://www.amazon.com" + li.select("a.a-link-normal")[1]["href"]
        rating = li.select("a.a-link-normal")[2].text
        try:
            price = li.select("a.a-link-normal")[3].text
        except:
            print("값이 존재하지 않습니다.")

        print(num, rating, title, price, sep="\t")
        # print(url)

    category_list.pop()
