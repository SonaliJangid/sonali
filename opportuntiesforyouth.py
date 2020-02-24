import pdb

import requests
from bs4 import BeautifulSoup

b = requests.get("https://www.opportunitiesforyouth.org/category/scholarships", headers={"User-Agent": "XY"})
soup = BeautifulSoup(b.text, 'html.parser')

div = soup.find("div", {"class": "post-entry-inner"})
articles = div.find_all("article")

opps = []
for article in articles:
    # bs4 tag
    headline_tag = article.find("h2", class_="post-title")
    headline_content = headline_tag.text
    opp_link = headline_tag.a['href']

    # bs4 tag
    category_tag = article.find("a", {"rel": "category tag"})
    # printing type of opp(master bachelor..)
    category_type = category_tag.text

    # bs4 tag
    image_tag = article.find("img", {"class": "img-is-large"})
    # print image link
    image_link = image_tag['src']

    # todo: merge with 02
    apply_link=''
    b = requests.get(opp_link, headers={"User-Agent": "XY"})
    soup = BeautifulSoup(b.text, 'html.parser')
    last_div = soup.find('div', {"class": "addtoany_content_bottom"})
    # link = element.find_previous_sibling('a')
    for element in last_div.previous_elements:

        if element.name == 'a' and "mailto" not in element['href']:
            apply_link = element['href']
            break

    sub_tags = soup.find('span', {"class": "post-tags"})
    sub_titles = sub_tags.text

    div_element = soup.find('div', {"class": "post-meta"})
    description = div_element.findNext('p').text
    # pdb.set_trace()
    # print (len(description_tag))

    next_p_tag = div_element.findNext('p')
    while description.count(' ') < 50:
        next_p_tag = next_p_tag.findNext('p')
        description += next_p_tag.text + "\n\n"
    descripton_text = description


    opps.append([headline_content, opp_link, category_type, image_link , apply_link, sub_titles , descripton_text])
pdb.set_trace()
