#serve pra cria a conexao e envia uma mensagem e espera a resposta dele, como se fosse o ping host
#AF_INET = protocolo ip IPv4
#SOCK_DGRAM = tipo de conexão = conexão UDP
import socket

#cria a conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado!")

host = 'localhost'
porta = 5433
mensagem = 'Cliente diz: Oi servidor'

try:
    print(f'Cliente: {mensagem}')
    #enpacota a mensagem e envia no host, e na porta 5432 do servidor
    s.sendto(mensagem.encode(), (host, 5432)) # o host e a posta o servidor, envia os pacotes
    #servidor e dados recebe do servidor a resposta de 4096bytes
    dados, servidor = s.recvfrom(4096)
    #desempacota os dados e printa os dados
    dados = dados.decode()
    print(f"Cliente: {dados}")
finally:
    print("Cliente: fechando conexão")
    s.close()