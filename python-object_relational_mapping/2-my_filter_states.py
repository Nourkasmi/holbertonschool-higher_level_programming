#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to the MySQL database and retrieves all states
    where name matches the provided argument.
    Results are sorted in ascending order by id.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cur = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY %s "
        "ORDER BY id ASC"
    )
    cur.execute(query, (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
