from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import Config
import os

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Crear la carpeta instance si no existe
    instance_path = os.path.join(app.root_path, 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)

    db.init_app(app)
    csrf.init_app(app)

    # Importa las rutas aquí para evitar la importación circular
    from app.routes import init_routes
    init_routes(app)

    @app.context_processor
    def inject_user():
        from app.models import User
        return dict(User=User)

    return app
