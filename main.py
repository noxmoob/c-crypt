import os
import pyaes
import hashlib

passphrase = input('enter the pass key: ')

key = hashlib.sha256(passphrase.encode('utf-8')).digest()

# Use the key for AES in CTR mode
aes = pyaes.AESModeOfOperationCTR(key)

# Encrypt the data
plaintext = b'test'
result = aes.encrypt(plaintext)

print(result)
