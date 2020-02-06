import pdb

import requests
from bs4 import BeautifulSoup

b = requests.get("https://www.afterschoolafrica.com/18901/african-science-academy-scholarship/", headers={"User-Agent": "XY"})
soup = BeautifulSoup(b.text, 'html.parser')
# print(soup.prettify())

# # Allblocks
# h = soup.find_all("div", {"class": "post"})
# # print(h[0])
#
# data = []
# opp_link = []
# headline = []
# imglink = []
# deadline = []
#
# j = soup.find_all("h3", {"class": "entry-title"})
# for idx, text in enumerate(j):
#     opp_link.append(text.a["href"])
#     headline.append(text.text.strip())
# # imagelinks
# j = soup.find_all("div", {"class": "entry-thumbnail"})
# for idx, text in enumerate(j):
#     imglink.append(text.img["src"])
#
# # deadline
# j = soup.find_all("li", {"class": "publish-date"})
# for idx, text in enumerate(j):
#     deadline.append(text.text)
#
# for idx, _ in enumerate(opp_link):
#     data.append({"opp": opp_link[idx], "headline": headline[idx], "image": imglink[idx], "deadline": deadline[idx]})
#
# print (data)

# deadlines
f=soup.find("strong", text=lambda x: x and 'Application Deadline' in x).parent.text.replace('\xa0', ' ')


# eligible countries
ec = soup.find("strong", text=lambda x: x and 'eligible countries' in x.lower()).parent.text.replace('\xa0', ' ')
pdb.set_trace()