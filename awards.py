import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.societyforscience.org/regeneron-sts/2020-finalists/')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'content')

names = table.find_all('strong')

projects = table.find_all('p')

names = [item.get_text() for item in names]

projects = [item.get_text() for item in projects]


awards = pd.DataFrame({
	'names:' : names,
	'projects:' : projects[1:],
	})

awards.to_csv('awards.csv')
