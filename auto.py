from tkinter import *
pwd = '1234'

def mostrar_nome():
    nome = txt_login.get()
    senha = txt_senha.get()
    if senha == pwd:
        label_final=Label(root, text='Bem vindo ' + nome)
        label_final.grid(row=3,column=1)
    else:
        label_final = Label(root, text='Senha inválida')
        label_final.grid(row=3, column=1)

#GUI
root = Tk()
root.title("Entrada")
root.geometry('500x500+500+250')

#cria os widgets
label1 = Label(root, text='Login:')
label2 = Label(root, text='Senha:')

txt_login = Entry(root)
txt_senha = Entry(root)

botao1 = Button(root, text='Entrar', command=mostrar_nome)

#organiza os widgets
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
txt_login.grid(row=0,column=1)
txt_senha.grid(row=1,column=1)
botao1.grid(row=2,column=1)

txt_login.focus()
root.mainloop()
