import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def start_client():
    with open("client_private.pem", "rb") as f:
        client_private_key = RSA.import_key(f.read())

  
    with open("server_cert.crt", "rb") as f:
        server_public_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(server_public_key)

    
    user_input = input("Shkruaj mesazhin qe deshiron te dergosh te Serveri: ")
    message = user_input.encode()

  
    h = SHA256.new(message)
    signature = pkcs1_15.new(client_private_key).sign(h)

    encrypted_msg = cipher_rsa.encrypt(message)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))

    client_socket.send(signature)
    client_socket.send(encrypted_msg)

    print("\nMesazhi u nenshkrua, u kriptua dhe u dergua me sukses!")
    client_socket.close()


if __name__ == "__main__":
    start_client()
