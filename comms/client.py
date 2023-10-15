import socket
from messages import MENSAJES

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'

# Whatever IP address you found from running ifconfig in terminal.
# SERVER = ""
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Officially connecting to the server.
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    mensaje = input()
    if mensaje == 'q':
        send(MENSAJES.DISCONNECT.value)
        break
    else:
        send(mensaje)