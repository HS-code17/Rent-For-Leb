from bs4 import BeautifulSoup
import requests
from urllib import request
import json
import re
import time

def scrape_url(base_url):
    # maybe you choose if this does not work
    valid_pages = input("Enter the number of pages you want to scrape:")
    urls =[]
    results = []
    for n in range(len(valid_pages)):
        url = f'{base_url}?page={valid_pages[n]}'
        # might not need the line here
        # TODO: check this function and refactor it
        source = requests.get(url,headers={"user-agent": "curl/7.54.0"})
        urls.append(url)
    for url in urls:
            prices = []
            names = []
            dates = []
            contacts = []
            source = requests.get(url,headers={"user-agent": "curl/7.54.0"})		
            soup = BeautifulSoup(source.text,'html.parser')
            # print(url)
            for price in soup('p', class_='ads__item__price'):
                pretty= price.text
                po = pretty.strip()
                clean_prices = re.sub('(\s\D+)',' ', po)
                c = str(clean_prices)
                final_list_prices = re.sub('([,\.])','',c)
                p = prices.append(final_list_prices)
            for name in soup('p', class_='ads__item__location'):
                pretty= name.text
                po = pretty.strip()
                p = names.append(po)
            for date in soup('p', class_='ads__item__date'):
                pretty= date.text
                po = pretty.strip()
                p = dates.append(po)
            # this for loop is to extract phone numbers maybe I need to write it in a function alone 
            find_all_a = soup.find_all("a", href=True, class_='ads__item__ad--title')
            for el in find_all_a:
                contact_ad_url = el['href']
                match_id = re.findall(r'(?<=-ID)[\w]*(?=\.html)',contact_ad_url)
                # print(str(match_id))
                # might need to remove 
                time.sleep(1)
                for id in match_id:
                    url_of_phone= 'https://www.olx.com.lb/ajax/misc/contact/phone/'+str(id)
                    page = requests.get(url_of_phone, headers={
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
                    })
                    # time.sleep(1)
                    soup = BeautifulSoup(page.text, 'html.parser')
                    try:
                        site_json=json.loads(soup.text)
                        number= site_json['value']
                        print("phone number:\n",number)
                        # number= site_json['value']
                        contacts.append(str(number))
                    except Exception as e:
                        print(e)
                    # print(contacts)
            res = [str(i) for i in prices]		
            final_list = list(zip(res,names,dates,contacts))
            results.extend(final_list)
            results.sort()
    return results
def check_data(scraped_results):
    if scraped_results is None:
        print ("error parsing stream")
    elif scraped_results:
        return True
    else:
        print ("result fail")
def parse_data(scraped_data):
    # I want to change the price to either Lira or USD based on current rate
    # converted_price = convert_to_usd(current_price)
    # 
    pass
def convert_to_usd():
    # the computation to convert to usd
    # depends on the current daily rate
    # current_daily_rate = foo
    # converted_price= converted_price*foo
    # 
    pass
def present_data():
    # present the current data to a nice graph or maybe to flask
    pass
import pandas as pd
import numpy as np
import requests
