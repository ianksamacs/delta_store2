# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Classes import *
from tkinter import *




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Testando versionamento')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MainTela = Tk()
    MainTela.state('zoomed')
    meuMenu = Menu(MainTela)
    produtoMenu = Menu(meuMenu, tearoff=0)
    produtoMenu.add_command(label="Novo")
    produtoMenu.add_command(label="Listar")
    meuMenu.add_cascade(label="Produtos", menu=produtoMenu)

    clienteMenu = Menu(meuMenu, tearoff=0)
    clienteMenu.add_command(label="Novo")
    clienteMenu.add_command(label="Listar")
    meuMenu.add_cascade(label="Clientes", menu=clienteMenu)
    

    produtoMenu = Menu(meuMenu, tearoff=0)
    produtoMenu.add_command(label="Novo")
    produtoMenu.add_command(label="Listar")
    meuMenu.add_command(label="Saida")
    produtoMenu = Menu(meuMenu, tearoff=0)
    produtoMenu.add_command(label="Novo")
    produtoMenu.add_command(label="Listar")
    meuMenu.add_command(label="Entrada")
    produtoMenu = Menu(meuMenu, tearoff=0)
    produtoMenu.add_command(label="Novo")
    produtoMenu.add_command(label="Listar")


    MainTela.config(menu=meuMenu)
    MainTela.title("Delta Store")
    MainTela.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
