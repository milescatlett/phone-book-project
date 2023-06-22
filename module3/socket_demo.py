from socket import *

ip = gethostbyname(gethostname())
host_name = gethostname()
localhost = gethostbyname("localhost")
print(host_name)
print(ip)
print(localhost)

HOST = localhost
PORT = 2001  # don't use ports less than 1024

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server started...")
    con, address = s.accept()
    with con:
        print(f"Connection by {address}")
        while True:
            con.sendall(b"Enter your name: ")
            data = con.recv(1024)
            if not data:
                break
            data = "Welcome " + data.decode()
            print(f"Sending {data} to client now ")
            con.sendall(data.encode())