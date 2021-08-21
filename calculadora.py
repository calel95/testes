from tkinter import *

root = Tk()
root.geometry('150x150+700+250')


def menu():
    def soma():
        a = int(input_n1.get())
        b = int(input_n2.get())
        total = a + b
        resultado.set(str(total))

    def subtrai():
        a = int(input_n1.get())
        b = int(input_n2.get())
        total = a - b
        resultado.set(str(total))

    def multiplicacao():
        a = int(input_n1.get())
        b = int(input_n2.get())
        total = a * b
        resultado.set(str(total))

    def divisao():
        a = float(input_n1.get())
        b = float(input_n2.get())
        total = a / b
        resultado.set(str(total))

    n1 = StringVar()
    n2 = StringVar()
    resultado = StringVar()

    def limpar():
        resultado.set("")
        n1.set("")
        n2.set("")
        input_n1.focus()

    # janela
    L1 = Label(root, text='N1')
    L2 = Label(root, text='N2')
    input_n1 = Entry(root, textvariable=n1)
    input_n2 = Entry(root, textvariable=n2)
    som = Button(root, text='+', command=soma)
    sub = Button(root, text='-', command=subtrai)
    mult = Button(root, text='x', command=multiplicacao)
    div = Button(root, text='/', command=divisao)
    limpar = Button(root, text='limpar', command=limpar)
    res = Label(root, textvariable=resultado)

    L1.grid(row=0, column=0)
    L2.grid(row=1, column=0)
    som.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)
    sub.place(relx=0.3, rely=0.5, relwidth=0.2, relheight=0.2)
    mult.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.2)
    div.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.2)
    input_n1.grid(row=0, column=1)
    input_n2.grid(row=1, column=1)
    res.grid()
    limpar.place(relx=0.4, rely=0.7, relwidth=0.3, relheight=0.2)


menu()
root.mainloop()
