# sender.py
import socket
from cipher_module import caesar_cipher

def sender():
    host = '192.168.0.105'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print("Sender Connected to", host)

    print("Enter message to be encrypted:")
    message = input()

    key = 3
    encrypted_message = caesar_cipher(message, key)

    print("ENCRYPTION")
    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)

    s.send(encrypted_message.encode())
    s.close()

if __name__ == "__main__":
    sender()
