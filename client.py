import socket
import threading

def main():
    """Main function to run the client."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 65432
    client_socket.connect((host, port))

    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print("Received from server:", response)

if __name__ == "__main__":
    main()