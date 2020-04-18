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

emaillist = []

# for x in range(20,220):
# 	entry = emails[x].get('href')
# 	if entry == None:
# 		continue
# 	if 
# 	print(entry)

for x in range(2, 202):
 	entry = text[x].get_text()
 	#print(entry, x)
 	if entry == '':
 		continue
 	if entry[0] == ('D') or entry[0] == ('C'):
 		emailaddress= emails[x+18].get('href')
 		emaillist.append(emailaddress[7:])
 		#print(entry)
 		codirectorsanddirectors.append(entry)


	
#print("codirectorsanddirectors:", codirectorsanddirectors)
#print(text[50].get_text())

names= [item.get_text() for item in names] 

#for x in range(27, 50)
	

#print(DUSnames)

full_list = pd.DataFrame(
	{'DUS': codirectorsanddirectors,
	'emails': emaillist
	
	})

departments = pd.DataFrame(
	{'departments': names
	
	})

full_list.to_csv('dus.csv')
departments.to_csv('departments.csv')

#print(emails[27])
