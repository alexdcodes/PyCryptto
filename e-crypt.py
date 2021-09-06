from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('alexdiker.csv', 'rb') as file:
    original = file.read()

e = fernet.encrypt(original)

with open('nba.csv', 'wb') as e_file:
    e_file.write(e)

fernet = Fernet(key)

with open('alexdiker.csv', 'rb') as enc_file:
    e = enc_file.read()

d = fernet.decrypt(e)

with open('alexdiker.csv', 'wb') as dec_file:
    dec_file.write(d)