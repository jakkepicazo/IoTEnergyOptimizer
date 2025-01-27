from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(200))
    
    hogares = db.relationship('Hogar', backref='usuario', lazy=True)
    dispositivos = db.relationship('UsuariosDispositivos', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

class Hogar(db.Model):
    __tablename__ = 'hogares'
    id_hogar = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    nombre_hogar = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))
    ciudad = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime, default=db.func.now())

    dispositivos = db.relationship('Dispositivo', backref='hogar', lazy=True)

class Dispositivo(db.Model):
    __tablename__ = 'dispositivos'
    id_dispositivo = db.Column(db.Integer, primary_key=True)
    id_hogar = db.Column(db.Integer, db.ForeignKey('hogares.id_hogar'))
    nombre_dispositivo = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))

    sensores = db.relationship('Sensor', backref='dispositivo', lazy=True)
    consumos = db.relationship('Consumo', backref='dispositivo', lazy=True)
    alertas = db.relationship('Alerta', backref='dispositivo', lazy=True)
    configuraciones = db.relationship('Configuracion', backref='dispositivo', lazy=True)

class Sensor(db.Model):
    __tablename__ = 'sensores'
    id_sensor = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivos.id_dispositivo'))
    tipo_sensor = db.Column(db.String(50))
    valor = db.Column(db.String(50))

class Consumo(db.Model):
    __tablename__ = 'consumo'
    id_consumo = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivos.id_dispositivo'))
    fecha = db.Column(db.Date)
    consumo_kwh = db.Column(db.Float, nullable=False)

class Alerta(db.Model):
    __tablename__ = 'alertas'
    id_alerta = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivos.id_dispositivo'))
    tipo_alerta = db.Column(db.String(100))
    mensaje = db.Column(db.Text)
    fecha_alerta = db.Column(db.Date)

class Configuracion(db.Model):
    __tablename__ = 'configuraciones'
    id_configuracion = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivos.id_dispositivo'))
    configuracion = db.Column(db.String(100))
    valor = db.Column(db.String(50))

class UsuariosDispositivos(db.Model):
    __tablename__ = 'usuarios_dispositivos'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivos.id_dispositivo'), primary_key=True)
