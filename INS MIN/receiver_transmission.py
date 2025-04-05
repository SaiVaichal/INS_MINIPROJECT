# receiver.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Generate RSA key pair if not exists
def generate_keys():
    if not os.path.exists("private.pem") or not os.path.exists("public.pem"):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open("private.pem", "wb") as prv_file:
            prv_file.write(private_key)
        with open("public.pem", "wb") as pub_file:
            pub_file.write(public_key)
        print("RSA key pair generated.")
    else:
        print("Key pair already exists.")

# Decrypt message
def decrypt_message():
    with open("encrypted_message.bin", "rb") as f:
        encrypted_message = f.read()

    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted = cipher_rsa.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted.decode())

if __name__ == "__main__":
    generate_keys()
    decrypt_message()
