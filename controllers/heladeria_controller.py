
from flask import Blueprint, render_template, request
from models.heladeria import Heladeria
from db import db

heladeria_bp = Blueprint('heladeria_bp', __name__)

@heladeria_bp.route("/vender/<int:producto_id>", methods=["POST"])
def vender(producto_id):
    heladeria = Heladeria()
    try:
        mensaje = heladeria.vender(producto_id)
        return render_template("resultado.html", mensaje=mensaje)
    except ValueError as e:
        return render_template("resultado.html", mensaje=f"¡Oh no! Nos hemos quedado sin {str(e)}.")
