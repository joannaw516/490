import pandas as pd
import requests
from bs4 import BeautifulSoup
#import pandas for exporting to csv, requests for fetching html, beautifulsoup for parsing html

#using requests to get html from url, and beautiful soup to parse html content
page = requests.get('http://profiles.dcps.dc.gov/')

soup = BeautifulSoup(page.content, 'html.parser')

#finding main content by id to have access 
table = soup.find(id= 'findschool_tablebody')

#started off by choosing the entire body of the row, including school, principal, etc
items = table.find_all(class_='tr_odd filter-in')
#later added this second part, because they split the schools by odd and even
items2= table.find_all(class_= 'tr_even filter-in')

#print(items[0].find(class_='schoolname').get_text())
#using find all to gather all links
link_list = [item.find_all('a') for item in items]
#creating list of email address text
email_list = [item[-1].get("href") for item in link_list]
#repeating for even schools
link_list2 = [item.find_all('a') for item in items2]

email_list2 = [item[-1].get("href") for item in link_list2]

#print(email_list)

#print(links)
#print(items[0].find_all('a'))

#print(links[-1].get("href"))

#using list comprehension to get school name 
school_list= [item.find(class_= 'schoolname').get_text() for item in items] 
#print(school_list)
#getting principal name
principal_list = [item.find(class_= 'principal_name').get_text() for item in items] 
#print(principal_list)
#repeating again
school_list2= [item.find(class_= 'schoolname').get_text() for item in items2] 
#print(school_list)

principal_list2 = [item.find(class_= 'principal_name').get_text() for item in items2] 
#print(principal_list)
#email_list= [item[-1].get("href") for item in link_list]
#print(email_list)

#exporting to school list, concatenating odd and even schools 
full_list = pd.DataFrame(
	{'school': school_list + school_list2,
	'principal_name': principal_list +principal_list2,
	'email': email_list + email_list2,
	}
	)	
#print(full_list)

full_list.to_csv('school_list.csv')