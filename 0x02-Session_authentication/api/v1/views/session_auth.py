#!/usr/bin/env python3
""" Module of Authorization Session views
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - the status of the API
    """
    email = request.form.get("email")
    if not email:
        return make_response(jsonify({"error": "email missing"}), 400)

    password = request.form.get("password")
    if not password:
        return make_response(jsonify({"error": "password missing"}), 400)

    existing_user = User.search({"email": email})
    if len(existing_user) == 0:
        return make_response(jsonify({"error": "no user found for this email"}), 404)

    from api.v1.app import auth
    for user in existing_user:
        if (user.is_valid_password(password)):
            session_id = auth.create_session(user.id)
            SESSION_NAME = getenv('SESSION_NAME')
            response = make_response(user.to_json())
            response.set_cookie(SESSION_NAME, session_id)
            return response

    return make_response(jsonify({"error": "wrong password"}), 401)
