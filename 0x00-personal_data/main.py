#!/usr/bin/env python3
"""
Password encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted password which is a string byte """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ The code checks if the provided password matches the hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
