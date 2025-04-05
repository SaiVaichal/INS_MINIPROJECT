# sender.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load public key
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(public_key)

# Take user input
message = input("Enter message to send securely: ")
encrypted = cipher_rsa.encrypt(message.encode())

# Save to file
with open("encrypted_message.bin", "wb") as f:
    f.write(encrypted)

print("Message encrypted and saved to 'encrypted_message.bin'")
