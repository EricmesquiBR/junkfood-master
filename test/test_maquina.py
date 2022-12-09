import unittest

from src.maquina import Maquina


class TestMaquina(unittest.TestCase):

    def testInicializacao(self):
        maquina = Maquina(3, 5)
        self.assertEqual(3, maquina.getSizeEspirais(),
                         "Ao iniciar uma maquina a quantidade de esperiais deve ser igual ao informada no construtor.")
        self.assertEqual(5, maquina.getMaximoProdutos(),
                         "Ao iniciar uma maquina a quantidade máxima de produtos em uma espiral deve ser igual ao informado no construtor.")
        self.assertEqual(0, maquina.getFaturamento(),
                         "Ao iniciar uma maquina o fataturamento deve vir zerado.")
        self.assertEqual(0, maquina.getSaldoCliente(),
                         "Ao iniciar uma maquina o saldo do cliente deve vir zerado.")

    def testPegarEspiralComIndiceValido(self):
        maquina = Maquina(2, 1)
        espiralRetornada = maquina.getEspiral(1)
        self.assertEqual(" - ", espiralRetornada.getNomeDoProduto(),
                         "Deve ser possível retornar uma espiral se o índice for valído.")
        self.assertEqual(0, espiralRetornada.getQuantidade(),
                         "Deve ser possível retornar uma espiral se o índice for valído.")
        self.assertEqual(0, espiralRetornada.getPreco(),
                         "Deve ser possível retornar uma espiral se o índice for valído.")

    def testPegarEspiralComIndiceInvalido(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(2, "Guaraná-Antártica", 2, 4.75),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(1, "Coca-Cola", 1, 3.25),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        espiral = maquina.getEspiral(3)
        self.assertIsNone(espiral, "Não deve ser possível pegar um espiral com índice inválido.")

    def testAlterarEspiralCorretamente(self):
        maquina = Maquina(3, 5)
        self.assertTrue(maquina.alterarEspiral(2, "Ruffles", 4, 4.50),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        espiral = maquina.getEspiral(2)
        self.assertEqual("Ruffles", espiral.getNomeDoProduto(),
                         "Deve ser possível alterar o nome do produto na espiral correspondente ao índice informado.")
        self.assertEqual(4, espiral.getQuantidade(),
                         "Deve ser possível alterar a quantidade de produto na espiral correspondente ao índice informado.")
        self.assertEqual(4.50, espiral.getPreco(),
                         "Deve ser possível alterar o preço do produto na espiral correspondente ao índice informado.")

    def testAlterarEspiralComLimiteExcedido(self):
        maquina = Maquina(4, 2)
        self.assertFalse(maquina.alterarEspiral(1, "Doritos", 5, 5.00),
                         "Não deve ser possível alterar as informações da espiral se a quantidade de produtos excede o limite máximo da maquina")
        self.assertFalse(maquina.alterarEspiral(3, "Coca-Cola", 3, 8.00),
                         "Não deve ser possível alterar as informações da espiral se a quantidade de produtos excede o limite máximo da maquina")

    def testAlterarEspiralComIndiceIncorreto(self):
        maquina = Maquina(2, 3)
        self.assertFalse(maquina.alterarEspiral(4, "Doritos", 2, 5.00),
                         "Não deve ser possível alterar as informações da espiral se o indice informado estiver incorreto.")
        self.assertFalse(maquina.alterarEspiral(-1, "Coca-Cola", 3, 8.00),
                         "Não deve ser possível alterar as informações da espiral se o indice informado estiver incorreto.")

    def testLimparEspiralCorretamente(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(1, "Ruffles", 4, 4.50),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(2, "Coca-Cola", 3, 8.00),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.limparEspiral(1),
                        "Deve ser possível limpar da espiral as descrições dos produtos se o índice estiver correto.")
        espiral = maquina.getEspiral(1)
        self.assertEqual(" - ", espiral.getNomeDoProduto(),
                         "Deve ser possível alterar o nome do produto na espiral para o status vazio.")
        self.assertEqual(0, espiral.getQuantidade(),
                         "Deve ser possível alterar a quantidade de produtos na espira para zero.")
        self.assertEqual(0.0, espiral.getPreco(),
                         "Deve ser possível alterar o preço do produto na espiral para zero.")

    def testLimparEspiralComIndiceIncorreto(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(1, "Ruffles", 4, 4.50),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(2, "Coca-Cola", 3, 8.00),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertFalse(maquina.limparEspiral(3),
                         "Não deve ser possível limpar as informações da espiral se o índice informado estiver incorreto.")
        self.assertFalse(maquina.limparEspiral(-1),
                         "Não deve ser possível limpar as informações da espiral se o índice informado estiver incorreto.")

    def testAdicionarDinheiro(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.inserirDinheiro(4.75),
                        "Deve ser possível adicionar dinheiro na máquina se o valor for maior que 0.")
        self.assertTrue(maquina.inserirDinheiro(5.25),
                        "Deve ser possível adicionar dinheiro na máquina se o valor for maior que 0.")
        self.assertFalse(maquina.inserirDinheiro(-3.35),
                         "Não deve ser possível adicionar dinheiro na máquina se o valor for menor ou igual a 0")
        self.assertEqual(10.00, maquina.getSaldoCliente(),
                         "Deve ser possível um cliente inserir dinheiro na maquina.")

    def testReceberTroco(self):
        maquina = Maquina(3, 4)
        maquina.inserirDinheiro(7.32)
        maquina.inserirDinheiro(6.68)
        self.assertEqual(14.00, maquina.getSaldoCliente(),
                         "Deve ser possível um cliente inserir dinheiro na maquina.")
        self.assertEqual(14.00, maquina.receberTroco(),
                         "Deve ser possível o cliente receber o troco da maquina.")
        self.assertEqual(0, maquina.getSaldoCliente(),
                         "Ao receber o troco o saldo do cliente fica zerado.")

    def testVenderProdutoComSucessoEReceberTroco(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(1, "Ruffles", 3, 4.50),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(0, "Lays", 2, 5.00),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(2, "Sensações", 2, 6.00),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.inserirDinheiro(2.25),
                        "Deve ser possível adicionar dinheiro na máquina se o valor for maior que 0.")
        self.assertTrue(maquina.inserirDinheiro(4.75),
                        "Deve ser possível adicionar dinheiro na máquina se o valor for maior que 0.")
        self.assertTrue(maquina.vender(2),
                        "Deve ser possível vender um produto da espiral se a máquina estiver com saldo sufieciente e se houver quantidade suficiente na espiral.")
        self.assertEqual(1.00, maquina.getEspiral(2).getQuantidade(),
                         "Ao vender um item a quanditidade de produto será decrementada se ainda houver mais produtos na espiral.")
        self.assertEqual(1.00, maquina.receberTroco(),
                         "Deve ser possível o cliente receber troco se houver troco resultante da compra.")
        self.assertEqual(6.00, maquina.getFaturamento(),
                         "Ao vender um item o lucro é incrementado com o valor do produto que foi vendido da espiral.")

    def testVenderProdutoComSucessoELimparEspiral(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(2, "Guaraná-Antártica", 2, 4.75),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(1, "Coca-Cola", 1, 3.25),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        maquina.inserirDinheiro(12.00)
        self.assertTrue(maquina.vender(2),
                        "Deve ser possível vender um produto da espiral se a máquina estiver com saldo sufieciente e se houver quantidade suficiente na espiral.")
        self.assertTrue(maquina.vender(2),
                        "Deve ser possível vender um produto da espiral se a máquina estiver com saldo sufieciente e se houver quantidade suficiente na espiral.")
        self.assertEqual(2.50, maquina.receberTroco(),
                         "Deve ser possível o cliente receber troco se houver troco resultante da compra.")
        self.assertEqual(9.50, maquina.getFaturamento(),
                         "Ao vender um item o lucro é incrementado com o valor do produto que foi vendido da espiral.")
        espiral = maquina.getEspiral(2)
        self.assertEqual(" - ", espiral.getNomeDoProduto(),
                         "Deve ser possível alterar o nome do produto na espiral para o status vazio.")
        self.assertEqual(0, espiral.getQuantidade(),
                         "Deve ser possível alterar a quantidade de produtos na espira para zero.")
        self.assertEqual(0.0, espiral.getPreco(),
                         "Deve ser possível alterar o preço do produto na espiral para zero.")

    def testVenderProdutoComIndiceErrado(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(2, "Guaraná-Antártica", 2, 4.75),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(1, "Coca-Cola", 1, 3.25),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.inserirDinheiro(5.25),
                        "Deve ser possível adicionar dinheiro na máquina se o valor for maior que 0.")
        self.assertFalse(maquina.vender(3),
                         "Não deve ser possível vender um produto se o indice não corresponder a nenhuma espiral.")
        self.assertFalse(maquina.vender(-2),
                         "Não deve ser possível vender um produto se o indice não corresponder a nenhuma espiral.")

    def testVenderProdutoSemDinheiroSuficiente(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(2, "Guaraná-Antártica", 2, 4.75),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(1, "Coca-Cola", 1, 3.25),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        maquina.inserirDinheiro(4.70)
        self.assertEqual(4.70, maquina.getSaldoCliente(),
                         "Deve ser possível um cliente inserir dinheiro na maquina.")
        self.assertFalse(maquina.vender(2),
                         "Não deve ser possível comprar um produto se o dinheiro inserido na máquina não for suficiente.")
        espiral = maquina.getEspiral(2)
        self.assertEqual(2, espiral.getQuantidade(),
                         "Não deve ser possível alterar a quantidade de produtos se não foi possível vender o produto.")

    def testVenderProdutoComDinheiroExato(self):
        maquina = Maquina(3, 4)
        self.assertTrue(maquina.alterarEspiral(2, "Guaraná-Antártica", 2, 4.75),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        self.assertTrue(maquina.alterarEspiral(1, "Coca-Cola", 1, 3.25),
                        "Deve ser possível alterar as informações da espiral com as descrições do produto se o índice estiver correto.")
        maquina.inserirDinheiro(3.25)
        self.assertEqual(3.25, maquina.getSaldoCliente(),
                         "Deve ser possível um cliente inserir dinheiro na maquina.")
        self.assertTrue(maquina.vender(1),
                        "Deve ser possível vender um produto da espiral se a máquina estiver com saldo sufieciente e se houver quantidade suficiente na espiral.")
        espiral = maquina.getEspiral(1)
        self.assertEqual(0, espiral.getQuantidade(),
                         "Deve ser possível alterar a quantidade de produtos se o foi possível vender o produto.")


if __name__ == '__main__':
    unittest.main()
