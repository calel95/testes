import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'
#recebe o ripemd160 algoritmo de hash, de critpigrafia, estipo o md3 sha-256...
hash1 = hashlib.new('md5')
#aqui ele faz a leitura do arquivo que ele ira abrir para comparar o hash, 'rb', modo de leitura binaria
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('md5')
hash2.update(open(arquivo2, 'rb').read())

#fazendo a comparação entre os arquivos
#o digest é necessário, se nao colocar ele nao reconhece o == e o != pra fazer a comparação
#o .hexdigest() serve para mostrar a criptografia que ele fiz do tipo ripemd160 no arquivo
if hash1.digest() == hash2.digest():
    print(f"o arquivo : {arquivo1} é igual do arquivo {arquivo2}")
    print(f"hash arquivo 1: {hash1.hexdigest()}\nhash arquivo 2: {hash2.hexdigest()}")
else:
    print("sao diferentes")
    print(f"hash arquivo 1: {hash1.hexdigest()}\nhash arquivo 2: {hash2.hexdigest()}")

