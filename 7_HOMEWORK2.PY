import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

create_connection("homework.db")

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)


def create_products(conn, products: tuple):
    sql = """ INSERT INTO products
    (product_title, price, quantity)
    VALUES(?, ?, ?);"""
    cursor = conn.cursor()
    cursor.execute(sql, products)
    conn.commit()

def id_products(conn, id):
    sql = """ WHERE id = ? """
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    conn.commit()

sql_create_table = """
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (6, 3) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0.0
);""" 

connection = create_connection("homework.db")
if connection:
    print("успешное подключение")
    create_table(connection, sql_create_table)
    create_products(connection, ("Apple", 27.10, 20))
    create_products(connection, ("Banana", 29.10, 10))
