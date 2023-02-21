import bs4, requests
def AmazonPrice(productPrice):
	res = requests.get(productPrice)

	#print(res.text)
	#this prints the HTML source for us but we need to parse the html to string with beautiful soup so ...

	soup = bs4.BeautifulSoup(res.text , 'html.parser')

	elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
	return elems[0].text.strip()

price = AmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The price is ' + price)