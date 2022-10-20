from argparse import Action
from cgitb import text
import json
from msilib.schema import Media
import socket

import ClientConfig
from MessageModel import MessageModel
from ActionEnum import ActionEnum

def menu(): 
    print("****MENU****")
    print("EXIT PROGRAM (1)")
    print("SHOW USERS (2)")
    print("SEND MESSAGE (3)")

    pass

client_config = ClientConfig.ClientConfig()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_config.server_ip_address, client_config.server_port))

print("Wellcome")
user_name = input("Enter your nick: ")

msg = MessageModel(user_name, "", "", ActionEnum.LOGIN )
json_str = json.dumps(msg.__dict__)
client_socket.send(json_str.encode())


while(True):
    
    action = input("Choose operation from the menu: ")
    match action:
        case "3":
            msg = MessageModel(user_name, "", "", ActionEnum.EXIT)
            json_str = json.dumps(msg,__dict__)
            client_socket.send(json_str.encode())
            client_socket.close()
            exit(0)
        case "2":
            msg = MessageModel(user_name, "", "", ActionEnum.USERS)
            json_str = json.dumps(msg,__dict__)
            client_socket.send(json_str.encode())
            data = client_socket.recv(1500)
            msg = json.loads(data.decode(), object_hook=MessageModel.from_json)
            print(f"USER LIST: {msg.text}")
            continue
        case "3":
            msg = input("Message: ")
            to_user = input("To user: ")
            msg = MessageModel(user_name, to_user, msg , ActionEnum.EXIT)
            json_str = json.dumps(msg,__dict__)
            client_socket.send(json_str.encode())
