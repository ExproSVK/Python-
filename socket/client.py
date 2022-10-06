import client
import imp
import socket


from ClientConfig import ClientConfig

client_config = ClientConfig()



client_socket = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
client_socket.connect((client_config.server_ip_address, client_config.server_port))

client_socket.send("Hello!!!".encode())