from models import Book, Library
from texts import texts
import time


if __name__ == "__main__":
    print("Добро пожаловать в библиотеку!")

    try:
        library = Library()
        while True:
            try:
                value = int(input(texts['main']))
            except ValueError:
                continue
            match value:
                case 1:
                    title = input("Введите название книги:")
                    author = input("Введите автора книги:")
                    while True:
                        try:
                            year = int(input("Введите год книги: "))
                            break
                        except ValueError:
                            print("Ошибка! Пожалуйста, введите числовое "
                                  "значение для года.")
                    book = Book(title=title, author=author, year=year)
                    library.add_book(book)
                case 2:
                    while True:
                        try:
                            id = int(input("Введите ID книги:"))
                            break
                        except ValueError:
                            print("Ошибка! Пожалуйста, введите числовое "
                                  "значение для ID.")
                    library.remove_book(id)
                case 3:
                    search_term = input("Введите название или автора книги:")
                    library.search_books(search_term=search_term)
                case 4:
                    library.display_all_books()
                case 5:
                    while True:
                        try:
                            book_id = int(input("Введите ID книги:"))
                            break
                        except ValueError:
                            print("Ошибка! Пожалуйста, введите числовое "
                                  "значение для ID.")
                    new_status = input("Введите новый статус книги:")
                    library.update_book_status(book_id=book_id,
                                               new_status=new_status)
                case 0:
                    raise KeyboardInterrupt
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nБудем ждать вас снова!")
        exit()
