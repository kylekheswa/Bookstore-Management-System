# Bookstore Management System

This Python program provides a simple command-line interface to manage a bookstore database using SQLite. It allows users to perform various operations such as adding, updating, deleting books, and searching for books by title or author.

## Getting Started

To run this program, ensure you have Python installed on your system. Also, make sure to have the SQLite module installed (`sqlite3`), which is typically included with Python installations.

1. Download or clone the source code from the repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the program files.
4. Run the program by executing the command: `python bookstore.py`

## Features

- **Add Book**: Allows the user to add a new book to the database by providing title, author, and quantity information.

- **Update Book**: Enables the user to update existing book information such as title, author, or quantity.

- **Delete Book**: Allows the user to delete a book from the database by specifying its ID.

- **Search Books**: Provides the ability to search for books by title or author. It displays matching books along with their details.

- **Exit**: Terminates the program.

## Database Structure

The program utilizes an SQLite database named `bookstore.db` with a single table named `book`. The structure of the `book` table is as follows:

| Field    | Type     | Description        |
|----------|----------|--------------------|
| ID       | INTEGER  | Primary Key        |
| Title    | TEXT     | Title of the book  |
| Author   | TEXT     | Author of the book |
| Quantity | INTEGER  | Quantity available |

## Usage

Upon running the program, you'll be presented with a menu where you can choose the desired operation by entering the corresponding number:

1. **Enter book**: Add a new book to the database.
2. **Update book**: Update existing book information.
3. **Delete book**: Delete a book from the database.
4. **Search books**: Search for books by title or author.
0. **Exit**: Terminate the program.

## Notes

- When updating a book, you can leave the fields blank to keep the existing values.
- When searching for books, you can enter a keyword (either title or author) to find matching books.

## Author

This program was developed by [Your Name]. Feel free to contact me with any questions or suggestions.

