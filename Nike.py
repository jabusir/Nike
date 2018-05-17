import webbrowser, requests, bs4
from operator import itemgetter, attrgetter
res = requests.get('https://store.nike.com/us/en_us/pw/mens-clearance-shoes/47Z7puZoi3') 
res.raise_for_status()
parseJunk = bs4.BeautifulSoup(res.text, "html.parser")


priceList = []
kicksList = []


priceJunk = parseJunk.select('span[class="local nsg-font-family--base"]')
kicksJunk = parseJunk.select('p[class="product-display-name nsg-font-family--base edf-font-size--regular nsg-text--dark-grey"]') 


for j in range(len(kicksJunk)):
	kicks = kicksJunk[j].getText()
	kicksList.append(kicks)



for price in range(len(priceJunk)): 
	price = priceJunk[price].getText()
	price = price[1:]
	price = float(price)
	priceList.append(price)



dict = {}
for i in range(len(priceList)):
	dict[priceList[i]] = kicksList[i]


keys = priceList
vals = kicksList 

newdict = sorted(dict.items(), key=itemgetter(0))

for i in newdict:
  print([i],"\n")

