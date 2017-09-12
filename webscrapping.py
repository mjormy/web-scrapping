from bs4 import BeautifulSoup
import re
import urllib2

url = r"html/5.html"
soup = BeautifulSoup(open(url).read())

comments = soup.find_all('div', {'class' : 'jive-comment-content clearfix'})

for comment in comments:
	print comment