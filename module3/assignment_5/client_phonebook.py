"""
Author: Miles Catlett
Date: 11/23/2022
This program allows the client connect to the phone book and read or make changes.
"""

import socket

HOST = "127.0.0.1"
PORT = 2001


def client():
    """
    This function connects to the server and allows the client to receive and post information.
    :return: None
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        text = 'something'
        while True and text != '':
            data = s.recv(1024)
            print(data.decode())
            text = input("Type your response: \n")
            s.sendall(text.encode())


client()
