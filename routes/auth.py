from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models import db, Usuario
from app import bcrypt

auth_bp = Blueprint('auth', __name__)

# Registro de usuarios
@auth_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.json
    correo = data['correo']
    nombre = data['nombre']
    contraseña = data['contraseña']
    
    # Verificar si el usuario ya existe
    if Usuario.query.filter_by(correo=correo).first():
        return jsonify({"mensaje": "El correo ya está registrado"}), 400
    
    # Crear un nuevo usuario
    hashed_password = bcrypt.generate_password_hash(contraseña).decode('utf-8')
    nuevo_usuario = Usuario(nombre=nombre, correo=correo, contraseña=hashed_password)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

# Inicio de sesión
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    correo = data['correo']
    contraseña = data['contraseña']
    
    usuario = Usuario.query.filter_by(correo=correo).first()
    if not usuario or not bcrypt.check_password_hash(usuario.contraseña, contraseña):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    # Crear un token de acceso
    token = create_access_token(identity=usuario.id_usuario)
    return jsonify({"token": token}), 200

# Ruta protegida de prueba
@auth_bp.route('/protegida', methods=['GET'])
@jwt_required()
def ruta_protegida():
    return jsonify({"mensaje": "Tienes acceso a esta ruta protegida"}), 200

@auth_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.json
    correo = data['correo']
    nombre = data['nombre']
    contraseña = data['contraseña']
    rol = data.get('rol', 'user')  # Asigna 'user' por defecto si no se proporciona un rol
    
    # Verificar si el usuario ya existe
    if Usuario.query.filter_by(correo=correo).first():
        return jsonify({"mensaje": "El correo ya está registrado"}), 400
    
    # Verificar si el rol es válido
    if rol not in ['user', 'admin']:
        return jsonify({"mensaje": "Rol inválido. Usa 'user' o 'admin'."}), 400
    
    # Crear un nuevo usuario
    hashed_password = bcrypt.generate_password_hash(contraseña).decode('utf-8')
    nuevo_usuario = Usuario(nombre=nombre, correo=correo, contraseña=hashed_password, rol=rol)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
