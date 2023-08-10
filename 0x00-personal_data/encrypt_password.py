import bcrypt
# password = b"super secret password"

def hash_password(password: str):
    '''returns a salted, hashed password, which is a byte string'''
    # password = b""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
