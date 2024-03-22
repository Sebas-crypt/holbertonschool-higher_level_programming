#!/usr/bin/python3
'''States filtering module'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3])
    st = db.cursor()
    st.execute("SELECT `id`, `name` FROM states WHERE name LIKE BINARY 'N%'\
               ORDER BY `id`;")
    res = st.fetchall()

    if len(res) == 2:
        print("Found 2 records:")
        for i in res:
            print(i)
    else:
        print("Found the following records:")
        for i in res:
            print(i)

    db.close()

