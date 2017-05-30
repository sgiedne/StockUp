from parse_seekingalpha import getNewsArticles
from symbol_lookup import symbolLookUp
from parse_stocktwits import parseStockTwits
from sentiment_analysis import getSentiment
from stockvalue import getStockValue
from historicalData import gethistoricalStockValues
from bs4 import BeautifulSoup
import requests
import unicodedata


# print getNewsArticles('FB')
# print ''
# print symbolLookUp('facebook')
# print ''
# print parseStockTwits('FB')


try:
	input_var = raw_input("Enter company name OR ticker symmbol: ")
	ticker = symbolLookUp(input_var)

	url = "http://www.finviz.com/quote.ashx?t="+ticker
	results = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html_text = results.content

	soup = BeautifulSoup(html_text, 'html.parser')
	tagsStock = soup.findAll("a", { "class" : "tab-link-news" })

	data = []

	for x in tagsStock:
		data.append(x.text)

	sentiment = getSentiment(data)
	print "General attitude towards company (based off finviz): " + sentiment
except:
	print 'error fetching data'