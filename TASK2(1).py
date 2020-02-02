import requests
from bs4 import BeautifulSoup

a= requests.get("https://www.afterschoolafrica.com/18901/african-science-academy-scholarship/")
soup = BeautifulSoup(a.text, 'html.parser')
print(soup.prettify())


# headline
print(soup.h1.text)


#apply now link

tags=soup.find_all("div",{"class": "call-to-action"})
tag=soup.find_all("a",{"class": "call-to-action-link"})