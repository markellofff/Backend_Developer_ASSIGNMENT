import sqlite3
import json
# connecting to database
db = sqlite3.connect('database.db')
ptr = db.cursor()

create_table = """CREATE TABLE users(Id int, First Name text, Last Name text, Company Name text,
                    Age int, City text, State text, Zip int, Email text, Web text)"""
ptr.execute(create_table)
with open('users.json') as f:
    dataj = json.load(f)
my_list = []
for user in dataj['users']:
    my_list.append(((user['id'], user['first_name'], user['last_name'],
                     user['company_name'], user['age'],
                     user['city'], user['state'], user['zip'], user['email'], user['web'])))

ptr=db.cursor()
sql="""INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?);"""
ptr.executemany(sql, my_list)
db.commit()
