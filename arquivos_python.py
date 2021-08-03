#criando um arquivo txt com o nome teste
# o 'w' faz uma nova escrita, ele substitui a antiga pela nova, sobrescreve! também é possível criar arquivo com o 'a'
'''texto = open ('arquivo_teste.txt', 'w')
texto.write("Escrevi essa linha de texto pelo python!")
texto.close()

# O 'a' serve pra fazer atualização, acrescentar novo texto sem apagar o que já está escrito, junto com o .write

texto = open ('arquivo_teste.txt', 'a')
texto.write("\nEscrevi essa segunda linha de texto pelo python!")
texto.close()
'''
def escreve_arquivo(texto):
    arquivo = open('venv/arquivo_teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('venv/arquivo_teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    printando = arquivo.read()
    print(printando)


escreve_arquivo('Primeira linha.\n')
#atualizar_arquivo('Terceira linha linha.\n')
#ler_arquivo('arquivo_teste.txt')