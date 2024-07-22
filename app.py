from flask import Flask, render_template
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from controllers.heladeria_controller import heladeria_bp
from controllers.ingredientes_controller import IngredienteController
from controllers.productos_controller import ProductosController

import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
api = Api(app)

# Registrar blueprints y recursos
app.register_blueprint(heladeria_bp, url_prefix='/heladerias')
api.add_resource(IngredienteController, '/ingredientes')
api.add_resource(ProductosController, '/productos')

@app.route("/")
def index():
    from models.productos import Productos
    productos = Productos.query.all()
    return render_template("index.html", productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
