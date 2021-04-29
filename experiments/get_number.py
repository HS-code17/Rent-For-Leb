from bs4 import BeautifulSoup
from lxml import etree
import requests
  
url = "https://www.olx.com.lb/ajax/misc/contact/phone/7whmt/"
  
source = requests.get(url,headers={"user-agent": "curl/7.54.0"})
soup = BeautifulSoup(source.text,'html.parser')
tree = etree.HTML(str(soup))
dom = tree.xpath('/html/body/div[4]/section/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/ul/li'[0].text)
print (dom)
# print(dom.xpath('/html/body/div[4]/section/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/ul/li/div')


# response = urlopen(url)
# htmlparser = etree.HTMLParser()
# tree = etree.parse(response, htmlparser)
# tree.xpath(xpathselector)
# /html/body/div[4]/section/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/ul/li
# /html/body/div[4]/section/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/ul/li/div