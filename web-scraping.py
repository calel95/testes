from bs4 import BeautifulSoup #usado para fazer a extração de dados html e xml
import requests


#content serve para pegar o conteudo do site
site = requests.get('https://www.climatempo.com.br/').content
#soup baixa do site o html
soup = BeautifulSoup(site, 'html.parser')
#Prettify transforma o html em string pra visualizar no print
print(soup.prettify())

