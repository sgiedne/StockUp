import urllib2
import json
import unicodedata

def parseStockTwits(ticker):
	tickertweets = []
	url = "https://api.stocktwits.com/api/2/streams/symbol/" + ticker + ".json?filter=top"
	raw_json = urllib2.urlopen(url).read()
	res = json.loads(raw_json)
	for msg in res['messages']:
		tickertweets.append(unicodedata.normalize('NFKD', msg['body']).encode('ascii','ignore'))
	return tickertweets