import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS stores (id INTEGER PRIMARY KEY, name text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real, store_id INTEGER, FOREIGN KEY(store_id) REFERENCES stores(id))"
cursor.execute(create_table)

connection.commit()

connection.close()

