import socket

#ria objeto de conexao
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado!')

host = 'localhost'
porta = 5432

#faz a ligação a partir do host e da porta do host
s.bind((host, porta))
mensagem = '\nServidor diz: Oi Cliente'

#se for verdadeiro
while True:
    #envia os dados
    dados, end = s.recvfrom(4096)
#se tiver dados
    if dados:
        print("servidor enviando mensagem...")
        #enviando a mensagem
        s.sendto(dados + (mensagem.encode()), end)