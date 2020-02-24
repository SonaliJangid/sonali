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

    # TASK 2 MERGING
    b = requests.get(opp_link, headers={"User-Agent": "XY"})
    soup = BeautifulSoup(b.text, 'html.parser')

    image_tag = soup.find("img", {"class": "img-responsive"})
    image_link = image_tag['src']
    # print(image_link)

    # deadline
    deadline = soup.find("strong", text=lambda x: x and 'Deadline' in x).parent.text
    # print(deadline)

    # hosting country
    country = soup.find('li', class_="views")
    hosting_country = country.text
    # print(country.text)
    pdb.set_trace()

    # description
    desc = soup.find('div', {"class": "entry-content"})
    first_desc = desc.findNext('p').text
    # print (desc.findNext('p').text)

    # official link
    div = soup.find("div", {"class": "col-sm-12 text-center"})
    link = div.findNext('a')
    official_link = link.findNext('a')
    officiallink = official_link['href']
    # print(officiallink)
    opps.append([heading, opp_link, image_link, hosting_country, first_desc, officiallink])
# print(heading)
pdb.set_trace()