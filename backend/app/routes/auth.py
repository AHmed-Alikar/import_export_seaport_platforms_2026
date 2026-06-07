from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from app.models.user import db, User, Role

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/roles', methods=['POST'])
def create_role():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Debug logging
        
        if not data or not data.get("name"):
            print("Error: Role name required")  # Debug logging
            return jsonify({"error": "Role name required"}), 400

        # Check if role already exists
        existing_role = Role.query.filter_by(name=data['name']).first()
        if existing_role:
            print(f"Error: Role '{data['name']}' already exists")  # Debug logging
            return jsonify({"error": "Role already exists"}), 400

        role = Role(name=data['name'])
        db.session.add(role)
        db.session.commit()
        print(f"Role created successfully: {role.name} with ID: {role.id}")  # Debug logging
        return jsonify({"message": "Role created", "id": role.id}), 201
    
    except Exception as e:
        print(f"Error creating role: {str(e)}")  # Debug logging
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not all(k in data for k in ('username', 'password', 'role_id')):
        return jsonify({"error": "Missing fields"}), 400

    hashed_pw = generate_password_hash(data['password'])
    user = User(username=data['username'], password=hashed_pw, role_id=data['role_id'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "id": user.id}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({"token": token})
