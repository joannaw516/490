import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('http://profiles.dcps.dc.gov/')
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'findschool_tablebody')


items = table.find_all(class_='tr_odd filter-in')

print(items[0].find(class_='schoolname').get_text())
print(items[0].find(class_='principal_name').get_text())


school_list= [item.find(class_= 'schoolname').get_text() for item in items] 
print(school_list)

principal_list = [item.find(class_= 'principal_name').get_text() for item in items] 
print(principal_list)

full_list = pd.DataFrame(
	{'school': school_list,
	'principal_name': principal_list}
	)	
print(full_list)

full_list.to_csv('school_list.csv')