from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save public key (to share with receiver)
with open("public_key.pem", "wb") as f:
    f.write(public_key)

# Save private key (keep securely, not shared)
with open("private_key.pem", "wb") as f:
    f.write(private_key)

# Get message input from user
message = input("Enter a message to sign: ").encode()

# Hash the message
hash_obj = SHA256.new(message)

# Sign the message using the private key
signature = pkcs1_15.new(key).sign(hash_obj)

# Save message and signature to files
with open("message.txt", "wb") as f:
    f.write(message)

with open("signature.bin", "wb") as f:
    f.write(signature)

print("\n Message signed and saved to 'message.txt' and 'signature.bin'.")
