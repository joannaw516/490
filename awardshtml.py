from html.parser import HTMLParser

import urllib.request

#request the url, open it, read it and write it to a string so the parser can read it later 
webUrl  = urllib.request.urlopen('https://www.societyforscience.org/regeneron-sts/2020-finalists/').read().decode('utf-8')

class projects(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		#set a counter/tracker for when you come across an open paragraph
		self.paragraphs = 0
		#to hold the collected project info
		self.data = []

	#these are customizations of methods already a part of HTMLparser
	def handle_starttag(self, tag, attrs):
		#check for paragraphs, aka where the projects are defined 
		if tag == 'p':
			#print("hello")
			#if you found a paragraph, reset the counter 
			self.paragraphs = 1 
	def handle_endtag(self, tag):
		if tag == 'p':
			#when you close a paragraph, decount the counter 
			self.paragraphs -=1
			#print("goodbye")

	def handle_data(self, data):
		if self.paragraphs:
			#add data to the collection 
			self.data.append(data)

parser = projects()

#feed in the html 
parser.feed(webUrl)

print(parser.data)
