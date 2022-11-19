import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")

from cryptography.fernet import Fernet

def encrypt(message: bytes) -> bytes:
    return Fernet(SECRET_KEY.encode()).encrypt(message)

def decrypt(token: bytes) -> bytes:
    return Fernet(SECRET_KEY.encode()).decrypt(token)