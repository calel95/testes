#serve pra testar conexões, onde usuario digita host e posta e ele tenta conectar, e se der erro mostrar qual
import socket
import sys

def principal():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as er:
        print("A conexão falhou!")
        print(f"Erro: {er}") #mostra o erro que deu
        sys.exit() #fecha o programa
    print("Socket criado com sucesso!")

    hostAlvo = input("Digite Host ou IP a ser conectado: ")
    portaAlvo = int(input("Digite a porta a ser conectada: "))

    try:
        s.connect((hostAlvo, portaAlvo))
        print(f"Cliente TCP conectado no host {hostAlvo} na porta {portaAlvo}")
        s.shutdown(2)
    except socket.error as er:
        print("Conexão falhou!")
        print(f"Erro: {er}")
        sys.exit()

principal()