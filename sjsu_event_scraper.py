from bs4 import BeautifulSoup
from datetime import date
import requests
import csv


source = requests.get('http://www.sjsu.edu/').text

soup = BeautifulSoup(source,'lxml')

output_file = open(f'sjsu_event_scrape_{date.today()}.csv','w')

writer = csv.writer(output_file)
writer.writerow(['Name','Date','Time','Location','Link'])

for event in soup.find_all('a',class_='o-calendar__event'):
	
	event_title = event.find('p',class_='o-calendar__event-name u-bar u-bar--light u-bar--sjsu-gold').text
	print(event_title)
	
	event_month = event.find('span',class_='o-calendar__month').text
	event_day = event.find('span',class_='o-calendar__day').text
	event_date = f'{event_month} {event_day}'

	event_time = event.find('span',class_='o-calendar__detail u-icon u-icon--clock u-color--sjsu-gold').text
	event_time = event_time.replace('Time:','').strip()

	print(event_date, event_time)

	event_location = event.find('span',class_='o-calendar__detail u-icon u-icon--location u-color--sjsu-gold').text
	event_location = event_location.replace('Location:','').strip()
	print(event_location)
	
	try:
		event_link = event['href']
	except Exception as e:
		event_link = None
	
	print(event_link)
	print()

	writer.writerow([event_title,event_date,event_time,event_location,event_link])



