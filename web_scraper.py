from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.sjsu.edu/').text

soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())