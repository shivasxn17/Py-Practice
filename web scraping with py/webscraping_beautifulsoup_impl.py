import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bsup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1"
html = urllib.request.urlopen(url).read()

soup = bsup(html,'html.parser')
movies_divs = soup.find_all('div', class_ = 'lister-item mode-advanced')
print(soup.title)
top_50_movie_list = []
for item in movies_divs: 
	top_50_movie_list.append(item.h3.a.text)
print(top_50_movie_list)