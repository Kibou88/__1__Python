# socket_UDP
# ------------------------------------------------------------------
# But:
# Créer une classe qui va permettre de gérer les dialogues UDP
# ------------------------------------------------------------------
# Date de création: 2025-06-05
# Date de modification: 2025-06-05
# ------------------------------------------------------------------
# Version: V1

import socket
import time

class Socket_UDP:
    def __init__(self, hostname: str, port: int, ip_version:int = 4, server = 0, client = 0):
        self.hostname = hostname
        self.client_addr = None
        self.client_msg = ""
        self.msg_received = ""

        # Check the config for the class
        if server == 0 and client == 0:
            raise Exception("Needs to be choice between server or client")
        elif server != 0 and client != 0:
            raise Exception("Impossible to be server and client in same time")
        elif server != 0:
            self.server = server
            self.client = 0
        elif client != 0:
            self.client = client
            self.server = 0

        if 0 < port < 65535:
            self.port = port
        else:
            raise Exception("port must be between 0 and 65535")

        # Création du self.sock en fonction de l'IPv4 ou 6 choisie par l'utilisateur
        if ip_version == 6:
            self.sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect(self):
        """
        Try to establish an UDP connection to the hostname and specific port
        Raise an exception if the connection fails
        :param
        self.hostname: (str) ip address of host
        self.port: (int) port number of host
        """
        try:
            self.sock.bind((self.hostname, self.port))
            print(f"Socket bound to {self.hostname}:{self.port}")
        except socket.error as msg:
            raise msg

    def close(self):
        """
        Close the connection to the hostname and specific port
        """
        self.sock.close()

    def receive_message(self):
        """
        Receive a message from the host using UDP socket
        Raise an exception if problem with client message and close the connection
        Check if client message is valid and client address
        :return:
        self.client_msg: (str) message received and decoded (UTF-8)
        self.client_addr: (str) ip address of client
        """
        try:
            self.client_msg, client_addr = self.sock.recvfrom(1024)
        except InterruptedError:
            raise Exception("Erreur dans le message, fermeture de la communication")
            self.close()
        if self.client_msg and client_addr:
            self.msg = self.client_msg.decode('utf-8')
            self.client_addr = client_addr

    def send_message(self, message_to_send: str, server_addr: str = "127.0.0.1", server_port: int = None):
        """
        Depends of the configuration (server or client), send a message to the other part using UDP socket
        :param
        message_to_send: (str) message (encoded utf-8) to send to the client or server
        server_addr: (str) ip address of server
        server_port: (int) port number of server
       """
        print(f"Server {self.server} Client {self.client}")
        if self.client_msg and self.server:
            self.sock.sendto(message_to_send.encode('utf-8'), self.client_addr)
        elif self.client and server_port:
            self.sock.sendto(message_to_send.encode('utf-8'), (server_addr, server_port))


    def display_message(self):
        """
        Display the message from client and delete message
        """
        if self.client_msg:
            print("Message reçu: ", self.client_msg)
            self.client_msg = ""

    def server_UDP(self, message_to_send: str):
        """
        Activate UDP Server
        :param message_to_send: (str) message to be sent
        """
        while True:
            self.connect()
            self.receive_message()
            self.display_message()
            self.send_message(message_to_send)
            self.close()
            break

    def client_UDP(self, message_to_transmit: str, server_addr: str, server_port: int):
        """
        Activate UDP Client
        :param
        message_to_transmit: (str) message to be transmitted
        server_addr: (str) ip address of server
        server_port: (int) port number of server
        """
        while True:
            print("Sending message to the server:", message_to_transmit)
            print(server_addr, server_port)
            self.send_message(message_to_transmit, server_addr, server_port)
            print("Message transmitted")
            self.receive_message()
            self.close()

if __name__ == "__main__":
    message_to_send = "Hello Client"
    message_to_transmit = "Hello Server"
    server_addr = "127.0.0.1"
    server_port = 65500

    server = Socket_UDP(server_addr, server_port, ip_version=4, server=1)
    server.server_UDP(message_to_send)
    time.sleep(2)
    client1 = Socket_UDP(server_addr, server_port, ip_version=4, client=1)
    client1.client_UDP(message_to_transmit, server_addr, server_port)


