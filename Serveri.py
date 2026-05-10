import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def start_server():
    with open("server_private.pem", "rb") as f:
        server_private_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(server_private_key)

    with open("client_cert.crt", "rb") as f:
        client_public_key = RSA.import_key(f.read())

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Serveri TCP po pret në portën 12345...")

    conn, addr = server_socket.accept()
    print(f"Lidhja u pranua nga: {addr}")
