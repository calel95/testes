#ping simples
#ping -n10 www.google.com - verifica o ping na conexao com o google, enviando 10 pacotes de teste
'''
import os

print('#'*60)
host_ip = input("IP ou Host: ")
qtd_pacotes = int(input("qtd de pacotes a ser enviados:"))
os.system(f'ping -n {qtd_pacotes} {host_ip}')
'''
#ping multiplos, ele le os hosts de dentro do arquivo e faz a leitura deles

import time
import os
#Criando o arquivo txt
def cria_arquivotxt():
    arquivo = open("hosts.txt", 'w')
    arquivo.write('Ip e Hosts a serem lidos')

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.split()
    for i in dump:
        os.system('ping '+ i)
        time.sleep(5)