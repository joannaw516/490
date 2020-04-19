import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://admissions.yale.edu/extracurriculars')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'zone-content')

headers = table.find_all('h3')

headers = [item.get_text().strip() for item in headers]

links = table.find_all('a')

url = [item.get('href') for item in links]

text = [item.get_text() for item in links]

print(len(url), len(text))


groups = pd.DataFrame({
	'url:' : url,
	'text:' : text,
	})


categories = pd.DataFrame(
 	{'categories': headers
	
	})

groups.to_csv('groups.csv')
categories.to_csv('categories.csv')