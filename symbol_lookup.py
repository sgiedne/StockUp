import re
import urllib2
import json

def symbolLookUp(company):
	url = "http://d.yimg.com/aq/autoc?query=" + company + "&region=IN&lang=en-UK&callback=YAHOO.Finance.SymbolSuggest.ssCallback"
	raw_json = urllib2.urlopen(url).read()
	res = json.loads(raw_json.split('YAHOO.Finance.SymbolSuggest.ssCallback(')[1].split(');')[0])
	return res['ResultSet']['Query']