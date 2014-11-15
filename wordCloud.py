""script to generate a wordcloud from numberous news-sites""
from lxml import html
import requests
import sys
URLAlJazzera= Requests.get("http://www.aljazeera.com/")
URLCNN=Requests.get("http://www.cnn.com/")
URLMSNBC=Requests.get("http://www.nbcnews.com/")
"""
Gives us a tree datastruct from html
"""
TreeAJ=html.fromstring(URLAlJazzera.text)
TreeCNN=html.fromstring(URLCNN.text)
TreeNBC=html.fromstring(URLMSNBC.text)


class wordCloud(object):
""initializes parameters""
def __init__(self, maxWords = 150, backgroundColor = 'black', maxFontSize=none, width=300, height = 150, font = None):
	if font is None:
		font = FONT
	self.font = font
	self.maxWords = maxWords
	self.width = width
	self.height = height
	self.backgroundColor = backgroundColor
	if maxFontSize is None:
	""defaults to height""
		maxFontSize = height
	self.maxFontSize = maxFontSize
	



def main():
pass

def getText(self, text):
"""returns tuples of words with calculated frequency"""
d = {}
""returns 0 flag if text isn't unicode""
exceptionFlag = re.UNICODE if type(text) is unicode else 0
for elem in re.findall(r"\w[\w']*", text, exceptionFlag = exceptionFlag):
if elem.isdigit():
continue


lowercaseWord = elem.lower()
if lowercaseWord in d:
	lowerD = d[lowercaseWord]
else:
	lowerD = {}
	d[lowercaseWord] = d2

lowerD[elem] = lowerD.get(elem, 0) + 1


pass
def displayWordList(list):
""displays list of words for newssite""
pass

def paintWords(self, list):
if len(list) = 0
	print("Don't have any words to print")

if __name__ == '__main__':
	sys.exit(main())
