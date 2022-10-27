# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Classes import *




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Testando versionamento')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    celular = Categoria()
    celular.nome="Teste"
    iphone8 = Produto("Iphone 8", "Bateria 100%")
    mov = Movimento(iphone8,1400,1400)
    print(mov.Produto.nome)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
