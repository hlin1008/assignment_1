import tracemalloc
import threading
from server import start_server
from client import start_client

def network_program():
    tracemalloc.start()  # Start memory tracking

    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    start_client()
    server_thread.join()

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[Top 10 memory-consuming lines]")
    for stat in top_stats[:10]:
        print(stat)

if __name__ == "__main__":
    network_program()