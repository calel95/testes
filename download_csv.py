#forma de fazer download direto do site e armazenando já em uma variavel
import requests
import pandas as pd

url = 'http://sistema.cenipa.aer.mil.br/cenipa/media/opendata/ocorrencia_2010_2020.csv'
df = pd.read_csv(url, encoding = 'latin-1', sep = ';')
df.head()