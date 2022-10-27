
class Produto:

    def __init__(self, nome, descricao, categoria = None, ultimoValor = 0, quantidade = 0):
        self.nome = nome
        self.descrição = descricao
        self.ultimoValor = ultimoValor
        self.categoria = categoria
        self.quantidade = quantidade
