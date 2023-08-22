#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth


app= Flask(__name__)
Auth = Auth()

@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not Auth.valid_login(email, password):
        abort(401)

    session_id = Auth.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response

@app.route('/sessions', methods=['DELETE'])
def logout():
    session_id = request.cookies.get('session_id')
    
    user = Auth.get_user_from_session_id(session_id)
    if user:
        Auth.destroy_session(user.id)
        return redirect('/', code=302)

    abort(403)

@app.route('/profile', methods=['GET'])
def profile():
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)

    user = Auth.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)

@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    email = request.form.get('email')

    try:
        # user = self._db.find_user_by(email=email)
        reset_token = Auth.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except NoResultFound:
        raise abort(403)

@app.route('/reset_password', methods=['PUT'])
def update_password():
    try:
        email = request.form.get('email')
        new_password = request.form.get('password')
        reset_token = request.form.get('reset_token')
    except KeyError:
        abort(403)
    try:
        Auth.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
