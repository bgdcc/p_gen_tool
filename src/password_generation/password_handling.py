import gnupg
import os
import dotenv

dotenv.load_dotenv(dotenv_path=os.path.expanduser("~/p_gen_tool/.env"))
master_password = str(os.getenv("MASTER_PASSWORD"))

gpg = gnupg.GPG(gnupghome = os.path.expanduser('~/.gnupg'))
gpg.encoding = 'utf-8'

def encrypt_password(password):
    encrypted_password = gpg.encrypt(password, symmetric=True, recipients = 'alice@gmail.com', passphrase=master_password)

    return encrypted_password

def decrypt_password(password, pw_attempt):
    decrypted_password = gpg.decrypt(password, passphrase=pw_attempt)

    return decrypted_password