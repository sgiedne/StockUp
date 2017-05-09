from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords
from textblob import TextBlob

def getSentiment(data):
	sent = 0.0
	psent = 0
	nsent = 0
	for line in data:
		analysis = TextBlob(line)
		sent += analysis.sentiment.polarity
		if analysis.sentiment.polarity >= 0:
			psent+=1
		else:
			nsent+=1

	avgSent = float(sent/len(data))
	# print "Average sentiment: " + str(avgSent)
	print "Percentage of postive articles/tweets: " + str("%.2f"%((float(psent)/len(data))*100)) + "%"
	print "Percentage of negative articles/tweets: " + str("%.2f"%((float(nsent)/len(data))*100)) + "%"
	if avgSent >= 0.5:
		return "Highly Positive"
	elif avgSent < 0.5 and sent > 0:
		return "Positive"
	elif avgSent < 0 and sent >= -0.5:
		return "Negative"
	else:
		return "Highly Negative"