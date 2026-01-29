from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

from extensions import mongo
from utils.security import hash_password, verify_password
from utils.jwt_helper import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    mongo.db.users.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password_hash": hash_password(data["password"])
    })

    return jsonify({"message": "User registered"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = mongo.db.users.find_one({"email": data["email"]})

    if not user or not verify_password(data["password"], user["password_hash"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user["_id"])
    return jsonify({"access_token": token})


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    return jsonify({
        "name": user["name"],
        "email": user["email"]
    })


@auth_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Logout success (mocked)"})
