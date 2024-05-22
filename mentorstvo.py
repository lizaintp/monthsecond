import sqlite3

connect = sqlite3.connect("library.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL
);
               """)

class Library:
    def __init__(self):
        self.title = None

    def add_book(self, title):
        cursor.execute("INSERT INTO books (title) VALUES (?)", (title,))
        connect.commit()
        print(f'Книга "{title}" добавлена в библиотеку.')

    def remove_book(self, book_id):
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        if cursor.rowcount > 0:
            connect.commit()
            print(f'Книга с ID {book_id} удалена из библиотеки.')
        else:
            print(f'Книги с ID {book_id} нет в библиотеке.')

    def display_books(self):
        cursor.execute("SELECT id, title FROM books")
        books = cursor.fetchall()
        if books:
            print("Список книг в библиотеке:")
            for book in books:
                print(f"ID: {book[0]}, Название: {book[1]}")
        else:
            print("В библиотеке нет книг.")

    def count_books(self):
        cursor.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]
        print(f'Общее количество книг в библиотеке: {count}')

    def main(self):
        while True:
            print("Выберите команду: ")
            print("1-Добавить книгу, 2-Удалить книгу, 3-Информация, 4-Посчитать сколько книг")
            command = int(input("Введите цифру: "))
            if command ==1:
                title = input("Введите название книги: ")
                self.add_book(title)

            elif command == 2:
                try:
                    book_id = int(input("Введите ID книги: "))
                    self.remove_book(book_id)
                except ValueError:
                    print("Пожалуйста, введите числовой ID.")

            elif command == 3:
                title = ('Хорошо')
                self.display_books()

            elif command == 4:
                title = ('Хорошо')
                self.count_books()
            else:
                print("Такой команды нет")

me = Library()
me.main()