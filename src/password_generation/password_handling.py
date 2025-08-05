import gnupg
import os

gpg = gnupg.GPG(gnupghome = os.path.expanduser('~/.gnupg'))
gpg.encoding = 'utf-8'

def encrypt_password(password):
    encrypted_password = gpg.encrypt(password, symmetric=True, recipients = 'alice@gmail.com', passphrase='your-password')

    return encrypted_password

def decrypt_password(password):
    decrypted_password = gpg.decrypt(password, passphrase='your-password')

    return decrypted_password