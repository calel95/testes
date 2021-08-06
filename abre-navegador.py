from tkinter import *
import webbrowser

janela = Tk()

janela.title('Abrir Brownser')
janela.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

botao = Button(janela, text='Abrir Google', command=google)
botao.pack(pady=20)
janela.mainloop()
