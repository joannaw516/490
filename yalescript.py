import pandas as pd
import requests
from bs4 import BeautifulSoup
#import pandas for exporting to csv, requests for fetching html, beautifulsoup for parsing html

#using requests to get html from url, and beautiful soup to parse html content

page = requests.get('https://yalecollege.yale.edu/academics/directory-duses-assistants-and-registrars')

soup = BeautifulSoup(page.content, 'html.parser')

#finding main content by id to have access 
table = soup.find(id= 'block-yale-college-content')

#find all main headers, the departments
names = table.find_all('h2')

#remove white space from both ends of text
cleannames= [item.get_text() for item in names] 
#print(school_list)

#find all email addresses / links 
emails = table.find_all('a')

#find all directors and registrars names 
text = table.find_all('p')
codirectorsanddirectors = []

emaillist = []

# for x in range(20,220):
# 	entry = emails[x].get('href')
# 	if entry == None:
# 		continue
# 	if 
# 	print(entry)

#this part was a little janky, there was a lot of variance in the directors- 
#some departments had co-directors, some had 1 DUS, some had 2, some had one for the fall and one for the spring

for x in range(2, 202):
 	entry = text[x].get_text()
 	#print(entry, x)
 	#remove empty strings
 	if entry == '':
 		continue
 	if entry[0] == ('D') or entry[0] == ('C'):
 		#this part was also very janky, i indexed into the emails offset by the few links for the letters at the top of the page 	
 		emailaddress= emails[x+18].get('href')
 		emaillist.append(emailaddress[7:])
 		#print(entry)
 		codirectorsanddirectors.append(entry)


	
#print("codirectorsanddirectors:", codirectorsanddirectors)
#print(text[50].get_text())
#get the text for all of the DUS names
names= [item.get_text() for item in names] 

#for x in range(27, 50)
	

#print(DUSnames)
#exported the emails and names separately from the departments
full_list = pd.DataFrame(
	{'DUS': codirectorsanddirectors,
	'emails': emaillist
	
	})

departments = pd.DataFrame(
	{'departments': names
	
	})

#export to CSV
full_list.to_csv('dus.csv')
departments.to_csv('departments.csv')

#print(emails[27])

#next steps for researching this would likely be to check out ways to web scrape that don't use find_all and scrape a page in chronological order
