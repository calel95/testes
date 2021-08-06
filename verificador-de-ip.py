import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
#abre a url e joga na variavel
resposta = urlopen(url)
#carrega no formato json na variavel dados
dados = json.load(resposta)

print(dados)