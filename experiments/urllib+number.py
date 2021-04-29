from lxml import html
import requests
from bs4 import BeautifulSoup
from urllib import request
import json
import re
# https://www.olx.com.lb/ajax/misc/contact/phone/7wvhe/
url= 'https://www.olx.com.lb/ad/brand-new-luxurious-apartment-banker-cheque-ref-2372-ID7wvhe.html'
match_id = re.findall(r'(?<=-ID)[\w]*(?=\.html)',url)
print(str(match_id))
for id in match_id:
    url_of_phone= 'https://www.olx.com.lb/ajax/misc/contact/phone/'+str(id)
    page = requests.get(url_of_phone, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
    })
    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup)
    site_json=json.loads(soup.text)
    print("phone number:\n",site_json['value'])

