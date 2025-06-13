import socket
import os
import subprocess
from threading import Thread

def lidar_com_cliente(cliente_socket):
    header = cliente_socket.recv(1024).decode()
    nome_arquivo, tamanho = header.split('|')
    cliente_socket.sendall(b"OK")

    caminho_salvo = os.path.join("/tmp", nome_arquivo)
    with open(caminho_salvo, 'wb') as f:
        bytes_recebidos = 0
        while bytes_recebidos < int(tamanho):
            chunk = cliente_socket.recv(4096)
            if not chunk:
                break
            f.write(chunk)
            bytes_recebidos += len(chunk)

    subprocess.run(["./backup_exec", caminho_salvo])  # executável C++

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind(('0.0.0.0', 9000))
        servidor.listen()

        print("Servidor ouvindo na porta 9000...")
        while True:
            cliente, _ = servidor.accept()
            Thread(target=lidar_com_cliente, args=(cliente,)).start()

iniciar_servidor()
