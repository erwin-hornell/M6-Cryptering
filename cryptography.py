import os
import hashlib
import vigenere
def generate_key(password: str, salt: bytes, iterations: int = 100_000, length: int = 32) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, dklen=length)

def xor_encrypt(data: str, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data.encode("utf-8"))])

def xor_decrypt(data: bytes, key: bytes) -> str:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)]).decode("utf-8")

def vigenère_encrypt(s: str, key: bytes) -> str:
    return vigenere.vigenereEncrypt(s, key)

def vigenère_decrypt(s: str, key: bytes) -> str:
    return vigenere.vigenereDecrypt(s, key)

def encrypt_text(s: str, key: bytes) -> bytes:
    return xor_encrypt(vigenère_encrypt(s, key.hex()), key)

def decrypt_text(s: bytes, key: bytes) -> str:
    return vigenère_decrypt(xor_decrypt(s, key), key.hex())

if __name__ == "__main__":
    pass
