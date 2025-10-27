import os
import hashlib

def generate_key(salt: str, password: str) -> str:

    return "salted password"
def cycled_key(s:str, key:str) -> str:
    #Returns a key the same length as the string s
    return key*(len(s)//len(key)) + key[0:len(s)%len(key)]

def xor_encrypt(s: str, key: str) -> bytes:
    key = cycled_key(s, key)
    bts = "".join(chr(ord(a)^ord(b)) for a, b in zip(s, key)).encode("utf-8")
    return bts

def xor_decrypt(s: bytes, key: str) -> str:
    pass

def vigenère_encrypt(s: str, key: str) -> str:
    pass

def vigenère_decrypt(s: str, key: str) -> str:
    pass

if __name__ == "__main__":
    key = "somekey"
    s = "short"
    print(s)
    print(xor_encrypt(s, key))
    print(xor_encrypt(s, key))