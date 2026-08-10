class LibraryBook:
    book_title = ""
    author = ""
    total_copies = 0
    issued_copies = 0

    def issue_book(self, quantity):
        available=self.total_copies-self.issued_copies
        if quantity <= available:
            self.issued_copies = self.issued_copies + quantity
            print(quantity, "copy/copies issued successfully")
        else:
            print("Copies are not available")

    def return_book(self, quantity):
        if quantity <= self.issued_copies:
            self.issued_copies = self.issued_copies - quantity
            print(quantity, "copy/copies returned successfully")
        else:
            print("Cannot return more copies than issued")
    def display(self):
        print("Book Title:", self.book_title)
        print("Author :", self.author)
        print("Total Copies :", self.total_copies)
        print("Issued Copies :", self.issued_copies)
        print("Available Copies :", self.total_copies - self.issued_copies)

book1 = LibraryBook()

book1.book_title = "advanced Python"
book1.author = "Guido"
book1.total_copies = 20
book1.issued_copies = 5

print("-----------------------------------")
book1.display()

book1.issue_book(4)

book1.display()

book1.return_book(2)

book1.display()