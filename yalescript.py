import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://yalecollege.yale.edu/academics/directory-duses-assistants-and-registrars')

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id= 'block-yale-college-content')

print(soup)
