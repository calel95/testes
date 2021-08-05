#usado para ataques de força bruta como quebra de autenticação, usada pra testes de invasão

import itertools #biblioteca para gerar lista de varios caracteres diferentes sem repetição de palavras
'''
#faz a permutação das palavras da biblioteca, escolhe a palavra que ele deve procurar e o numero de permutacoes()caracteres
#que serao usados da string ' '
resultado = itertools.permutations('abcdef', 3)

for i in resultado:
    print(''.join(i))
'''

#nesse segundo exemplo ele pega a string digitada e de acordo com o tamanho da string ele faz a wordlist, combinações com as letras
#da string sem repetição
string = input("Palavra a ser permutada:")
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))