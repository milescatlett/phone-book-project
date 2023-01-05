"""
Author: Miles Catlett
Date: 11/23/2022
This houses the PhoneBook class, which is used to format phone book entries.
"""

class PhoneBook:
    def __init__(self, phone_number, first_name, last_name, street_address, city, state, zip):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return f'{self.phone_number}\n{self.last_name}, {self.first_name}\n{self.street_address}\n{self.city}, ' \
               f'{self.state} {self.zip}'

    def get_entry_by_last_name(self, last_name):
        if self.last_name == last_name:
            return self.__str__()

