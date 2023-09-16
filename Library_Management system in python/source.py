# Abdul Aziz
# BCSF19A026
# Add/Drop

library = []
class Book:
    def __init__(self, IBAN, name, author, issued = False):
        self.IBAN = IBAN
        self.name = name
        self.author = author
        self.issued = issued
    def issue_book(self):
        self.issued = True
    def return_book(self):
        self.issued = False
    def display(self):
        print (f"{self.IBAN}, {self.name}, {self.author}, {int(self.issued)}")

        
def add_book():
    print ("Enter Book\n")
    IBAN= input("IBAN: ")
    while len(IBAN) != 5: 
        IBAN = input("Enter IBAN with 5 character: ")
    name = input("Name: ")
    author = input ("Author: ")
    new_book = Book(IBAN, name, author)
    library.append(new_book)
def search_book():
    flag = False
    print("1. search book by name\n2. search book by author")
    choice = input ("Your choice: ")
    while ( choice < "1" or  choice   > "2"):
        choice = input ("Input Valid choice 1,2:")
    if (choice == "1"):
        name = input("Enter book name: ")
        for book in library:
            if name == book.name:
                print("Book found")
                book.display()
                flag = True
                break
        if not flag:
            print("Book not found")
    else:
        author = input ("Enter author: ")
        for book in library:
            if author== book.author:
                print("Book found")
                book.display()
                flag = True
                break
        if not flag:
            print("Book not found")
def show_books():
    for book in library:
        book.display()
while True:
    print("1. Add a book.\n2. Search a book.\n3. Show all book present in the library.\n4. Issue a book")
    print ("5. Return a book\n6. Exit")
    choice = input ("Your Choice: ")
    while ( choice < "1" or choice > "6"):
        choice = input ("Enter a Valid Choice 1-6: ")
    print("\n\n")
    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        show_books()
    elif choice == "4":
        IBAN = input("Enter IBAN: ")
        flag = False
        while len(IBAN) != 5: 
            IBAN = input("Enter IBAN with 5 character: ")
        for book in library:
            if (book.IBAN == IBAN and book.issued == False):
                print ("Book found and issued successfully")
                book.issue_book()
                flag = True
                break
        if not flag:
            print ("Book is not available")
    elif choice == "5":
        IBAN = input("Enter IBAN: ")
        flag = False
        while len(IBAN) != 5: 
            IBAN = input("Enter IBAN with 5 character: ")
        for book in library:
            if (book.IBAN == IBAN and book.issued == True):
                print ("Book return successfully")  
                book.return_book()
                flag = True
                break
        if not flag:
            print ("Book is not found or still available to issue")
    else:
        with open ("books.txt", "w") as f:
            for book in library:
                f.write (str(book.IBAN))
                f.write(", ")
                f.write(str(book.name))
                f.write(", ")
                f.write(str(book.author))
                f.write(", ")
                f.write(str(int(book.issued)))
                f.write("\n")
        exit()
    print("\n\n\n")
