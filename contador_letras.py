#como ficaria fazendo em lambda
'''
conta_letra = lambda lista: [len(i) for i in lista]

lista = ['macaco', 'elefante']
print(conta_letra(lista))
'''
def conta_letras(lista_letras):
    cont = []
    for i in lista_letras:
        qtd = len(i)
        cont.append(qtd)
    return cont

if __name__ == '__main__':
    lista = ['macaco', 'elefante']
    print(conta_letras(lista))