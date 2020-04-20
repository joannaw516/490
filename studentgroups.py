import pandas as pd
import requests
from bs4 import BeautifulSoup
#import pandas for exporting to csv, requests for fetching html, beautifulsoup for parsing html

#using requests to get html from url, and beautiful soup to parse html content
page = requests.get('https://admissions.yale.edu/extracurriculars')

soup = BeautifulSoup(page.content, 'html.parser')

#finding main content by id to have access 
table = soup.find(id= 'zone-content')

#get all of the student group headers
headers = table.find_all('h3')

#remove whitespace
headers = [item.get_text().strip() for item in headers]

#gather all links to student groups
links = table.find_all('a')

#separate URL from text / name of group
url = [item.get('href') for item in links]

text = [item.get_text() for item in links]

#export the url and name of group 
groups = pd.DataFrame({
	'url:' : url,
	'text:' : text,
	})


categories = pd.DataFrame(
 	{'categories': headers
	
	})

groups.to_csv('groups.csv')
categories.to_csv('categories.csv')

#i ended up just using the csv for the name of the group and their url to send 