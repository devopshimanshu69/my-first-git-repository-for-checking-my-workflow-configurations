
import socket
import datetime 
# define the target and port
target_host = "127.0.0.1"
target_port = 80
print (f"trying network path : {target_host} on port {target_port}")
# make a socket object for the connection attempt (AF_INET = IPV4 , socket.SOCK_STREAM = TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set a timeout for the script to keep moving even if the port is closed 
s.settimeout(1)
# connect to the port using connect_ex function for getting 0 when connected or error code instead of some random error when the connection fails or the port is closed
# define the output as result
result = s.connect_ex((target_host, target_port))

if result == 0 :
    print(f" -->  success! Port {target_port} is open .")
else:
    print(f"--> error : Port is closed ")
# clean up and close the connection 
s.close()
