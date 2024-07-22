
from models.productos import Productos
from models.ingredientes import Ingredientes
from db import db

class Heladeria:
    def __init__(self):
        self.ingredientes = Ingredientes.query.all()
        self.productos = Productos.query.all()

    def vender(self, producto_id: int):
        producto_vendido = None
        for producto in self.productos:
            if producto_id == producto.id:
                if producto.ingrediente1.inventario <= 0:
                    raise ValueError(producto.ingrediente1.nombre)
                if producto.ingrediente2.inventario <= 0:
                    raise ValueError(producto.ingrediente2.nombre)
                if producto.ingrediente3.inventario <= 0:
                    raise ValueError(producto.ingrediente3.nombre)
                producto.ingrediente1.inventario -= 1
                producto.ingrediente2.inventario -= 1
                producto.ingrediente3.inventario -= 1
                producto_vendido = producto
                break

        if producto_vendido:
            db.session.commit()
            return "¡Vendido!"
        else:
            raise ValueError("El producto solicitado no está disponible en el menú.")
