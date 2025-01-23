from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=db.func.now())
    rol = db.Column(db.String(20), nullable=False, default='user') 

    def __repr__(self):
        return f'<Usuario {self.nombre}>'
    
class Hogar(db.Model):
    __tablename__ = 'hogares'
    id_hogar = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    nombre_hogar = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255))
    ciudad = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime, default=db.func.now())

class Consumo(db.Model):
    __tablename__ = 'consumos'
    id_consumo = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivos.id_dispositivo'))
    fecha_hora = db.Column(db.DateTime, default=db.func.now())
    consumo_kwh = db.Column(db.Float, nullable=False)

    dispositivo = db.relationship('Dispositivo', backref='consumos')
