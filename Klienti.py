import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def start_client():
    # 1. Lexo celesin privat te klientit per te nenshkruar mesazhin
    with open("client_private.pem", "rb") as f:
        client_private_key = RSA.import_key(f.read())


if __name__ == "__main__":
    start_client()
