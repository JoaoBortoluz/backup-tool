import socket
import os

def enviar_arquivo(path, host='127.0.0.1', porta=9000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((host, porta))

        nome_arquivo = os.path.basename(path)
        tamanho = os.path.getsize(path)

        cliente.sendall(f"{nome_arquivo}|{tamanho}".encode())
        ack = cliente.recv(2)

        with open(path, 'rb') as f:
            while chunk := f.read(4096):
                cliente.sendall(chunk)

        print("Arquivo enviado com sucesso")

# Exemplo: enviar 'test.txt'
enviar_arquivo('test.txt')
