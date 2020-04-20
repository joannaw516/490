import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.societyforscience.org/regeneron-sts/2020-scholars/')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'content')

names = table.find_all('strong')

projects = table.find_all('p')

newnames = []


for item in range(0, len(names)):
	if(names[item].get_text() != '\xa0'):
		newnames.append(names[item].get_text())
	print(names[item], item)
	

#names = [item.get_text() for item in names]
finalprojects = []
for item in range(0, len(projects)):
	if(projects[item].get_text() != '\xa0'):
		finalprojects.append(projects[item].get_text())
	
#projects = [item.get_text() for item in projects]
print(len(finalprojects))

awards = pd.DataFrame({
	'names:' : newnames,
	'projects:' : finalprojects[1:],
	})

awards.to_csv('awardscholars.csv')
