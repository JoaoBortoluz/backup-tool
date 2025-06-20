import socket
import os
import subprocess
import multiprocessing

QUEUE = multiprocessing.JoinableQueue()
NUM_WORKERS = 4
CLIENT_COUNTER = multiprocessing.Value("i", 0)
PORT = 9000


def worker(queue):
    while True:
        path = queue.get()
        if path is None:
            break
        subprocess.run(["./backup_exec", path])
        print(f"[✓] Backup completed: {path}", flush=True)
        queue.task_done()


def handle_client(client_socket, queue, client_id):
    try:
        header = client_socket.recv(1024).decode()
        relative_name, size = header.split("|")
        client_socket.sendall(b"OK")

        print(f"[+] ({client_id}) Receiving file: {relative_name}", flush=True)

        saved_path = os.path.join("/tmp", relative_name)
        os.makedirs(os.path.dirname(saved_path), exist_ok=True)

        with open(saved_path, "wb") as f:
            received = 0
            while received < int(size):
                chunk = client_socket.recv(4096)
                if not chunk:
                    break
                f.write(chunk)
                received += len(chunk)

        print(
            f"[✓] ({client_id}) File {relative_name} received successfully.", flush=True
        )
        queue.put(saved_path)

    except Exception as e:
        print(f"[!] ({client_id}) Error handling client: {e}", flush=True)


def start_server():
    # IMPORTANTE - separa os arquivos enviados em multiprocessos,
    # criando distribuição no servidor
    for _ in range(NUM_WORKERS):
        multiprocessing.Process(target=worker, args=(QUEUE,), daemon=True).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("0.0.0.0", PORT))
        server.listen()
        print(
            f"[~] Server listening on port {PORT} with {
                NUM_WORKERS
            } worker processes...",
            flush=True,
        )

        while True:
            client, _ = server.accept()

            with CLIENT_COUNTER.get_lock():
                CLIENT_COUNTER.value += 1
                client_id = CLIENT_COUNTER.value

            multiprocessing.Process(
                target=handle_client, args=(client, QUEUE, client_id), daemon=True
            ).start()


if __name__ == "__main__":
    start_server()
