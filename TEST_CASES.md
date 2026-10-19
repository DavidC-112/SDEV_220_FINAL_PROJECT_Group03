# Library Management System Test Cases

## Test Case 1 - Add a Book

Input:
- Title: The Hobbit
- Author: J.R.R. Tolkien
- ISBN: 1001

Expected Result:
The book is successfully added to the library and its status displays as Available.

## Test Case 2 - Add a Patron

Input:
- Name: Elizabeth
- Patron ID: P001

Expected Result:
The patron is successfully added and Books Borrowed displays None.

## Test Case 3 - Checkout a Book

Input:
- ISBN: 1001
- Patron ID: P001

Expected Result:
The checkout is successful. The book status changes to Checked Out and The Hobbit appears in the patron's Books Borrowed list.

## Test Case 4 - Checkout an Already Checked Out Book

Input:
- ISBN: 1001
- Patron ID: P001

Expected Result:
The checkout fails because the book is already checked out. The program continues running without an error.

## Test Case 5 - Return a Book

Input:
- ISBN: 1001
- Patron ID: P001

Expected Result:
The return is successful. The book status changes back to Available and the patron's Books Borrowed displays None.

## Test Case 6 - Invalid ISBN

Input:
- ISBN: 9999
- Patron ID: P001

Expected Result:
The checkout fails and an error message is displayed. The program continues running.

## Test Case 7 - Invalid Patron ID

Input:
- ISBN: 1001
- Patron ID: P999

Expected Result:
The checkout fails and an error message is displayed. The program continues running.

## Test Case 8 - Missing Required Information

Input:
Leave one or more Add Book fields blank and select Add Book.

Expected Result:
An error message tells the user to enter the required information. No book is added.