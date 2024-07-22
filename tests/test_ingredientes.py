import unittest
from models.ingredientes import Ingredientes

def crear_ingredientes():
    return [
        Ingredientes(nombre='Mango', precio=500, calorias=30, inventario=10, es_vegetariano=True),
        Ingredientes(nombre='Leche', precio=200, calorias=100, inventario=10, es_vegetariano=False),
        Ingredientes(nombre='Mani', precio=700, calorias=50, inventario=10, es_vegetariano=False),
        Ingredientes(nombre='Sal', precio=400, calorias=300, inventario=10, es_vegetariano=True)
    ]


class TestIngredientes(unittest.TestCase):
    def setUp(self):
        self.ingredientes = crear_ingredientes()        

    def tearDown(self):
        pass
        #with app.app_context():
        #    db.drop_all()

    def test_es_sano(self):
        self.assertEqual(self.ingredientes[0].es_sano(), True)
        self.assertEqual(self.ingredientes[1].es_sano(), False)
        self.assertEqual(self.ingredientes[2].es_sano(), True)
        self.assertEqual(self.ingredientes[3].es_sano(), True)

    

    
if __name__ == '__main__':
    unittest.main()    

