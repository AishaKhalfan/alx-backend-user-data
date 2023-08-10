import bcrypt

def hash_password(password: str) -> bytes:
    '''returns a salted, hashed password, which is a byte string'''
    pswd_encoded = password.encode()
    pswd_hashed = bcrypt.hashpw(pswd.encoded, bcrypt.gensalt())
    return pswd_hashed
