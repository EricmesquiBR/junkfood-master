import unittest

from src.espiral import Espiral


class TestEspiral(unittest.TestCase):

    def testInicializacao(self):
        espiral = Espiral()
        self.assertEqual(" - ", espiral.getNomeDoProduto(),
                         "Ao inicializar uma espiral ela deve conter o simbólo ' - ' para representar que não há produto definido")
        self.assertEqual(0, espiral.getQuantidade(),
                         "Ao inicializar uma espiral a quantidade de produtos deve vir zerada")
        self.assertEqual(0, espiral.getPreco(),
                         "Ao inicializar uma espiral o preco do produto na espiral deve vir zaerado")

    def testAlterandoEspiral(self):
        espiral = Espiral()
        espiral.setNomeDoProduto("m&m")
        espiral.setPreco(3.25)
        espiral.setQuantidade(5)
        self.assertEqual("m&m", espiral.getNomeDoProduto(),
                         "Deve ser possível alterar o nome do produto que está na espiral")
        self.assertEqual(3.25, espiral.getPreco(), "Deve ser possível alterar o preço do produto que está na espiral")
        self.assertEqual(5, espiral.getQuantidade(),
                         "Deve ser possível alterar a quantidade de produtos que está na espiral")


if __name__ == '__main__':
    unittest.main()
