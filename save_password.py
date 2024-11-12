from encryption_utils import encrypt_password, load_key

def save_password(password, filename='passwords.txt', key=None):
    if key is None:
        key = load_key()
    encrypted_password = encrypt_password(password, key)
    with open(filename, 'ab') as file:
        file.write(encrypted_password + b'\n')
