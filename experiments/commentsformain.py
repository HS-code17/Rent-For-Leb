# this is how it is first
			# https://www.olx.com.lb/ad/brand-new-luxurious-apartment-banker-cheque-ref-2372-ID7wvhe.html
# 			just_ajax_url = 'https://www.olx.com.lb/ajax/misc/contact/phone/'+match_id+'/'
# 			page = requests.get(just_ajax_url, headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
# })			
# 			soup_for_ad = BeautifulSoup(page.text, 'html.parser')
# 			contact_text= soup.find_all(id='contact_methods'))
			# this is when we have the right url and id 
# 			page = requests.get('https://www.olx.com.lb/ajax/misc/contact/phone/7wvhe/', headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0",
# })
# soup = BeautifulSoup(page.text, 'html.parser')

# 					print(soup)
# 					site_json=json.loads(soup.text)
# 					print("phone number:\n",site_json['value'])
				# for phone in contact_text:
				# 	# phone is going to be the number
				# 	print(phone)
			# pretty= contact_url.text
			# po = pretty.strip()
			# p = contacts.append(po)
			# print(p)

		# for contact in url:
		# 	# this is just url which is basically url
		# 	# we_have_url = 'https://www.olx.com.lb/en/properties/apartments-villas-for-rent/?page=1'
		# 	# split_string_at_6_/ = we_have.split(6,'/')
		# 	slice_we_have_url = url[:-7]
		# 	# we need the ad url
		# 	# <a href="https://www.olx.com.lb/ad/apartment-for-rent-in-achrafieh-ID7tJB9.html" title="Apartment for rent in Achrafieh شقة للإيجار في الأشرفية" class="ads__item__ad--title">
		# 	# Apartment for rent in Achrafieh شقة للإيجا...		</a>
		# 	# div.ads:nth-child(2) > div:nth-child(2) > div:nth-child(2)
		# 	# html body.offersview.standard.smallscreen div#innerLayout
		# 	#  div#listContainer section#body-container.container div.wrapper
		# 	#  div.content.search-results div.rel.listHandler div.ads.ads--gallery 
		# 	# div.ads__item div.ads__item__info
		# 	# ad/duplex-open-sea-view-for-rent-ref-2581-ID7viMp.html
		# 	ad = slice_we_have_url
		# 	insert_ad= 'brand-new-luxurious-apartment-banker-cheque-ref-2372-ID7wvhe'
		# 	contact_url= 'https://www.olx.com.lb/ad/'+insert_string+'.html'
		# 	print(contact_url)
		# for contact in soup()
		# print(soup.find_all(id='contact_methods'))

# https://www.olx.com.lb/ajax/misc/contact/phone/7whmt/

# phone_number = response.html.xpath('/html/body/div[4]/section/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/ul/li/div/strong')
# print(phone_number)

