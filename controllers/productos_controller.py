
from flask_restful import Resource
from models.productos import Productos

class ProductosController(Resource):
    def get(self):
        productos = Productos.query.all()
        return {'productos': [{'id': p.id, 'nombre': p.nombre, 'precio': p.precio, 'ingrediente1_id': p.ingrediente1_id, 'ingrediente2_id': p.ingrediente2_id, 'ingrediente3_id': p.ingrediente3_id} for p in productos]}
