import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('http://profiles.dcps.dc.gov/')
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'findschool_tablebody')


items = table.find_all(class_='tr_odd filter-in')

#print(items[0].find(class_='schoolname').get_text())

link_list = [item.find_all('a') for item in items]

email_list = [item[-1].get("href") for item in link_list]

print(email_list)

#print(links)
#print(items[0].find_all('a'))

#print(links[-1].get("href"))


school_list= [item.find(class_= 'schoolname').get_text() for item in items] 
#print(school_list)

principal_list = [item.find(class_= 'principal_name').get_text() for item in items] 
#print(principal_list)

#email_list= [item[-1].get("href") for item in link_list]
#print(email_list)



full_list = pd.DataFrame(
	{'school': school_list,
	'principal_name': principal_list,
	'email': email_list,
	}
	)	
#print(full_list)

full_list.to_csv('school_list.csv')