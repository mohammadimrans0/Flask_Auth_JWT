import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'flask-jwt-secret-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'flask-jwt-jwt-secret')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
