import pdb

import requests
from bs4 import BeautifulSoup

b = requests.get("https://scholarships365.info/Student-Exchange-Program/page/1/", headers={"User-Agent": "XY"})
soup = BeautifulSoup(b.text, 'html.parser')

# # div = soup.find('div', {"class": "row"})
# articles = soup.find_all('div', {"class": "col-sm-4"})
# # print(articles)
# for article in articles:
#     headline = soup.find('h3', {"class": "entry-title"})
# print (headline)
# pdb.set_trace()

opps = []
headlines = soup.find_all('h3', class_="entry-title")
# print (headlines)
for i in headlines:

    heading = i.text
    opp_link = i.a['href']
    opps.append([heading, opp_link])
# print(heading)
pdb.set_trace()