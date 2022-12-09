class Espiral:
    def __init__(self):
        self.NomeDoProduto = " - "
        self.Quantidade= 0
        self.Preco = 0.0

    def getNomeDoProduto(self):
        return self.NomeDoProduto

    def getQuantidade(self):
        return self.Quantidade

    def getPreco(self):
        return self.Preco

    def setNomeDoProduto(self, nome: str):
        self.NomeDoProduto = nome
        return True

    def setQuantidade(self, qtd: int):
        self.Quantidade = qtd
        return True

    def setPreco(self, preco: float):
        self.Preco = preco
        return True
