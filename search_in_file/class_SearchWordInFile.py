import os
import chardet


class SearchWordInFile:
    detector = chardet.UniversalDetector()

    def __init__(self, path: str, list_words: list):
        self.list_words = list_words
        self.path = path
        self.errordecode = []
        self.list_encoding = {}
        self.confirmed_files = []
        self.encode()
        self.search()

    def encode(self):
        for i in os.listdir(self.path):
            with open(f"{self.path}/{i}", "rb") as file:
                book = file.read()
                self.detector.feed(book)
                self.list_encoding[f"{i}"] = self.detector.result["encoding"]

    def search(self):
        for i in self.list_encoding:
            try:
                with open(f"{self.path}/{i}", "r", encoding=self.list_encoding.get(i)) as file:
                    book = file.read()
                    for j in self.list_words:
                        if j in book:
                            self.confirmed_files.append(i)
            except UnicodeDecodeError:
                self.errordecode.append(i)
            except LookupError:
                self.errordecode.append(i)

    def __repr__(self):
        return f"Your word list is in the files (quantity: {len(self.confirmed_files)}): {self.confirmed_files}." \
               f"\nFiles with unknown encoding (quantity: {len(self.errordecode)}): {self.errordecode}."


my_books = SearchWordInFile("books", ["Агафья"])

print(my_books)
