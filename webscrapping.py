from bs4 import BeautifulSoup
import re
import urllib2

url = r"html/4.html"
soup = BeautifulSoup(open(url).read())

comments = soup.find_all('div', {'class' : 'jive-comment-content clearfix'})

for comment_element in comments:
	comment = comment_element.find('div', {'class': 'jive-rendered-content'}).getText()
	print comment