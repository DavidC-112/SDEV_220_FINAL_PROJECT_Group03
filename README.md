# Library Management System

## SDEV 220 Final Project - Group 03

This project is a Python Library Management System created for the
SDEV 220 Final Project.

## Features

The system allows a user to:

- Add books to the library inventory
- Add library patrons
- Check out books
- Return books
- View book availability
- View registered patrons
- View books currently borrowed by each patron
- Handle invalid or missing information

## Files

- backend.py - Contains the Book, Patron, and LibraryCatalog classes
  and the main library logic.
- gui.py - Contains the Tkinter graphical user interface.
- TEST_CASES.md - Contains test cases used to test the system.

## How to Run the Program

1. Make sure Python 3 is installed.
2. Download or clone this GitHub repository.
3. Open the project folder in VS Code or another Python IDE.
4. Run:

python gui.py

The Library Management System window will open.

## Example Test

1. Add a book:
   - Title: The Hobbit
   - Author: J.R.R. Tolkien
   - ISBN: 1001

2. Add a patron:
   - Name: Elizabeth
   - Patron ID: P001

3. Checkout:
   - ISBN: 1001
   - Patron ID: P001

The book should display as "Checked Out" and The Hobbit should appear
under the patron's borrowed books.

4. Return the same book.

The book should return to "Available" and the patron's borrowed books
should display "None".

## Technology Used

- Python
- Tkinter
- GitHub
- Trello
