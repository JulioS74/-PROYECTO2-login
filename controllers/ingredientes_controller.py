
from flask_restful import Resource
from models.ingredientes import Ingredientes

class IngredienteController(Resource):
    def get(self):
        ingredientes = Ingredientes.query.all()
        return {'ingredientes': [{'id': i.id, 'nombre': i.nombre, 'precio': i.precio, 'calorias': i.calorias, 'inventario': i.inventario, 'es_vegetariano': i.es_vegetariano} for i in ingredientes]}
    #def by_id(self, id_ingrediente):
    #    return Ingredientes.query.get(id_ingrediente)