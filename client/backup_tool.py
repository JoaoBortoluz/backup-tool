#!/usr/bin/env python3

import socket
import os
import time
import argparse
import pathlib

# atitus: 10.1.25.70
HOST = "192.168.0.11"
PORT = 9000


def send_file(path: pathlib.Path, base_dir: pathlib.Path):
    if not path.is_file():
        print(f"[!] Skipped: {path} is not a file.")
        return

    relative_path = str(path.relative_to(base_dir))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        size = path.stat().st_size
        header = f"{relative_path}|{size}"
        client.sendall(header.encode())

        # espera pelo Ok
        client.recv(2)

        print(f"[→] Sending: {relative_path}")
        with open(path, "rb") as f:
            while chunk := f.read(4096):
                client.sendall(chunk)

                # TESTE atrasa o envio para testar a distribuição do sistema
                time.sleep(0.01)  # simula 100kb/s velocidade de envio
                # TESTE

        print(f"[✓] Sent: {relative_path}")


def process_send(path):
    resolved_path = pathlib.Path(path).expanduser().resolve()

    if resolved_path.is_file():
        base_dir = resolved_path.parent
        send_file(resolved_path, base_dir)

    elif resolved_path.is_dir():
        base_dir = resolved_path
        for item in resolved_path.rglob("*"):
            if item.is_file():
                send_file(item, base_dir)
    else:
        print(f"[!] Invalid path: {resolved_path}")


def main():
    parser = argparse.ArgumentParser(
        prog="backup-tool",
        description="Backup client for sending files and directories.",
    )
    parser.add_argument("command", choices=["send"], help="Command to execute")
    parser.add_argument("path", help="File or directory path to send")

    args = parser.parse_args()

    if args.command == "send":
        process_send(args.path)


if __name__ == "__main__":
    main()
