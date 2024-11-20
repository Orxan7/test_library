import json


class Book:
    def __init__(self, title: str, author: str, year: int,
                 status: str = "в наличии", id: int = 1):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def as_dict(self):
        """Преобразование объекта книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:
    def __init__(self, filename='data.json'):
        self.filename = filename

    def get_all_books(self) -> list:
        """Получить все книги из JSON файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_next_id(self) -> int:
        """Генерирование ID для следующей книги."""
        books = self.get_all_books()
        if books:
            return max(book['id'] for book in books) + 1
        return 1

    def add_book(self, book: Book):
        """Добавление новой книги в библиотеку."""
        book.id = self.get_next_id()

        books = self.get_all_books()
        books.append(book.as_dict())

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=4, ensure_ascii=False)

    def display_all_books(self):
        """Показать все книги из библиотеки."""
        books = self.get_all_books()
        if not books:
            print("Библиотека пока пустая.")
        for book in books:
            print(f"ID: {book['id']}, Название: {book['title']}, "
                  f"Автор: {book['author']}, Год: {book['year']}, "
                  f"Статус: {book['status']}")

    def search_books(self, search_term: str):
        """Поиск книги по автору или названию."""
        books = self.get_all_books()
        found_books = [book for book in books
                       if search_term.lower() in book['title'].lower() or
                       search_term.lower() in book['author'].lower()]

        if not found_books:
            print(f"Не найдено книг по запросу '{search_term}'.")
        else:
            for book in found_books:
                print(f"ID: {book['id']}, Название: {book['title']}, "
                      f"Автор: {book['author']}, Год: {book['year']}, "
                      f"Статус: {book['status']}")

    def remove_book(self, book_id: int):
        """Удаление книги из библиотеки по ID."""
        books = self.get_all_books()
        updated_books = [book for book in books if book['id'] != book_id]

        if len(updated_books) == len(books):
            print(f"Не найдено книг с ID {book_id}.")
        else:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(updated_books, f, indent=4, ensure_ascii=False)
            print(f"Книга с ID {book_id} была удалена.")

    def update_book_status(self, book_id: int, new_status: str):
        """Обновление статуса книги."""
        if new_status not in ["в наличии", "выдана"]:
            print('Неправильный статус. Выберите один из статусов '
                  '"в наличии" или "выдана".')

        books = self.get_all_books()
        updated_books = False

        for book in books:
            if book['id'] == book_id:
                book['status'] = new_status
                updated_books = True
                print(f"Статус книги '{book['title']}' (ID: {book_id}) был"
                      f" обновлен на '{new_status}'.")
                break

        if not updated_books:
            print(f"Не найдено книги с ID {book_id}.")
        else:
            # Save the updated list back to the JSON file
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(books, f, indent=4, ensure_ascii=False)
