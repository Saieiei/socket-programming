import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "192.168.0.105"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def send(msg):
    try:
        if msg == DISCONNECT_MESSAGE:
            client.send(DISCONNECT_MESSAGE.encode(FORMAT))
            client.close()
        else:
            message = msg.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
    except Exception as e:
        print(f"Error: {e}")

try:
    while True:
        user_input = input("Enter message (type '!DISCONNECT' to exit): ")
        send(user_input)
        if user_input == DISCONNECT_MESSAGE:
            break
except KeyboardInterrupt:
    pass
finally:
    client.close()
    print("Disconnected.")
