import re
import urllib2, json
from bs4 import BeautifulSoup
import requests
import unicodedata

def getStockValue(symbol):
	url = "http://www.marketwatch.com/investing/stock/"+symbol
	results = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html_text = results.content

	soup = BeautifulSoup(html_text, 'html.parser')

	tagsStock = soup.findAll("bg-quote", class_="value")
	stockChange = soup.findAll("span", class_="change--point--q")
	percentageChange = soup.findAll("span", class_="change--percent--q")
	LastUpdatedTime = soup.findAll("span", class_="timestamp__time")


	stockValue = 'None'
	changeValue = 'None'
	percentValue = 'None'
	lastUpdatedValue = 'None'


	for match in tagsStock:
		stockValue = match.text.strip()

	for match in stockChange:
		changeValue = match.text.strip()

	for match in percentageChange:
		percentValue = match.text.strip()

	for match in LastUpdatedTime:
		lastUpdatedValue = match.text.strip()

	print 'StockValue '+stockValue
	print 'ChangeValue '+changeValue
	print 'PercentValue '+percentValue
	# print lastUpdatedValue



