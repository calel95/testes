#faz a encriptação da senha para o tipo de hash que desejar
import hashlib


import hashlib
# para fazer a criptografia a senha precisa antes ser codificada para utf8 ou ascii
senha = input("Digite a senha que deseja criptografa:")
resultado = hashlib.md5(senha.encode('utf-8'))

print("A senha criptografada no tipo md5 fica:", resultado.hexdigest())


