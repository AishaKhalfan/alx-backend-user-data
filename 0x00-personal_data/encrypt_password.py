#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    '''returns a salted, hashed password, which is a byte string'''
    pswd_encoded = password.encode()
    pswd_hashed = bcrypt.hashpw(pswd_encoded, bcrypt.gensalt())
    return pswd_hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Check valid password'''
    pass_encoded = password.encode()
    hashed_password = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())
    if bcrypt.checkpw(pass_encoded, hashed_password):
        return True
    return False
