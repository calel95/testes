#Se dentro do try der algum erro, ele entra no except
#except BaseException: esse serve para ousar em qualquer erro, pois ele é o pai de todos os erros.
'''
try:
    divisao = 10/0
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero')


try:
    divisao = 10/0
except IndexError:
    print('Erro Desconhecido')

lista = [1,10]
try:
    divisao = 10/2
    numero = lista[1]
except IndexError:
    print('Erro De indice')
except BaseException:
    print('Erro Desconhecido')
else:
    print("se nao tiver excesçao, executa o else")
finally:
    print("finally sempre sera executado")
'''
#Se for digitado uma letra ou numero invalido, ele entrara na excecao ate que seja digitado um numero
while True:
    try:
        n = int(input("digite um numero"))
        print(n)
        break
    except ValueError:
        print("Voce digitou uma letra. Digite um numero")