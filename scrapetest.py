from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#find title with error handling
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
#use beautifulsoup to make html more organized and readble
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,'html.parser')
#findall() func searches for matching tags and attributes
#get_text() strips tags from text
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

nameList = bsObj.findAll(text="the prince")
print(len(nameList))

allText = bsObj.findAll(id="text")
print(allText[0].get_text())
