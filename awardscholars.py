import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.societyforscience.org/regeneron-sts/2020-scholars/')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'content')

names = table.find_all('strong')

projects = table.find_all('p')

newnames = []

for item in range(0, len(names), 2):
	newnames.append(names[item].get_text())
	

#names = [item.get_text() for item in names]

projects = [item.get_text() for item in projects]
print(newnames)

awards = pd.DataFrame({
	'names:' : newnames,
	'projects:' : projects[1:],
	})

awards.to_csv('awardscholars.csv')
