from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.sjsu.edu/').text

soup = BeautifulSoup(source,'lxml')

for event in soup.find_all('a',class_='o-calendar__event'):
	
	event_title = event.find('p',class_='o-calendar__event-name u-bar u-bar--light u-bar--sjsu-gold').text

	try:
		event_link = event['href']
	except Exception as e:
		event_link = None
	
	event_month = event.find('span',class_='o-calendar__month').text
	event_day = event.find('span',class_='o-calendar__day').text

	event_time = event.find('span',class_='o-calendar__detail u-icon u-icon--clock u-color--sjsu-gold').text
	event_time = event_time.replace('Time:','').strip()

	event_location = event.find('span',class_='o-calendar__detail u-icon u-icon--location u-color--sjsu-gold').text
	event_location = event_location.replace('Location:','').strip()
	
	print(event_title)
	print(event_month,event_day, event_time)
	print(event_location)
	print(event_link)
	print()