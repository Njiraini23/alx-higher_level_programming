#!/usr/bin/python3
""" lists all the staes from the database hbtn_Oe_O_usa:"""

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    my_user = argv[1]
    my_pass = argv[2]
    name = argv[3]
    #DB iniliaization
    db = MySQLdb.connect(host='localhost', user=my_user, passwd=my_pass,
                         db=name, port=3306)
    #Get the cursor
    curs = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id;')
    result = cur.fetchall()
    [print(row) for row in result]
    cur.close()
    db.close()
