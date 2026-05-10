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
   
   signature = conn.recv(256)
    encrypted_msg = conn.recv(1024)

    try:

        decrypted_msg = cipher_rsa.decrypt(encrypted_msg)
        print(f"Mesazhi u dekriptua me sukses!")

        h = SHA256.new(decrypted_msg)
        pkcs1_15.new(client_public_key).verify(h, signature)
        print("Verifikimi i Nënshkrimit: SUKSES (Mesazhi është i vërtetë dhe i paprekur)!")
        print(f"Përmbajtja e mesazhit: {decrypted_msg.decode()}")

    except (ValueError, TypeError):
        print("ALARM: Verifikimi dështoi! Mesazhi ose nënshkrimi mund të jenë manipuluar.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()