"""
Author: Miles Catlett
Date: 11/23/2022
This file houses the database functions for the phone book app. I had an issue with the global connection that was
causing an error. In researching this, I found I could avoid the error by connecting individually inside the function.
This error was because of the threading being used.
"""
import sqlite3


def create_table():
    """
    Creates a new table. Runs in main.
    :return: None
    """
    stmt = '''CREATE TABLE Phone_Book (
                phone_number text,
                first_name text,
                last_name text,
                street_address text,
                city text,
                state text,
                zip integer
            )'''
    try:
        con = sqlite3.connect('phone_book.db')
        cur = con.cursor()
        cur.execute(stmt)
        cur.close()
        con.commit()
    except:
        print('Database already created.')


def insert_entry(phone_number, first_name, last_name, street_address, city, state, zip):
    """
    This function inserts a PhoneBook object into the database.
    :param phone_number: String
    :param first_name: String
    :param last_name: String
    :param street_address: String
    :param city: String
    :param state: String
    :param zip: Integer
    :return: None
    """
    stmt = '''INSERT INTO Phone_Book (phone_number, first_name, last_name, street_address, city, state, zip)
            VALUES (?, ?, ?, ?, ?, ?, ?)'''
    if get_entry_by_last_name(last_name) is None:
        con = sqlite3.connect('phone_book.db')
        cur = con.cursor()
        cur.execute(stmt, (phone_number, first_name, last_name, street_address, city, state, zip))
        cur.close()
        con.commit()
        return 'Entry has been added.'
    else:
        return "This entry already exists."


def get_entry_by_last_name(last_name):
    """
    This function returns the overriden __str__ based on the last_name that is submitted.
    :param last_name:
    :return: String
    """
    sql = 'SELECT * FROM Phone_Book WHERE last_name = ?'
    con = sqlite3.connect('phone_book.db')
    cur = con.cursor()
    cur.execute(sql, (last_name,))
    result = cur.fetchone()
    cur.close()
    return result

