from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Load public key
with open("public_key.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Load message and signature
with open("message.txt", "rb") as f:
    message = f.read()

with open("signature.bin", "rb") as f:
    signature = f.read()

# Hash the message
hash_obj = SHA256.new(message)

# Verify signature
try:
    pkcs1_15.new(public_key).verify(hash_obj, signature)
    print(" Signature is valid. Message is authentic.")
    print(f" Message from sender: {message.decode()}")
except (ValueError, TypeError):
    print(" Signature is NOT valid. Message may be tampered.")
