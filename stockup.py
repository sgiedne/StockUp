from parse_seekingalpha import getNewsArticles
from symbol_lookup import symbolLookUp
from parse_stocktwits import parseStockTwits
from sentiment_analysis import getSentiment
from stockvalue import getStockValue
from historicalData import gethistoricalStockValues



# print getNewsArticles('FB')
# print ''
# print symbolLookUp('facebook')
# print ''
# print parseStockTwits('FB')


ticker = symbolLookUp('twitter')
getStockValue(ticker)
gethistoricalStockValues(ticker)
newsArticles = getNewsArticles(ticker)
tweets = parseStockTwits(ticker)
data = tweets + newsArticles
sentiment = getSentiment(data)

print sentiment