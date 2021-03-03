from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import re


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

		# final_list = []
		source = requests.get(url,headers={"user-agent": "curl/7.54.0"})		
		soup = BeautifulSoup(source.text,'html.parser')
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

		# Get their contacts/ phone numbers/ ... 
		# I need to figure out how to press on that specific element 
		# then when I press on that specific element I need to figure out how to unveil the price
		# 
		# this is new, so I need to fix the code a little
		#
		
		res = [str(i) for i in prices]
		
		
		final_list = list(zip(res,names,dates))
		results.extend(final_list)
		results.sort()



# dic_prices_location = {}
# res = [int(i) for i in prices]
# for key in res:
# 	for value in names:
# 		dic_prices_location[key]= value
# 		# names.remove(value)
# 		#this will print a sorted list of the keys
# 		(sorted(dic_prices_location.keys()))
# 		#this will print the sorted list with items.
# 		sorted_dic=(sorted(dic_prices_location.items()))
# 		break
#
# print(results)
# I need to add a way to send this to email + currency converter on the side 

# add also cars prices list 



# so maybe create a list that has two lists inside of it one list made of integers and other made of 
# I want another list that has the smallest prices in it 


length_1 = len(results)

length_2 = len(final_list)

app = Flask(__name__,template_folder= "templates")


@app.route('/')
def hello():
	return render_template('hello.html', result= results, name= length_1, along= length_2)

app.run(host='localhost', port=5000)

		
