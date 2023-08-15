#!/usr/bin/env python3
""" Module of Authorization Session views
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User



@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - the status of the API
    """
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if not password:
        return jsonify({"error": "password missing"}),400

    existing_user = User.search({"email": email})
    if len(existing_user) == 0:
        return jsonify({"error": "no user found for this email" }), 404

    if not User.is_valid_password(password):
        return jsonify({ "error": "wrong password" })

    from api.v1.app import auth
    session_id = self.auth.create_session(user_id)

    return User.to_json(session_id)
