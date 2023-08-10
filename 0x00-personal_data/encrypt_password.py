import bcrypt
# password = b"super secret password"

def hash_password(password: str):
    '''returns a salted, hashed password, which is a byte string'''
    password = b""
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
    if bcrypt.checkpw(password, hashed):
        return hashed
