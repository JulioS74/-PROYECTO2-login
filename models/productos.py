
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

    
