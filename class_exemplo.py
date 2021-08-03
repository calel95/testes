#       EXEMPLO 1

class calculadora:
    def __init__(self,n1 , n2): #define os parametros, por padrao o self tem que ter, o init que inicia a class
        self.a = n1
        self.b = n2
    def soma(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def div(self):
        return self.a / self.b
    def mult(self):
        return self.a * self.b
if __name__ == '__main__':

    calculadora = calculadora(20,4)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.div())
    print(calculadora.mult())

#************************************************************************************************************
#           EXEMPLO 2
class calculadora2:
    def __init__(self):  #funciona sem o metodo init tbm, pois ele esta vazio
        pass
    def soma(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def div(self,a,b):
        return a / b
    def mult(self,a,b):
        return a * b
if __name__ == '__main__':

    calculadora2 = calculadora2()
    print(calculadora2.soma(10,2))
    print(calculadora2.sub(5,3))
    print(calculadora2.div(100,2))
    print(calculadora2.mult(10,5))

#******************************************************************************************************************
#       EXEMPLO 3
class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True
    def aumenta_canal(self):
        self.canal = self.canal + 1
    def diminui_canal(self):
        self.canal = self.canal - 1
if __name__ == '__main__':

    tv = televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    print(tv.canal)
    tv.aumenta_canal()
    tv.aumenta_canal()
    tv.aumenta_canal()
    print(tv.canal)