# Library Book Management System 
# Author: IWUOHA GODWIN CHUKWUKA 24/14932
books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book = {"title": title, "author": author}
    books.append(book)
    print("Book added successfully.\n")

def view_books():
    if not books:
        print("No books available.\n")
    else:
        print("Library Books:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book['title']} by {book['author']}")
        print()

def main():
    while True:
        print("LIBRARY BOOK MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print("Exiting system.")
            break
        else:
            print("Invalid option. Try again.\n")

main()
