import socket
import threading

def handle_client(client_socket):
    
        while True:
                 data = client_socket.recv(1024)
                 if not data:
                    break
                 message = data.decode('utf-8')
                 print(f"Received message: {message}")
                 response = "Server received your message: " + message
                 client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

def main():
    """Starts the TCP server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 65432    
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow up to 5 connections in the queu
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print("Accepted connection from:", addr)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()