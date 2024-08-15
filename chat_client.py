import socket
import threading

# Client settings
HOST = '127.0.0.1'  # Server's IP address
PORT = 12345        # Server's port

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"{message}")
        except:
            print("[ERROR] Connection closed.")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input()
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print("[ERROR] Connection closed.")
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()
