from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename='secret.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password
