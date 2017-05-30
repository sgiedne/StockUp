from bs4 import BeautifulSoup
import requests
import unicodedata

def gethistoricalStockValues(symbol):
	#symbol = "twtr"
	url = "http://www.nasdaq.com/symbol/"+symbol+"/stock-chart?intraday=off&timeframe=5d&charttype=bar&splits=off&earnings=off&movingaverage=None&lowerstudy=volume&comparison=off&index=&drilldown=off&sDefault=true"
	results = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html_text = results.content

	soup = BeautifulSoup(html_text, 'html.parser')

	hist_data = soup.select("div.marginT5px")

	urlValue = 'None'

	for hist in hist_data:
		image = hist.find('img')
		urlValue = image['src']
		# print urlValue


	# url = "http://charting.nasdaq.com/ext/charts.dll?2-1-14-0-0-75-03NA000000TWTR-&SF:43|5-BG=FFFFFF-BT=0-WD=635-HT=395--XTBL-"
	# print url

	url = urlValue+"-XTBL-"
	print url
	results = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html_text = results.content

	soup = BeautifulSoup(html_text, 'html.parser')

	tagsStock = soup.findAll("table", class_="DrillDown")

	cells = []

	for match in tagsStock:
		rows = match.findAll('tr')
		for row in rows:
			allrows = row.findAll('td')
			cells.append(allrows)

	# print cells
	finalHistoricalSet = []
	for cell in cells:
		for x in cell:
			finalHistoricalSet.append(cell[0].text + "   " + cell[1].text + "   "+cell[2].text)

	print "   Date      Value     Volume"
	print ''
	for res in finalHistoricalSet:
		print res
		print ''