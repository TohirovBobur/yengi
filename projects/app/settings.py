from time import time_ns
import bcrypt


def generate_id():
    return str(time_ns())


def encode_password(raw_password: str):
    encoded_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt(4)
    return bcrypt.hashpw(encoded_password, salt)


