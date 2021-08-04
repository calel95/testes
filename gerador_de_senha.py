import random
import string

tamanho = int(input("Tamanho da senha:"))
caracter = int(input("Você quer símbolos na senha?\n1 - Sim\n2 - Não"))
a = '!@#$%&*?\/'
if caracter ==1:
#aqui ele cadastra na variaveis char o alfabeto com letras maiusculas e minusculas com o LETTERS
#e digitos de 0 a 9 com o digits e os caracteres cadastrados na mão
    chars = string.ascii_letters  + string.digits + a
else:
    chars = string.ascii_letters + string.digits

for i in range(tamanho):
# gera a senha de forma aleatoria a partior do sistema operacional
    senha = ''.join(random.choice(chars))
    print('',end = senha)
