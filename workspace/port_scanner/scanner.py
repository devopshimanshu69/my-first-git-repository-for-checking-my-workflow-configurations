import threading 
import socket 
import datetime 

target_host = "127.0.0.1" 

def scan_port(port):
# setting up connection 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_host, port)) # updated to use the function's port
    if result == 0: 
        print(f" --> success! Port {port} is open.")
    s.close()

# 2. Add the threading loop 
if __name__ == "__main__":
    print(f"trying network path : {target_host}")
    
    threads = []
    # create the loop to target all the ports at once 
    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()
        
    # join the threads 
    for t in threads:
        t.join()

