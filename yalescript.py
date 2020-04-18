import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://yalecollege.yale.edu/academics/directory-duses-assistants-and-registrars')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'block-yale-college-content')

names = table.find_all('h2')

cleannames= [item.get_text() for item in names] 
#print(school_list)

emails = table.find_all('a')

text = table.find_all('p')
codirectorsanddirectors = []

print(text[2].get_text())

for x in range(2, 202):
 	entry = text[x].get_text()
 	print(entry, x)
 	if entry == '':
 		continue
 	if entry[0] == ('D') or entry[0] == ('C'):
 		print(entry)
 		codirectorsanddirectors.append(entry)


	
#print("codirectorsanddirectors:", codirectorsanddirectors)


#print(text[50].get_text())

names= [item.get_text() for item in names] 

#for x in range(27, 50)
	

#print(DUSnames)

full_list = pd.DataFrame(
	{'DUS': codirectorsanddirectors
	
	})

departments = pd.DataFrame(
	{'departments': names
	
	})

full_list.to_csv('dus.csv')
departments.to_csv('departments.csv')

#print(emails[27])
