#verifica o estado do telefone
import phonenumbers
from phonenumbers import geocoder

telefone = input("Nùmero do telefone no formato +5511995647864:")

numero_telefone = phonenumbers.parse(telefone)

print(geocoder.description_for_number(numero_telefone, 'pt'))