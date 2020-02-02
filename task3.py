import requests
from bs4 import BeautifulSoup

b = requests.get("http://scholarships365.info/Scholarships", headers={"User-Agent": "XY"})
soup = BeautifulSoup(b.text, 'html.parser')
print(soup.prettify())

# Allblocks
h = soup.find_all("div", {"class": "post"})
print(h[0])

data = []
opp_link = []
headline = []
imglink = []
deadline = []

j = soup.find_all("h3", {"class": "entry-title"})
for idx, text in enumerate(j):
    opp_link.append(text.a["href"])
    headline.append(text.text.strip())
# imagelinks
j = soup.find_all("div", {"class": "entry-thumbnail"})
for idx, text in enumerate(j):
    imglink.append(text.img["src"])





# deadline
j = soup.find_all("li", {"class": "publish-date"})
for idx, text in enumerate(j):
    deadline.append(text.text)

for idx, _ in  enumerate(opp_link):
    data.append({ "opp": opp_link[idx], "headline": headline[idx], "image": imglink[idx], "deadline": deadline[idx]})

print (data)