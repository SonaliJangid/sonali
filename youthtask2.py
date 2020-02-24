import requests
from bs4 import BeautifulSoup

b = requests.get("https://scholarships365.info/university-of-iowa-summer-exchange-program", headers={"User-Agent": "XY"})
soup = BeautifulSoup(b.text, 'html.parser')

 # div = soup.find('div', {"class": "entry-thumbnail"})
 # image = soup.find('img', {"class": "img-responsive"})

image_tag = soup.find("img", {"class": "img-responsive"})
# # print image link
image_link = image_tag['src']
print(image_link)

# div = soup.find("div", {"class": "col-sm-12"})
# officallinks = div.find_all('a')
# print (officallinks['href'])
for data in soup.find_all('div', class_='col-sm-12'):
    for a in data.find_all('a'):
        print(a.get('href')) #for getting link

