from bs4 import BeautifulSoup
from datetime import date
import requests
import csv

team_source = requests.get('https://www.nba.com/teams').text
soup = BeautifulSoup(team_source,'lxml')
nba_teams = []

output_file = open(f'nba_scores_{date.today()}.csv','w')

writer = csv.writer(output_file)
writer.writerow(['Winning Team','Score','Losing Team','Score','Best Player','Score'])

for team in soup.find_all('div',class_='team__list'):
	if team.text == 'Los Angeles Lakers':
		nba_teams.append('LA Lakers')
	nba_teams.append(team.text)

source = requests.get('https://www.basketball-reference.com/boxscores/').text
soup = BeautifulSoup(source,'lxml')

for game in soup.find_all('div',class_='game_summary expanded nohover'):
	#print(game.prettify())

	winner = game.find('tr',class_='winner')
	#print(winner.a.text)
	winner_score = winner.find('td',class_='right').text


	for team in nba_teams:
		if winner.a.text in team:
			winner = team
			break
	
	print(winner,winner_score)
	loser = game.find('tr',class_='loser')
	loser_score = loser.find('td',class_='right').text
	
	for team in nba_teams:
		if loser.a.text in team:
			loser = team
			break

	print(loser,loser_score)

	player = game.find('table',class_='stats')
	player_name = player.a.text
	player_score = player.find('td',class_='right').text
	print(player_name,player_score,'\n')

	writer.writerow([winner,winner_score,loser,loser_score,player_name,player_score])
	

