class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added successfully!")

    def show_books(self):
        print("\nBooks List:")
        for b in self.books:
            status = "Available" if b.available else "Not Available"
            print(b.title, "-", status)

    def lend_book(self, title):
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                print("Book issued!")
                return
        print("Book not available!")

    def return_book(self, title):
        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned!")
                return


# Menu Driven Program
lib = Library()

while True:
    print("\n1.Add Book\n2.Show Books\n3.Lend Book\n4.Return Book\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        title = input("Enter book name: ")
        lib.add_book(title)

    elif choice == 2:
        lib.show_books()

    elif choice == 3:
        title = input("Enter book name to lend: ")
        lib.lend_book(title)

    elif choice == 4:
        title = input("Enter book name to return: ")
        lib.return_book(title)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")