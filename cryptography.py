import os
import hashlib

def generate_key(password: str, salt: bytes, iterations: int = 100_000, length: int = 32) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, dklen=length)
    



def xor_encrypt(data: str, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data.encode("utf-8"))])

def xor_decrypt(data: bytes, key: bytes) -> str:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)]).decode("utf-8")

def vigenère_encrypt(s: str, key: bytes) -> str:
    return f"vigenère_encrypt: {s}"

def vigenère_decrypt(s: str, key: bytes) -> str:
    return s.replace("vigenère_encrypt: ", "")

def encrypt_text(s: str, key: bytes) -> bytes:
    return xor_encrypt(vigenère_encrypt(s, key), key)

def decrypt_text(s: bytes, key: bytes) -> str:
    return vigenère_decrypt(xor_decrypt(s, key), key)

if __name__ == "__main__":
    salt = os.urandom(8)
    key = generate_key("123", salt)
    print(salt, key)
    s = "short text"
    print(s)
    s = encrypt_text(s, key)
    print(s)
    s = decrypt_text(s, key)
    print(s)
