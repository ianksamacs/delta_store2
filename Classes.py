class Categoria:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao


class Movimento:
    def __init__(self, Produto, valorUnitario, valorTotal, quantidade=1):
        self.Produto = Produto
        self.quantidade = quantidade
        self.valorTotal = valorTotal
        self.valorUnitario = valorUnitario


class Produto:
    def __init__(self, nome, descricao, Categoria=None, ultimoValor=0, quantidade=0):
        self.nome = nome
        self.descricao = descricao
        self.ultimoValor = ultimoValor
        self.Categoria = Categoria
        self.quantidade = quantidade


class Cliente:
    def __init__(self, nome, telefone=None, cpf=None, endereco=None):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco


class Endereco:
    def __init__(self, logradouro, numero, cidade, estado=None, bairro=None, cep=None):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.bairro = bairro
        self.cep = cep


class Entrada:
    def __init__(self, Movimento, data, origem=None, observacao=None, status="Pendente"):
        self.Movimento = Movimento
        self.data = data
        self.origem = origem
        self.observacao = observacao
        self.status = status


class Saida:
    def __init__(self, Usuario, Movimento, data, Cliente=None, origem=None, observacao=None, status=None):
        self.Usuario = Usuario
        self.Movimento = Movimento
        self.data = data
        self.origem = origem
        self.observacao = observacao
        self.Cliente = Cliente
        self.status = status

class Usuario:
    def __int__(self, nome, login, senha, admin=False):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.admin = admin
