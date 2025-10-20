import os
import hashlib

def generate_key(salt: str, password: str) -> str:

    return "salted password"
def cycled_key(s:str, key:str) -> str:
    return key*(len(s)//len(key)) + key[0:len(s)%len(key)]

def xor_encrypt(s: str, key: str) -> bytes:
    bts = [(a^b) for a, b in zip(s, key)]
    return bts

def xor_decrypt(s: str, key: str) -> bytes:
    pass

def vigenère_encrypt(s: str, key: str) -> str:
    pass

def vigenère_decrypt(s: str, key: str) -> str:
    pass

if __name__ == "__main__":
    key = "somekey"
    s = "short"
    print(s)
    print(cycled_key(s, key))