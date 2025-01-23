from flask import Blueprint, jsonify, request
from models import db, Hogar

hogares_bp = Blueprint('hogares', __name__)

@hogares_bp.route('/', methods=['GET'])
def obtener_hogares():
    hogares = Hogar.query.all()
    return jsonify([{
        "id": h.id_hogar,
        "nombre": h.nombre_hogar,
        "direccion": h.direccion,
        "ciudad": h.ciudad,
        "pais": h.pais
    } for h in hogares])

@hogares_bp.route('/', methods=['POST'])
def crear_hogar():
    data = request.json
    nuevo_hogar = Hogar(
        id_usuario=data['id_usuario'],
        nombre_hogar=data['nombre_hogar'],
        direccion=data.get('direccion'),
        ciudad=data.get('ciudad'),
        pais=data.get('pais')
    )
    db.session.add(nuevo_hogar)
    db.session.commit()
    return jsonify({"mensaje": "Hogar creado"}), 201



