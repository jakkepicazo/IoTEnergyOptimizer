from flask import Blueprint, jsonify, request
from models import db, Consumo

consumos_bp = Blueprint('consumos', __name__)

@consumos_bp.route('/', methods=['GET'])
def obtener_consumos():
    consumos = Consumo.query.all()
    return jsonify([{
        "id": c.id_consumo,
        "id_dispositivo": c.id_dispositivo,
        "fecha_hora": c.fecha_hora,
        "consumo_kwh": c.consumo_kwh
    } for c in consumos])

@consumos_bp.route('/', methods=['POST'])
def registrar_consumo():
    data = request.json
    nuevo_consumo = Consumo(
        id_dispositivo=data['id_dispositivo'],
        consumo_kwh=data['consumo_kwh']
    )
    db.session.add(nuevo_consumo)
    db.session.commit()
    return jsonify({"mensaje": "Consumo registrado"}), 201
