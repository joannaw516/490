import pandas as pd
import requests
from bs4 import BeautifulSoup
#import pandas for exporting to csv, requests for fetching html, beautifulsoup for parsing html

#using requests to get html from url, and beautiful soup to parse html content
page = requests.get('https://www.societyforscience.org/regeneron-sts/2020-scholars/')

soup = BeautifulSoup(page.content, 'html.parser')

#finding main content by id to have access 
table = soup.find(id= 'content')

#get student names
names = table.find_all('strong')
#get student projects
projects = table.find_all('p')

newnames = []

#there were some empty spots that were also classified as 'strong', had to get rid of those
for item in range(0, len(names)):
	if(names[item].get_text() != '\xa0'):
		newnames.append(names[item].get_text())
	#print(names[item], item)
	

#names = [item.get_text() for item in names]

#did the same thing for the projects
finalprojects = []
for item in range(0, len(projects)):
	if(projects[item].get_text() != '\xa0'):
		finalprojects.append(projects[item].get_text())
	

awards = pd.DataFrame({
	'names:' : newnames,
	'projects:' : finalprojects[1:],
	})

awards.to_csv('awardscholars.csv')
