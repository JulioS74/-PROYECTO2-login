
from db import db

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    ingrediente1_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    ingrediente2_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    ingrediente3_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))

    ingrediente1 = db.relationship('Ingredientes', foreign_keys=[ingrediente1_id])
    ingrediente2 = db.relationship('Ingredientes', foreign_keys=[ingrediente2_id])
    ingrediente3 = db.relationship('Ingredientes', foreign_keys=[ingrediente3_id])

    def __init__(self, nombre, precio, ingrediente1_id, ingrediente2_id, ingrediente3_id):
        self.nombre = nombre
        self.precio = precio
        self.ingrediente1_id = ingrediente1_id
        self.ingrediente2_id = ingrediente2_id
        self.ingrediente3_id = ingrediente3_id

    def calcular_costo_de_produccion(self):
        # Implementación del cálculo del costo de producción si es necesario
        pass

    def calcular_rentabilidad(self):
        # Implementación del cálculo de rentabilidad si es necesario
        pass

    def encontrar_producto_mas_rentable(self):
        # Implementación de la lógica para encontrar el producto más rentable si es necesario
        pass    
