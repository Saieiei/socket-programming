import socket
import threading

HEADER=64 #header is the first message sent by the client, it tells the length of the message
FORMAT='utf-8' #encoding format
DISCONNECT_MESSAGE="!DISCONNECT" #disconnect message
PORT=5050
#SERVER="192.168.0.105" #ur laptop ip
SERVER=socket.gethostbyname(socket.gethostname())
#print(SERVER) #ur laptop ip
#print(socket.gethostname()) #ur laptop name
ADDR=(SERVER,PORT) #binding the address with the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is ipv4 and SOCK_STREAM is tcp(different types of protocols/streaming data)
server.bind(ADDR) #binding the address with the socket

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    try:
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                if msg_length == DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[{addr}] Disconnect message received.")
                else:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    print(f"[{addr}] {msg}")
                    conn.send("Msg received".encode(FORMAT))
    except ConnectionAbortedError:
        print(f"[{addr}] Connection aborted by client.")
    finally:
        conn.close()
        print(f"[{addr}] Connection closed.")




def start(): #starting the server
    server.listen() #listening for connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept() #accepting the connection, cpnnection and address
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}") #active connections, -1 because the start() is also a thread

print("[STARTING] server is starting...")
start()