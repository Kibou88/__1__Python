# server_UDP
# ------------------------------------------------------------------
# But:
# Créer une classe qui va permettre de créer et gérer un serveur UDP
# ------------------------------------------------------------------
# Date de création: 2025-06-06
# Date de modification: 2025-06-06
# ------------------------------------------------------------------
# Version: V1

import socket

class server_UDP:

    def __init__(self, server_addr, server_port, ip_version=4):
        self.hostname = hostname
        # self.client_addr = None
        # self.client_msg = ""
        self.msg_received = ""

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

if __name__ == "__main__":
    message_to_send = "Hello Client"
    message_to_transmit = "Hello Server"
    server_addr = "127.0.0.1"
    server_port = 65500

    server = server_UDP(server_addr, server_port, ip_version=4)