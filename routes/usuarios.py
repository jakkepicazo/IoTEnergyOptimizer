from flask import Blueprint, jsonify, request
from models import db, Usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id_usuario, "nombre": u.nombre, "email": u.email} for u in usuarios])

@usuarios_bp.route('/', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado"}), 201

@app.route('/usuario/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)  # Obtener el usuario por su ID
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.correo = request.form['correo']
        usuario.rol = request.form['rol']
        db.session.commit()  # Guardar los cambios en la base de datos
        return redirect(url_for('mostrar_usuarios'))  # Redirigir a la lista de usuarios
    return render_template('editar_usuario.html', usuario=usuario)

@app.route('/usuarios')
def mostrar_usuarios():
    usuarios = Usuario.query.all()  # Obtener todos los usuarios
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/usuario/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)  # Buscar el usuario por ID
    db.session.delete(usuario)  # Eliminar el usuario
    db.session.commit()  # Confirmar el cambio en la base de datos
    return redirect(url_for('mostrar_usuarios'))  # Redirigir a la lista de usuarios
