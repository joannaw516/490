import pandas as pd
import requests
from bs4 import BeautifulSoup
#import pandas for exporting to csv, requests for fetching html, beautifulsoup for parsing html

#using requests to get html from url, and beautiful soup to parse html content
page = requests.get('https://www.societyforscience.org/press-release/intel-isef-2019-special-awards-winners-announced/')

soup = BeautifulSoup(page.content, 'html.parser')

#finding main content by id to have access 
table = soup.find(id= 'content')

#get the students names
names = table.find_all('li')

#strip text
names = [item.get_text() for item in names]

#print(names)
isef = pd.DataFrame({
	'award recipients:' : names
	})

isef.to_csv('isefspecialawards.csv')


