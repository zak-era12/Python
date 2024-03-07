#p8-Write a Python program to create server-client and exchange basic information
'''
The server and the client communicate using the socket module. The server listens for incoming connections on a specific IP address and port. Once a connection is established, the server receives data from the client, processes it, and sends a response back. The client sends data to the server, receives the response, and displays it to the user. The communication continues until the user types "bye" to end the session.
'''


#Code for Server:
import socket

def start_server():
    host = "127.0.0.1"
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    print(f"Server listening on {host}:{port}")

    server_socket.listen(2)
    conn, address = server_socket.accept()

    print(f"Connection from {address} has been established!")

    while True:
        data = conn.recv(1024).decode()

        if not 
            break

        print(f"From connected user: {data}")

        data = input(" -> ")
        conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
    start_server()

#Code for client
import socket

def start_client():
    host = "127.0.0.1"
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != "bye":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print(f"From server: {data}")

        message = input(" -> ")

    client_socket.close()

if __name__ == "__main__":
    start_client()


