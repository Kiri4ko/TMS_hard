import os


def searchinfile(path: str, word: str, encoding: str):
    confirmed_files = []
    for i in os.listdir(path):
        with open(f"{path}/{i}", "rb") as file:
            book = file.read()
            word_encode = word.encode(encoding=encoding)
            if word_encode in book:
                confirmed_files.append(i)
    return f"Your word list is in the files (quantity: {len(confirmed_files)}): {confirmed_files}."


print(searchinfile("books", "Агафья", "windows-1251"))
