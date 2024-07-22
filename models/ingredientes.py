
from db import db

class Ingredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)

    def es_sano(self):
        return self.calorias < 100 or self.es_vegetariano

    @staticmethod
    def calcular_calorias(ingredientes):
        total_calorias = sum(ingrediente.calorias for ingrediente in ingredientes) * 0.95
        return round(total_calorias, 2)