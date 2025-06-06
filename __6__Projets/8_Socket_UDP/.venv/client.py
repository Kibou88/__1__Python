import socket

mySocket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=0, fileno=None
)
print("Socket created.")
while True:
    msg = "Hi I am a UDP client created by Aditya."
    print("Sending msg to the server:", msg)
    mySocket.sendto(msg.encode(), ("localhost", 65500))
    msg_in = mySocket.recv(1024).decode()
    print("Acknowledgment received from the server:")
    print(msg_in)
    print("Terminating the Connection.")
    mySocket.close()
    break