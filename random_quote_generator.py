import requests
import bs4
import random


empty_quotes = []
req4 = requests.get('https://quotes.toscrape.com/')
soup4 = bs4.BeautifulSoup(req4.text,'lxml')
quotes = soup4.select('.text')
# print(quotes)
for items in quotes:
    empty_quotes.append(items.text)

# print(empty_quotes)

rand_quote = random.choice(empty_quotes)
print(rand_quote)