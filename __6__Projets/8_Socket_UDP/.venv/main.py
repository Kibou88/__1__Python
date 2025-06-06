# Socket UDP
# -------------------------------------------------------------------
# main.py
# -------------------------------------------------------------------
# But:
# Contient la logique du code pour la création/gestion de socket UDP
# -------------------------------------------------------------------
# Date de création: 2025-06-05
# Date de modification: 2025-06-05
# -------------------------------------------------------------------
# Version: 1.0

import socket

HOSTNAME = "127.0.0.1"
PORT = 9999

try:
    socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=0, fileno=None)
    # socket_UDP.bind((HOSTNAME, PORT))
    #AF_INET => IPv4  // SOCK_DGRAM => UDP
    #AF_INET6 => IPv6 // SOCK_STREAM => TCP
except socket.error as msg:
    print("Socket creation error")
except AttributeError:
    print("Erreur dans les attributs sockets")
else:
    print("Socket creation successful")

socket_UDP.bind((HOSTNAME, PORT))
# socket_UDP.listen(5) # le paramètre désigne le nombre maximum de connexions non acceptées que le système
# autorisera avant de refuser de nouvelles connexions.
while True:
    print(socket_UDP.recvfrom(1024))
    msg, client_addr = socket_UDP.recvfrom(1024)
    print("Message recieved")
    print(msg.decode())
    print("Sending message received to the client")
    msg_out = "Message received"
    socket_UDP.sendto(msg_out.encode(), client_addr)
    socket_UDP.close()
    break
