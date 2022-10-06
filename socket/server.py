from concurrent.futures import thread
from http import client, server
import socket
import threading
from ServerConfig import ServerConfig

def handle_client(pa_client_socket, pa_client_address):
    #while(True):
        data = pa_client_socket.recv(1500)
        print(data)
    #pass

server_config = ServerConfig()
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((server_config.ip_address, server_config.port))
server_socket.listen(10)

print(f"Server is running on IP {server_config.ip_address}, {server_config.port}")

while(True):
    (client_socket, client_address) = server_socket.accept()
    thread = threading.Thread(target=handle_client, args= (client_socket, client_address))
    thread.start()