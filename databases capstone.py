# Import the SQLite module
import sqlite3

# Create the SQLite database and a table
def create_database():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            ID INTEGER PRIMARY KEY,
            Title TEXT,
            Author TEXT,
            Quantity INTEGER
        )
    ''')

    # Populate the table with sample data
    cursor.executemany("INSERT INTO book (Title, Author, Quantity) VALUES (?, ?, ?)", [
        ("A Tale of Two Cities", "Charles Dickens", 30),
        ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
        ("The Lion, the Witch, and the Wardrobe", "C.S. Lewis", 25),
        ("The Lord of the Rings", "J.R.R. Tolkien", 37),
        ("Alice in Wonderland", "Lewis Carroll", 12),
    ])

    conn.commit()
    conn.close()

# Call create_database() function 
create_database()


# Function to add a new book to the database
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    quantity = int(input("Enter quantity: "))

    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO book (Title, Author, Quantity) VALUES (?, ?, ?)", (title, author, quantity))

    conn.commit()
    conn.close()

# Function to update book information
def update_book():
    book_id = int(input("Enter the ID of the book to update: "))
    new_title = input("Enter new title (leave empty to keep existing): ")
    new_author = input("Enter new author (leave empty to keep existing): ")
    new_quantity_str = input("Enter new quantity (leave empty to keep existing): ")

    # Check if new_quantity_str is not empty before converting to int
    new_quantity = int(new_quantity_str) if new_quantity_str else None

    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    update_query = "UPDATE book SET"
    update_data = []

    if new_title:
        update_query += " Title = ?,"
        update_data.append(new_title)

    if new_author:
        update_query += " Author = ?,"
        update_data.append(new_author)

    if new_quantity is not None:
        update_query += " Quantity = ?,"
        update_data.append(new_quantity)

    # Remove trailing comma and add the WHERE condition
    update_query = update_query.rstrip(',') + " WHERE ID = ?"
    update_data.append(book_id)

    cursor.execute(update_query, update_data)
    conn.commit()
    conn.close()


# Function to delete a book from the database
def delete_book():
    book_id = int(input("Enter the ID of the book to delete: "))

    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM book WHERE ID = ?", (book_id,))

    conn.commit()
    conn.close()

# Function to search for a book by title or author
def search_books():
    keyword = input("Enter a keyword to search for a book (title or author): ")

    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM book WHERE Title LIKE ? OR Author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()

    if books:
        print("Search Results:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
    else:
        print("No matching books found.")

    conn.close()

# Main program loop
while True:
    print("Bookstore Clerk Menu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_books()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")