import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def start_client():
    # 1. Lexo celesin privat te klientit per te nenshkruar mesazhin
    with open("client_private.pem", "rb") as f:
        client_private_key = RSA.import_key(f.read())

    # 2. Lexo certifikaten e serverit (X.509) per te kriptuar mesazhin
    with open("server_cert.crt", "rb") as f:
        server_public_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(server_public_key)

    # Merr mesazhin nga tastiera (perdoruesi e shkruan vete)
    user_input = input("Shkruaj mesazhin qe deshiron te dergosh te Serveri: ")
    message = user_input.encode()

    # 3. Krijimi i Nenshkrimit Digjital (Digital Signature)
    h = SHA256.new(message)
    signature = pkcs1_15.new(client_private_key).sign(h)

    # 4. Kriptimi i mesazhit
    encrypted_msg = cipher_rsa.encrypt(message)


if __name__ == "__main__":
    start_client()
