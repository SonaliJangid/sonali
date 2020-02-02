import requests
import codecs
from bs4 import BeautifulSoup

a = requests.get("http://www.afterschoolafrica.com/page/2/?s").text
soup = BeautifulSoup(a, 'html.parser')

print(soup.prettify())


# for finding all opportunties
r = soup.findAll("h2", {"class" : "title"})
g=soup.find_all('h2')[0:5]
print(g)
print (g[1].text)
for link in g:
    print(link.text)

    for idx, val in enumerate(g):

        print((idx, val))

soup.find_all('a')