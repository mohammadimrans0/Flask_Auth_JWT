from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required,
    get_jwt_identity
)
from datetime import datetime
from .models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return "Hello, Flask!"

# Register a new user
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    if not all(key in data for key in ('username', 'email', 'full_name', 'password')):
        return jsonify({"msg": "Missing required fields"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 400

    try:
        date_of_birth = datetime.strptime(data['date_of_birth'], "%Y-%m-%d").date() if data.get('date_of_birth') else None
    except ValueError:
        return jsonify({"msg": "Invalid date format. Use YYYY-MM-DD."}), 400

    user = User(
        username=data['username'],
        email=data['email'],
        full_name=data['full_name'],
        address=data.get('address'),
        date_of_birth=date_of_birth
    )
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201

# Login a user
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

# Authenticated profile route
@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))

    if not user:
        return jsonify({"msg": "User not found"}), 404

    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "date_of_birth": user.date_of_birth.isoformat() if user.date_of_birth else None,
        "address": user.address
    }

    return jsonify(user_data), 200
