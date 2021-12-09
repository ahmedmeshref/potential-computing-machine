import rsa


def generateEncryptionKeys():
    publicKey, privateKey = rsa.newkeys(512)
    return publicKey, privateKey


def encryptText(message: str, publicKey: str) -> str:
    cipherText = rsa.encrypt(message.encode(), publicKey)
    return cipherText


def decryptText(cipherText: str, privateKey: str) -> str:
    try:
        message = rsa.decrypt(cipherText, privateKey).decode()
        return message
    except:
        return "Key is invalid"


pubKey, privKey = generateEncryptionKeys()
cipher = encryptText("Ahmed meshref is here", pubKey)
print(f"CipherText = {cipher}")
print(f"Decrypt ciphertext with invalid key: {decryptText(cipher, '1238912832198321')}")
print(f"Decrypt ciphertext with valid key: {decryptText(cipher, privKey)}")
