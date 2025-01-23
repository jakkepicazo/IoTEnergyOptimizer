from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Registrar rutas
from routes.usuarios import usuarios_bp
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

if __name__ == '__main__':
    app.run(debug=True)

from routes.hogares import hogares_bp
from routes.dispositivos import dispositivos_bp

app.register_blueprint(hogares_bp, url_prefix='/hogares')
app.register_blueprint(dispositivos_bp, url_prefix='/dispositivos')

from routes.consumos import consumos_bp
app.register_blueprint(consumos_bp, url_prefix='/consumos')

from routes.auth import auth_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
