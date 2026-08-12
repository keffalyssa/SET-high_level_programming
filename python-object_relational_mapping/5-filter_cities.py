#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa,
safe from SQL injection.
Takes 4 arguments: mysql username, mysql password,
database name, and state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    rows = cursor.fetchall()

    city_list = [row[0] for row in rows]
    print(", ".join(city_list))

    cursor.close()
    db.close()
