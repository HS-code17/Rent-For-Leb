from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from urllib import request
import json
import re
import time

valid_pages = '123'
urls =[]
for n in range(len(valid_pages)):
		name = "https://www.olx.com.lb/en/properties/apartments-villas-for-rent/"
		url = f'{name}?page={valid_pages[n]}'
		source = requests.get(url,headers={"user-agent": "curl/7.54.0"})
		urls.append(url)

results = []
# prices = []
# names = []
for url in urls:
		prices = []
		names = []
		dates = []
		contacts = []
		source = requests.get(url,headers={"user-agent": "curl/7.54.0"})		
		soup = BeautifulSoup(source.text,'html.parser')
		print(url)
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

		find_all_a = soup.find_all("a", href=True, class_='ads__item__ad--title')
		for el in find_all_a:
			contact_ad_url = el['href']
			match_id = re.findall(r'(?<=-ID)[\w]*(?=\.html)',contact_ad_url)
			print(str(match_id))
			time.sleep(2)
			for id in match_id:
				url_of_phone= 'https://www.olx.com.lb/ajax/misc/contact/phone/'+str(id)
				page = requests.get(url_of_phone, headers={
					"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
				})
				time.sleep(3)
				soup = BeautifulSoup(page.text, 'html.parser')
				site_json=json.loads(soup.text)
				print("phone number:\n",site_json['value'])
			

		res = [str(i) for i in prices]		
		final_list = list(zip(res,names,dates,))
		results.extend(final_list)
		results.sort()


length_1 = len(results)
length_2 = len(final_list)
app = Flask(__name__,template_folder= "templates")

@app.route('/')
def hello():
	return render_template('hello.html', result= results, name= length_1, along= length_2)

app.run(host='localhost', port=5000)
