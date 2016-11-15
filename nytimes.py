import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.nytimes.com/")
r_html = r.text
soup = BeautifulSoup(r_html)
title_list = soup.find_all("h2",attrs={"class": "story-heading"})
for title in title_list:
    single_title = title.text.strip()
    if single_title!="":
        print(single_title)

