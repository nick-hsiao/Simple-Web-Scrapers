from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.sjsu.edu/').text

soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())


for event in soup.find_all('a',class_='o-calendar__event'):
	
	event_title = event.find('p',class_='o-calendar__event-name u-bar u-bar--light u-bar--sjsu-gold').text
	#print(event_title)
	#print(event.prettify())
	try:
		event_link = event['href']
	except Exception as e:
		event_link = None
	
	event_month = event.find('span',class_='o-calendar__month').text
	event_day = event.find('span',class_='o-calendar__day').text

	event_time = event.find('span',class_='o-calendar__detail u-icon u-icon--clock u-color--sjsu-gold').text
	event_time = event_time.replace(' ','').replace('Time:','').strip()

	print(event_title,event_month,event_day,event_time)
