from bs4 import BeautifulSoup
from datetime import date
import requests
import csv

team_source = requests.get('https://www.nba.com/teams').text
soup = BeautifulSoup(team_source,'lxml')
nba_teams = []

for team in soup.find_all('div',class_='team__list'):
	if team.text == 'Los Angeles Lakers':
		nba_teams.append('LA Lakers')
	nba_teams.append(team.text)
	
source = requests.get('https://www.basketball-reference.com/boxscores/').text
soup = BeautifulSoup(source,'lxml')

todays_games = soup.find('div',class_='game_summary expanded nohover')
print(todays_games.prettify())

winner = todays_games.find('tr',class_='winner')
#print(winner.a.text)

for team in nba_teams:
	if winner.a.text in team:
		winner = team
		break
print(winner)