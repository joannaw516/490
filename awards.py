import pandas as pd
import requests
from bs4 import BeautifulSoup
#import pandas for exporting to csv, requests for fetching html, beautifulsoup for parsing html

#using requests to get html from url, and beautiful soup to parse html content
page = requests.get('https://www.societyforscience.org/regeneron-sts/2020-finalists/')

soup = BeautifulSoup(page.content, 'html.parser')

#finding main content by id to have access 
table = soup.find(id= 'content')

#get the students names
names = table.find_all('strong')

#get the projects
projects = table.find_all('p')

#strip just the text
names = [item.get_text() for item in names]

projects = [item.get_text() for item in projects]

#create csv
awards = pd.DataFrame({
	'names:' : names,
	'projects:' : projects[1:],
	})

awards.to_csv('awards.csv')
