import socket
HOST = "127.0.0.1"
PORT = 2100

BUFFER_SIZE = 1024

udp_server_socket = socket.socket(socket.AF_INET, socket.DGRAM)
udp_server_socket.bind((HOST, PORT))
print("UPD Server Started...")

while True:
    data = udp_server_socket.recvfrom(BUFFER_SIZE)
    message_received = data[0]
    message_received_from = data[1]
    print(message_received, " is from ", message_received_from)

    # send reply message back to client
    reply_message = "I received your message, " + message_received.decode()
    udp_server_socket.sendto(reply_message.endcode(), message_received_from)