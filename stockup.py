import re
import urllib2
from bs4 import BeautifulSoup
import json
import requests
import unicodedata

def symbolLookUp(company):
	url = "http://d.yimg.com/aq/autoc?query=" + company + "&region=IN&lang=en-UK&callback=YAHOO.Finance.SymbolSuggest.ssCallback"
	raw_json = urllib2.urlopen(url).read()
	res = json.loads(raw_json.split('YAHOO.Finance.SymbolSuggest.ssCallback(')[1].split(');')[0])
	return res['ResultSet']['Query']

def parseStockTwits(ticker):
	url = "https://api.stocktwits.com/api/2/streams/symbol/" + ticker + ".json?filter=top"
	raw_json = urllib2.urlopen(url).read()
	res = json.loads(raw_json)
	for msg in res['messages']:
		print unicodedata.normalize('NFKD', msg['body']).encode('ascii','ignore')
		print ''


<<<<<<< HEAD
parseStockTwits('FB')
=======
def symbolLookUp(company):
	pattern = re.compile("\/quote\/.*\?")
	raw_page = urllib2.urlopen("https://finance.yahoo.com/quote/" + company + "?p=" + company).read()
	soup = BeautifulSoup(raw_page,"lxml")
	print soup
	for text in soup.findAll('a'):
		if pattern.match(text):
			print text

symbolLookUp('facebook')
>>>>>>> cc50dcfd20c62341a26ffdf9b2310d78a052a2b1
