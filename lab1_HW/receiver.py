# receiver.py
import socket
from cipher_module import caesar_decipher

def receiver():
    host = '192.168.0.105'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(1)
    print("Receiver waiting for connection...")
    conn, addr = s.accept()
    print("Receiver connected to", addr)

    encrypted_message = conn.recv(1024).decode()

    print("Received Encrypted Message:", encrypted_message)

    key = 3
    decrypted_message = caesar_decipher(encrypted_message, key)

    print("DECRYPTION")
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

    conn.close()
    s.close()

if __name__ == "__main__":
    receiver()
