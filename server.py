import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(1)
    print("Server listening on port 9999...")

    conn, addr = server_socket.accept()
    data = conn.recv(1024)
    print("Received:", data.decode())
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()