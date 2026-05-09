from Crypto.PublicKey import RSA

server_key = RSA.generate(2048)
with open("server_private.pem", "wb") as f:
    f.write(server_key.export_key())
with open("server_cert.crt", "wb") as f:
    f.write(server_key.publickey().export_key())

    client_key = RSA.generate(2048)
    with open("client_private.pem", "wb") as f:
        f.write(client_key.export_key())
    with open("client_cert.crt", "wb") as f:
        f.write(client_key.publickey().export_key())

    print("Të gjitha certifikatat dhe çelësat u krijuan me sukses!")