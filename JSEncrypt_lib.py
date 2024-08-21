import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode

def encrypt_data(input_data):
    # Define the public key in PEM format
    public_key_pem = (
        "-----BEGIN PUBLIC KEY-----\n"
        <public key>
        "-----END PUBLIC KEY-----"
    )

    # Load the public key
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_v1_5.new(public_key)

    # Encrypt the data
    encrypted_data = cipher.encrypt(input_data.encode('utf-8'))

    # Encode encrypted data to base64
    encrypted_data_b64 = b64encode(encrypted_data).decode('utf-8')

    return encrypted_data_b64

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python enn.py <data>")
        sys.exit(1)
    
    plaintext = sys.argv[1]
    
    encrypted_message = encrypt_data(plaintext)
    print(encrypted_message, end="")
