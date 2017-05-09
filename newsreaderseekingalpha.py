import re
import urllib2, json
from bs4 import BeautifulSoup
import requests
import unicodedata


def getNewsArticles():
	url = "https://seekingalpha.com/symbol/GOOG/news"
	results = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html_text = results.content

	soup = BeautifulSoup(html_text, 'html.parser')

	newslist = []
	#print soup
	for span in soup.findAll('li'):
		finalText = unicodedata.normalize('NFKD', span.text).encode('ascii','ignore')
		finalText = finalText.replace('\\n', ' ')
		finalText = finalText.replace('\\"', '')
		finalText = re.sub(r'\s\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun).*\s\s+', ' ', finalText)
		finalText = re.sub(r'\s\s+(Mon|Tue|Wed|Thu|Fri|Sat|Sun).*\s\s+.*Comments', ' ', finalText)
		print finalText
		newslist.append(finalText)

	for x in newslist:
		if x is not "None":
			print x
			print ''

getNewsArticles()