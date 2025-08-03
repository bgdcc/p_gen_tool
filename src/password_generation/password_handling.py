import gnupg
import os

def encrypt_password(password):
    gpg = gnupg.GPG(gnupghome = os.path.expanduser('~/.gnupg'))
    gpg.encoding = 'utf-8'

    encrypted_password = gpg.encrypt(password, symmetric=True, recipients = 'alice@gmail.com', passphrase='your-password')

    return encrypted_password