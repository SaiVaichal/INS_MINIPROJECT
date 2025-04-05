import mysql.connector
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64
from Crypto.Random import get_random_bytes
import os


KEY_FILE = "aes_key.key"


if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(get_random_bytes(16))  


with open(KEY_FILE, "rb") as f:
    key = f.read()



key = os.urandom(32)  


def encrypt_data(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_bytes).decode()


def decrypt_data(encrypted_text, key):
    encrypted_bytes = base64.b64decode(encrypted_text)
    iv = encrypted_bytes[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes[16:]), AES.block_size)
    return decrypted_bytes.decode()

conn = mysql.connector.connect(
    host="localhost",     
    user="root", 
    password="Nigeria@123", 
    database="secure_db"
)
cursor = conn.cursor()


def insert_user(name, age):
    encrypted_name = encrypt_data(name, key) 
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (encrypted_name, age))
    conn.commit()
    print("User added successfully!")

# Retrieve and decrypt data from MySQL
def fetch_users():
    cursor.execute("SELECT id, name, age FROM users")
    for row in cursor.fetchall():
        decrypted_name = decrypt_data(row[1], key)  
        print(f"ID: {row[0]}, Name: {decrypted_name}, Age: {row[2]}")


while True:
    name = input("Enter name (or type 'exit' to stop): ")
    if name.lower() == "exit":
        break  

    age = input("Enter age: ")

    insert_user(name, int(age))  

print("\n Stored users (decrypted):")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    decrypted_name = decrypt_data(row[1], key)
    print(f"ID: {row[0]}, Name: {decrypted_name}, Age: {row[2]}")




cursor.close()
conn.close()
