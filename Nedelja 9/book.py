class Book:
    def __init__(self, title, author, pages):
        print("Book has been created")
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'Naslov: {self.title}, Autor: {self.author}, Broj stranica: {self.pages}'
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(self.title)
        print("Book has been deleted")
    
    def __eq__(self, other):
        print("Calling equal")
        return self.title == other.title and self.author == other.author


book1 = Book("Uvod u programiranje", "Marko Markovic", 240)
book2 = Book("Web programiranje", "Marko Markovic", 140)
books = []
books.append(book1)
books.append(book2)

lista = [1, 2, 3]
print(lista) # kako Python zna kako da stampa listu?
print(book1)
print("--------")
for book in books:
    print(book)

print(len(book2))
# del book2

print(book1 == book2)