from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from .models import db
from .config import Config
from .routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(auth_bp)

    return app
