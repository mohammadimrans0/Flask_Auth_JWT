from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt = JWTManager(app)

    from .routes import auth_bp
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()
    
    return app
