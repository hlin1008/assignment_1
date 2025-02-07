import cProfile
import threading
from server import start_server
from client import start_client

def network_program():
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    start_client()
    server_thread.join()

if __name__ == "__main__":
    cProfile.run("network_program()")