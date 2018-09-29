"""
Module to read data from CSV files and HTML file
to populate an SQL database

ITEC649 2018
"""

from database import DATABASE_NAME
import sqlite3
import csv

con = sqlite3.connect('itec649.db')

reader = csv.reader(open('people.csv', 'r'))
columns = next(reader)
query = 'INSERT INTO people (id, first_name, middle_name, last_name, email, phone) VALUES (?, ?, ?, ?, ?, ?)'
query = query.format(','.join(columns), ','.join('?' * len(columns)))
cursor = con.cursor()
for row in reader:
    cursor.execute(query, row)
con.commit()
cursor.close()

# closes connection to database

if __name__ == '__main__':
    db = sqlite3.connect(DATABASE_NAME)

    # Add your 'main' code here to call your functions
