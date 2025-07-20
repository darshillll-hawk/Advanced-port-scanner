import socket
import threading
from queue import Queue
import datetime

# Target and Port Range
target = input("Enter the target IP or domain: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))
timeout = 0.5

# Thread-safe Queue
queue = Queue()

# Save results to file
results_file = open("results.txt", "w")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        conn = s.connect_ex((target, port))
        if conn == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            result = f"[+] Port {port} is OPEN | Service: {service}"
            print(result)
            results_file.write(result + "\n")
        s.close()
    except Exception as e:
        pass

def threader():
    while True:
        port = queue.get()
        scan_port(port)
        queue.task_done()

# Start Timer
start_time = datetime.datetime.now()
print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

# Create threads
for x in range(100):  # 100 threads
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# Fill the queue
for port in range(start_port, end_port + 1):
    queue.put(port)

queue.join()
end_time = datetime.datetime.now()
print(f"\nScan completed in: {end_time - start_time}")
results_file.write(f"\nScan completed in: {end_time - start_time}\n")
results_file.close()
