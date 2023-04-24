#!/usr/bin/python3
""" shows the states in the databse"""
import mySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    name = args[3]
    # Initializing the DB
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=name, port=3306)
    # Getting the cursor
    curs = db.cursor()
    # Executing the msql statement and exit from db
    num_rows = curs.execute("""SELECT * FROM states WHERE name
                    LIKE BINARY 'N%' ORDER BY states.id;""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
