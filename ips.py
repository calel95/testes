import ipaddress
#fazendo calculos com ip, assim pode adicionar e sustrair a quantidade que desejar que ele faz o calculo
ip = '192.168.0.1'
endereco = ipaddress.ip_address((ip))
print(endereco + 100)

#faz a mesma coisa acima porem aqui ele pega a red junto
ip = '192.168.0.0/24'
#se colocar como false ele aceita qualquer endereco ip, senao ele so aceita ip valido
rede = ipaddress.ip_network(ip, strict=False)

print(rede)
