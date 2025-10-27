import os
import hashlib

def generate_key(password: str, salt: bytes, iterations: int = 100_000, length: int = 32) -> str:
    key_bytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, dklen=length)
    return key_bytes.hex()

def cycled_key(s:str, key:str) -> str:
    #Returns a key the same length as the string s
    return key*(len(s)//len(key)) + key[0:len(s)%len(key)]

def xor_encrypt(s: str, key: str) -> bytes:
    return "".join(chr(ord(c)^ord(key[i % len(key)])) for i, c in enumerate(s)).encode("utf-8")

def xor_decrypt(s: bytes, key: str) -> str:
    return "".join(chr(ord(c)^ord(key[i % len(key)])) for i, c in enumerate(s.decode("utf-8")))

def vigenère_encrypt(s: str, key: str) -> str:
    pass

def vigenère_decrypt(s: str, key: str) -> str:
    pass

if __name__ == "__main__":
    salt = os.urandom(8)
    key = generate_key("123", salt)
    print(salt, key)
    s = "short text"
    print(s)
    s = xor_encrypt(s, key)
    print(s)
    s = xor_decrypt(s, key)
    print(s)
