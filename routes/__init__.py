from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

# Inicializar extensiones
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/mi_base_datos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'clave_secreta_super_segura'  # Cambia esto por algo más seguro
    
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    # Registrar blueprints aquí
    # ...

    return app
