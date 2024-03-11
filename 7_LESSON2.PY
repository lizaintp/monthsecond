# #СУБД - СИСТЕМА УПРАВЛЕНИЯ БАЗЫ ДАННЫХ
# #БД - БАЗА ДАННЫХ
# #db - date base
# """CRUD - СОЗДАЕТСЯ ЧИТАЕТ ОБНОВЛЯЕТСЯ УДАЛЯЕТСЯ = CREATE READ UPDATE DELETE """
# import sqlite3

# def create_connection(db_name):
#     connection = sqlite3.connect(db_name)
#     return connection

# create_connection("school.db")

# def create_table(conn, sql):
#     cursor = conn.cursor()
#     cursor.execute(sql)     

# #execute - отправляет запрос в бд
# #cursor - Посредник между нашим кодом и бд(sqlite3)
    
# def create_student(conn, student: tuple):
#     sql = """INSERT INTO students 
#     (fullname, age, hobby, birthday, mark , is_passed)
#     VALUES(?, ?, ?, ?, ?, ?);"""
#     cursor = conn.cursor()
#     cursor.execute(sql, student)
#     conn.commit()
# #str - TEXT, VARCHAR(100)
# #bool - BOOBLEAM
# #float - DOUBLE
# #int - INTEJER
# #DATA - ДЛЯ ДАТЫ
    
# #PRIMARY KEY - УНИКАЛЬНЫЙ КЛЮЧ , ЧТОБЫ НЕ БЫЛО ДУБЛИКАТОВ
# #IF NOT EXISTS - УСЛОВИЕ ЧТОБЫ БАЗА ДАННЫХ ДВА РАЗА НЕ ВЫДАВАЛОСЬ И НЕ ВЫДАВАЛО ОШИБКУ
    
# sql_create_table = """
# CREATE TABLE IF NOT EXISTS students(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# fullname VARCHAR (100), NOT NULL,
# age INTEGER NOT NULL,
# hobby TEXT, 
# birtday DATE NOT NULL,
# mark DUOBLE (5, 2) NOT NULL DEFAULT 0.0,
# is_passed BOOLEAN DEFAULT FALSE
# );"""

# connection = create_connection("school.db")
# if connection:
#     print("Успешноe подключение")
#     create_table(connection, sql_create_table)
#     create_student(connection, ("Abdillabekova Eliza", 17, "drawing", "07-09-2007", "100.00", True ))








    # CУБД - Система Управления Базой Данных
# БД- база данных
# CRUD - Create, Read, Update, Delete

# DB - data base

import sqlite3
# подготовка для создания и связь с базой
############################################

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

create_connection('school.db')


# создать таблицу в базе 
############################################
def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

   

# отправляем  запрос в бд для создания полей(столбцов)
############################################
def create_student(conn, student: tuple):
    sql = """ INSERT INTO students
    (fullname, age, hobby, birthday, mark, is_passed)
    VALUES(?, ?, ?, ?, ?, ?);"""
    cursor = conn.cursor()
    cursor.execute(sql,student)
    conn.commit()
    
def update_students_mark(conn, id, new_mark):
    sql = """ UPDATE students SET mark=?  WHERE id = ? """
    cursor = conn.cursor()
    cursor.execute(sql, (new_mark, id))
    conn.commit()


# создаем столбцы с подходящим типом данных
############################################
sql_create_table = """
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (100) NOT NULL,
age INTEGER NOT NULL,
hobby TEXT NULL,
birthday DATE NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
is_passed BOOLEAN DEFAULT FALSE
);"""


# вводим данные
############################################
connection = create_connection('school.db')
if connection:
    print('успешное подключение')
    create_table(connection, sql_create_table)
    create_student(connection, ('Temirbaeva Nurai', 16, 'playing the guitar', "07-01-2008", 100.00, True))
    create_student(connection, ('Абдиллабекова Элиза ', 17, 'рисовать', "07-09-2007", 100.00, True))
    create_student(connection, ('Тахиров Хожиакбар', 17, 'Играть футбол', "01-07-2007", 100.00, True))
    create_student(connection, ('Тагайбеков Дайырбек', 14, 'рисовать тоже', "23-05-2009", 100.00, True))
    create_student(connection, ('Байбалаев Аслан', 15, 'много чего любит', "05-07-2008", 100.00, True))
    update_students_mark(connection, 2, 100.00)
    update_students_mark(connection, 4, 100.00)






# execute - Отправляет запрос в бд
# cursor - Посредник между нашим кодом и бд(sqlite3)

# str - TEXT, VARCHAR(100)
# int - INTEGER
# bool - BOOLEAN
# float - DOUBLE




# # IF NOT EXISTS = создать таблицу если такой не существует
# # AUTOINCREMENT = сам сгенерирует айди
# # VARCHAR = текст с ограниченной длиной(str)
# # NOT NULL = обязательное поле
# # DOUBLE = float
# # TEXT = текст без ограничений(str)
# # DEFAULT NULL = необязательное поле

    
#  PRIMARY KEY - УНИКАЛЬНЫЙ КЛЮЧ что бы не было дубликатов
# IF NOT EXISTS - условие чтобы бд два раза не создавалась и вне выдавал ошибку













