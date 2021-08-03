#módulos sao os arquivos .py

import class_exemplo

#quando tem mais de uma classe no modulo
from class_exemplo import calculadora
from contador_letras import conta_letras


#fazendo as chamadas
calculadora = calculadora(20,4)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.div())
print(calculadora.mult())
lista = ['cachorro', 'macaco']
print(conta_letras(lista))

