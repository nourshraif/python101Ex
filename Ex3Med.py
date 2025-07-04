class Book:
    def __init__(self,title,author,year,is_checked_out=False):
        self.title=title
        self.author=author
        self.year=year
        self.is_checked_out=is_checked_out
    def checkout(self):
        self.is_checked_out=True
    
    def return_book(self):
        self.is_checked_out=False

    def __str__(self):
      return f"{self.title} by {self.author} | Checked Out: {self.is_checked_out}"

    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
    def find_book(self,title):
        for book in self.books:
            if book.title==title:
                return True
        return False    
    def available_books(self):
        b=[]
        booksAv=""
        for book in self.books:
            if not book.is_checked_out:
                b.append(book.title)
                booksAv+=book.title+"\n"
        return booksAv
    
b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.list_books()

b1.checkout()
lib.list_books()

found = lib.find_book("1984")
print(found)
        

    
    
        