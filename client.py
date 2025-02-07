import socket
import time

def start_client():
    time.sleep(1)  # Ensure server is running
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))
    client_socket.sendall(b"Hello, Server!")
    client_socket.close()

if __name__ == "__main__":
    start_client()