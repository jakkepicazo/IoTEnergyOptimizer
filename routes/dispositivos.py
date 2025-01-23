from flask import Blueprint, jsonify, request
from models import db, Dispositivo

dispositivos_bp = Blueprint('dispositivos', __name__)

@dispositivos_bp.route('/', methods=['GET'])
def obtener_dispositivos():
    dispositivos = Dispositivo.query.all()
    return jsonify([{
        "id": d.id_dispositivo,
        "nombre": d.nombre_dispositivo,
        "tipo": d.tipo_dispositivo,
        "estado": d.estado,
        "ultima_conexion": d.ultima_conexion
    } for d in dispositivos])

@dispositivos_bp.route('/', methods=['POST'])
def crear_dispositivo():
    data = request.json
    nuevo_dispositivo = Dispositivo(
        id_hogar=data['id_hogar'],
        tipo_dispositivo=data['tipo_dispositivo'],
        nombre_dispositivo=data['nombre_dispositivo']
    )
    db.session.add(nuevo_dispositivo)
    db.session.commit()
    return jsonify({"mensaje": "Dispositivo creado"}), 201
