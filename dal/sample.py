"""

pip install pymysql
pip install cryptography

"""

import pymysql


# connection to database
connection = pymysql.connect(
    host='localhost',
    user='adam',
    password='qwerty@123',
    database='starwarsDB'
 )

cursor = connection.cursor()
sql = "select * from starwarsDB.species_sample;"
result = cursor.execute(sql)
print(result)
