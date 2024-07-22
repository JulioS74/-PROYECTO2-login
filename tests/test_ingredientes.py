import unittest
from models.ingredientes import Ingredientes

class TestIngredientes(unittest.TestCase):
    def setUp(self):
        self.ingredientes = [
            Ingredientes(nombre='Azúcar', precio=500, calorias=30, inventario=10, es_vegetariano=True),
            Ingredientes(nombre='Leche', precio=200, calorias=100, inventario=10, es_vegetariano=False),
            Ingredientes(nombre='Chocolate', precio=700, calorias=200, inventario=10, es_vegetariano=True)
        ]

    def test_es_sano(self):
        self.assertTrue(self.ingredientes[0].es_sano())
        self.assertFalse(self.ingredientes[1].es_sano())
        self.assertTrue(self.ingredientes[2].es_sano())

    def test_abastecer(self):
        # Implementar las pruebas para el método abastecer si es necesario
        pass

if __name__ == '__main__':
    unittest.main()
