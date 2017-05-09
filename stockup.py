import re
import urllib2
from bs4 import BeautifulSoup




def symbolLookUp(company):
	pattern = re.compile("\/quote\/.*\?")
	raw_page = urllib2.urlopen("https://finance.yahoo.com/quote/" + company + "?p=" + company).read()
	soup = BeautifulSoup(raw_page,"lxml")
	print soup
	for text in soup.findAll('a'):
		if pattern.match(text):
			print text

symbolLookUp('facebook')