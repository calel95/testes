import ctypes


endereco_arquivo = 'C:/Users/calel/OneDrive/Área de Trabalho/AtestadoMatricula.pdf'
#cria a dll para que o arquivo possa ser ocultado pelo sistema, o digito 2 é pra ocultar
retorno = ctypes.windll.kernel32.SetFileAttributesW(endereco_arquivo, 2)

if retorno == True:
    print("Arquivo ocultado!")
else:
    print("Nao funcionou")