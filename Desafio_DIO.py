#faz o dobro do seu antecessor 10 vezes
x = int(input())
n = []
soma = 0
dobra = 0
for i in range(10):
    if i > 0:
        dobra = x*2
        x = dobra
        n.append(x)
    else:
        n.append(x)
for i in range(10):
    print(f"N[{i}] = {n[i]}")