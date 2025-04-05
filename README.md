# INS_MINIPROJECT

---

 Module Overviews

 Secure Data Storage (AES + MySQL)

- Encrypts user **names** using **AES symmetric encryption**.
- Stores encrypted data in a **MySQL** database (`secure_db`).
- On retrieval, the names are **decrypted** and displayed.
  
 *Data at rest is never in plain text.*

 2.  Secure Data Transmission (RSA)

- Uses **RSA public-private key encryption** to securely transmit messages.
- The **sender encrypts** the message with the receiver’s public key.
- The **receiver decrypts** it using their private key.

 *Ensures confidentiality over insecure channels.*

 3.  Digital Signature (RSA + SHA-256)

- The **sender hashes + signs** a message using their private key.
- The **receiver verifies** the message and the signature using the sender's public key.

 *Ensures data integrity and authentication.*

---

## Installation

Install required packages:

```bash
pip install pycryptodome mysql-connector-python
