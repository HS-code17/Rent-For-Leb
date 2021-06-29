from bs4 import BeautifulSoup
import requests

# url = "https://www.lebaneselira.org/?ref=w3use.com"
# source = requests.get(url,headers={"user-agent": "curl/7.54.0"})
# soup = BeautifulSoup(source.content, 'html.parser')


url_of_phone= 'https://www.lebaneselira.org/?ref=w3use.com'
page = requests.get(url_of_phone, headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
})
soup = BeautifulSoup(page.text, 'html.parser')
# divs = soup.findAll("table", {"class": "an"})  
# for div in divs:
#     row = ''
#     rows = div.findAll('tr')


# lbp = soup.find('td')
# print(lbp)

print(soup.prettify())

