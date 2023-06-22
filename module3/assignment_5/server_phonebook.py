"""
Author: Miles Catlett
Date: 11/23/2022
This program allows the client connect to the server. The use of threads allows multiple clients to interact
while appearing that the program is running normally. The server program sends and receives information (objects)
from the user and then accesses the database on the user's behalf. It also utilizes the phone book class.
"""

from socket import *
import phone_book as pb
import db
from threading import Thread

HOST = 'localhost'
PORT = 2001


class PhoneBookUser(Thread):
    """
    This class allows the creation of individual user threads.
    """
    def __init__(self, name="Phone book user thread", count=100):
        Thread.__init__(self, name=name)
        self.count = count

    def run(self):
        for i in range(self.count):
            print(f'{self.getName()}: {i}')
            with socket(AF_INET, SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                print("Server started...")
                con, address = s.accept()
                with con:
                    print(f"Connection by {address}")
                    while True:
                        con.sendall(b"Please enter a selection: "
                                    b"\n 1 for searching the phone book. "
                                    b"\n 2 for creating a new entry. ")
                        data = con.recv(1024)
                        response = data.decode()
                        print(response)
                        if response == '1':
                            con.sendall(b"Please enter the last name you want to search: \n")
                            data = con.recv(1024)
                            last_name = data.decode()
                            entry_name = db.get_entry_by_last_name(last_name)
                            entry = pb.PhoneBook(
                                entry_name[0],
                                entry_name[1],
                                entry_name[2],
                                entry_name[3],
                                entry_name[4],
                                entry_name[5],
                                entry_name[6],
                            )
                            entry = entry.__str__()
                            con.sendall(entry.encode())
                        if response == '2':
                            con.sendall(b"Please enter the phone number: \n")
                            data = con.recv(1024)
                            phone_number = data.decode()
                            con.sendall(b"Please enter the last name: \n")
                            data = con.recv(1024)
                            last_name = data.decode()
                            con.sendall(b"Please enter the first name: \n")
                            data = con.recv(1024)
                            first_name = data.decode()
                            con.sendall(b"Please enter the street address: \n")
                            data = con.recv(1024)
                            street_address = data.decode()
                            con.sendall(b"Please enter the city: \n")
                            data = con.recv(1024)
                            city = data.decode()
                            con.sendall(b"Please enter the state: \n")
                            data = con.recv(1024)
                            state = data.decode()
                            con.sendall(b"Please enter the zip: \n")
                            data = con.recv(1024)
                            zip = data.decode()
                            db.insert_entry(phone_number, first_name, last_name, street_address, city, state, zip)
                            new_entry = db.get_entry_by_last_name(last_name)
                            new_entry = pb.PhoneBook(
                                new_entry[0],
                                new_entry[1],
                                new_entry[2],
                                new_entry[3],
                                new_entry[4],
                                new_entry[5],
                                new_entry[6],
                            )
                            text = 'Success! Here is the new entry: \n'
                            new_entry = new_entry.__str__()
                            text += new_entry
                            con.sendall(text.encode())
                        if data is not None:
                            break


def main():
    """
    This function creates the database and adds several entries. It also creates three threads.
    :return: None
    """
    db.create_table()
    entry1 = pb.PhoneBook('(336)555-4444', 'John', 'Doe', '123 My Place', 'Clemmons', 'NC', '27012')
    entry2 = pb.PhoneBook('(336)555-3333', 'Sally', 'Wayne', '456 My Court', 'Clemmons', 'NC', '27012')
    entry3 = pb.PhoneBook('(336)555-2222', 'James', 'Smith', '789 My Avenue', 'Clemmons', 'NC', '27012')
    entries = [entry1, entry2, entry3]
    for i in range(len(entries)):
        db.insert_entry(
            entries[i].phone_number,
            entries[i].first_name,
            entries[i].last_name,
            entries[i].street_address,
            entries[i].city,
            entries[i].state,
            entries[i].zip
        )
    # In a real case I think there would be additional logic here that would create a new thread for each user.
    # This throws an error if you enable more than one thread because it wants to use a different socket.
    # I would need to figure out how to create a new socket connection for each user to avoid the error.
    task1 = PhoneBookUser()
    task1.start()
    # task2 = PhoneBookUser()
    # task2.start()
    # task3 = PhoneBookUser()
    # task3.start()


main()
