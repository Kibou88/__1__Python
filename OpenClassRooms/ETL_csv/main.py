import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, 'html.parser')

titres = soup.find_all('div', class_="gem-c-document-list__item-title")
titres_textes = [] # Initialisation de la liste
for titre in titres:
    titre_string = titre.find('a', class_="govuk-link").string
    titres_textes.append(titre_string.string) #On ajoute les titres dans la liste

descriptions = soup.find_all('p', class_="gem-c-document-list__item-description")
descriptions_textes = []
for description in descriptions:
    descriptions_textes.append(description.string)

en_tete = ['titre', 'description']
with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    for titre, description in zip(titres_textes, descriptions_textes):
        writer.writerow([titre, description])