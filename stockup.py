from parse_seekingalpha import getNewsArticles
from symbol_lookup import symbolLookUp
from parse_stocktwits import parseStockTwits


print getNewsArticles('FB')
print ''
print symbolLookUp('facebook')
print ''
print parseStockTwits('FB')