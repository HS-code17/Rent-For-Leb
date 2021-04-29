from lxml import html
import requests
from bs4 import BeautifulSoup
# from urllib import urlopen
import json

  
# Request the page
page = requests.get('https://www.olx.com.lb/ad/brand-new-luxurious-apartment-banker-cheque-ref-2372-ID7wvhe.html', headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
})
soup = BeautifulSoup(page.text, 'html.parser')
# https://www.olx.com.lb/ajax/misc/contact/phone/7wvhe/
# 
# value	"03803131"
# endpoint = requests.get('https://www.olx.com.lb/ajax/misc/contact/phone/7whmt/', headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
# })

# soups = BeautifulSoup(endpoint.text, 'html.parser')
# print the number
# print(soups)

# url = urlopen('https://www.olx.com.lb/ajax/misc/contact/phone/7wvhe/').read()
# result = json.loads(url)
# print '"networkdiff":', result['getpoolstatus']['data']['networkdiff']
# string.match(/(?<=-ID)[\w]*(?=\.html)/)

match_id = re.findall(r'(?<=-ID)[\w]*(?=\.html)',string)

print ("phone number:", result['value'])

numbers = []
contact_text = soup.find_all(id='contact_methods')

contact_string = str(contact_text)
# print(contact_string)


# for number in soup('li', class_='rel'):
#         pretty= number.text
#         po = pretty.strip()
#         p = numbers.append(po)
#         print(p)

# for number in contact_text:

#     print(number)

# for number in soup('p', class_='ads__item__date'):
#         pretty= date.text
#         po = pretty.strip()
#         p = dates.append(po)
# tree = html.fromstring(page.content) 
# # 
# xpath_path = tree.xpath('//*[@id="contact_methods"]/li/div/text()')
# print(xpath_path)