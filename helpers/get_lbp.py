from bs4 import BeautifulSoup
import requests

url= 'https://www.lebaneselira.org/?ref=w3use.com'
page = requests.get(url, headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
})
soup = BeautifulSoup(page.text, 'html.parser')

lbp = soup.find('td')
print(lbp)
print(soup.prettify())