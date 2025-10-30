def charToAscii(l: list[str]) -> list[int]: # converts chars to ascii value
    asciiList = []
    for char in l:
        asciiList.append(ord(char))
    return asciiList

def asciiToChar(l: list[int]) -> list[str]: # converts ascii value to chars
    charList = []
    for char in l:
        charList.append(chr(char))
    return charList

def asciiSum(l1: list[int], l2: list[int]) -> list[int]:
    sumAscii = [] # declare empty list sumAscii
    for n in range(len(l1)): # repeat until entire text L1 has been encrypted by key L2
        i = n % len(l2) # password "repeats" if shorter than text
        n1 = int(l1[n])
        n2 = int(l2[i])
        ascii = ((n1 + n2) % 256)
        sumAscii.append(ascii) # add summed integer to list sumAscii
    return sumAscii


def vigenereEncrypt(text: str, key: str) -> str : #Input: text, key | return: text encrypted by key
    textAscii = charToAscii(list(text))
    keyAscii = charToAscii(list(key))
    encryptedText = asciiSum(textAscii, keyAscii)
    encryptedText = asciiToChar(encryptedText)
    return ''.join(encryptedText)

def vigenereDecrypt(text: str, key: str) -> str : #Input: text, key | return: text decrypted by key
    textAscii = charToAscii(list(text))
    keyAscii = charToAscii(list(key))
    for n in range(len(keyAscii)):
        keyAscii[n] = -keyAscii[n]
        keyAscii[n] = str(keyAscii[n])
    decryptedText = asciiSum(textAscii, keyAscii)
    decryptedText = asciiToChar(decryptedText)
    return ''.join(decryptedText)
    

# test of functions vigenereEncrypt and vigenereDecrypt
if __name__ == "__main__":
    message = "Hemlig mening hemlig mening hemlig mening hemlig mening."
    password = "jfiod5u4tJAOSPvn59"
    textEncrypted = vigenereEncrypt(message, password)
    print(textEncrypted)
    print()

    textDecrypted = vigenereDecrypt(textEncrypted, password)
    print(textDecrypted)
    print()

    failDecrypt = vigenereDecrypt(textEncrypted, "test1234")
    print(failDecrypt)