import tkinter as tk
from tkinter import messagebox
from backend import Book, Patron, LibraryCatalog


# Create the library catalog
catalog = LibraryCatalog()


# ---------------- FUNCTIONS ----------------

def add_book():
    title = book_title_entry.get().strip()
    author = book_author_entry.get().strip()
    isbn = book_isbn_entry.get().strip()

    if not title or not author or not isbn:
        messagebox.showerror(
            "Error",
            "Please enter a title, author, and ISBN."
        )
        return

    if isbn in catalog.books:
        messagebox.showerror(
            "Error",
            "A book with that ISBN already exists."
        )
        return

    book = Book(title, author, isbn)
    catalog.add_book(book)

    messagebox.showinfo(
        "Success",
        f"{title} was added to the library."
    )

    book_title_entry.delete(0, tk.END)
    book_author_entry.delete(0, tk.END)
    book_isbn_entry.delete(0, tk.END)

    update_display()


def add_patron():
    name = patron_name_entry.get().strip()
    patron_id = patron_id_entry.get().strip()

    if not name or not patron_id:
        messagebox.showerror(
            "Error",
            "Please enter a patron name and ID."
        )
        return

    if patron_id in catalog.patrons:
        messagebox.showerror(
            "Error",
            "A patron with that ID already exists."
        )
        return

    patron = Patron(name, patron_id)
    catalog.add_patron(patron)

    messagebox.showinfo(
        "Success",
        f"{name} was added as a patron."
    )

    patron_name_entry.delete(0, tk.END)
    patron_id_entry.delete(0, tk.END)

    update_display()


def checkout_book():
    isbn = checkout_isbn_entry.get().strip()
    patron_id = checkout_patron_entry.get().strip()

    if not isbn or not patron_id:
        messagebox.showerror(
            "Error",
            "Please enter an ISBN and Patron ID."
        )
        return

    if catalog.checkout_book(isbn, patron_id):
        messagebox.showinfo(
            "Success",
            "Book checked out successfully."
        )

        checkout_isbn_entry.delete(0, tk.END)
        checkout_patron_entry.delete(0, tk.END)

        update_display()

    else:
        messagebox.showerror(
            "Checkout Failed",
            "Unable to check out the book.\n\n"
            "Check that the ISBN and Patron ID are correct "
            "and that the book is available."
        )


def return_book():
    isbn = return_isbn_entry.get().strip()
    patron_id = return_patron_entry.get().strip()

    if not isbn or not patron_id:
        messagebox.showerror(
            "Error",
            "Please enter an ISBN and Patron ID."
        )
        return

    if catalog.return_book(isbn, patron_id):
        messagebox.showinfo(
            "Success",
            "Book returned successfully."
        )

        return_isbn_entry.delete(0, tk.END)
        return_patron_entry.delete(0, tk.END)

        update_display()

    else:
        messagebox.showerror(
            "Return Failed",
            "Unable to return the book.\n\n"
            "Check that the ISBN and Patron ID are correct."
        )


def update_display():
    # Clear the current information
    display_text.delete("1.0", tk.END)

    # Display book inventory
    display_text.insert(
        tk.END,
        "BOOK INVENTORY\n"
    )

    display_text.insert(
        tk.END,
        "----------------------------------------\n"
    )

    if not catalog.books:
        display_text.insert(
            tk.END,
            "No books currently in the library.\n"
        )

    for book in catalog.books.values():

        if book.is_book_checked_out:
            status = "Checked Out"
        else:
            status = "Available"

        display_text.insert(
            tk.END,
            f"Title: {book.title}\n"
            f"Author: {book.author}\n"
            f"ISBN: {book.isbn}\n"
            f"Status: {status}\n\n"
        )

    # Display patrons
    display_text.insert(
        tk.END,
        "\nPATRONS\n"
    )

    display_text.insert(
        tk.END,
        "----------------------------------------\n"
    )

    if not catalog.patrons:
        display_text.insert(
            tk.END,
            "No patrons currently registered.\n"
        )

    for patron in catalog.patrons.values():

        if patron.books_borrowed:
            borrowed = ", ".join(patron.books_borrowed)
        else:
            borrowed = "None"

        display_text.insert(
            tk.END,
            f"Name: {patron.name}\n"
            f"Patron ID: {patron.patron_id}\n"
            f"Books Borrowed: {borrowed}\n\n"
        )


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Library Management System")
root.geometry("750x850")


# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="Library Management System",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=15)


# ---------------- ADD BOOK ----------------

book_frame = tk.LabelFrame(
    root,
    text="Add Book",
    padx=10,
    pady=10
)

book_frame.pack(
    fill="x",
    padx=20,
    pady=5
)

tk.Label(
    book_frame,
    text="Title:"
).grid(row=0, column=0, sticky="w")

book_title_entry = tk.Entry(
    book_frame,
    width=25
)

book_title_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

tk.Label(
    book_frame,
    text="Author:"
).grid(row=0, column=2, sticky="w")

book_author_entry = tk.Entry(
    book_frame,
    width=25
)

book_author_entry.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)

tk.Label(
    book_frame,
    text="ISBN:"
).grid(row=1, column=0, sticky="w")

book_isbn_entry = tk.Entry(
    book_frame,
    width=25
)

book_isbn_entry.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)

add_book_button = tk.Button(
    book_frame,
    text="Add Book",
    command=add_book
)

add_book_button.grid(
    row=1,
    column=3,
    pady=5
)


# ---------------- PATRON MANAGEMENT ----------------

patron_frame = tk.LabelFrame(
    root,
    text="Patron Management",
    padx=10,
    pady=10
)

patron_frame.pack(
    fill="x",
    padx=20,
    pady=5
)

tk.Label(
    patron_frame,
    text="Name:"
).grid(row=0, column=0, sticky="w")

patron_name_entry = tk.Entry(
    patron_frame,
    width=25
)

patron_name_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

tk.Label(
    patron_frame,
    text="Patron ID:"
).grid(row=0, column=2, sticky="w")

patron_id_entry = tk.Entry(
    patron_frame,
    width=25
)

patron_id_entry.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)

add_patron_button = tk.Button(
    patron_frame,
    text="Add Patron",
    command=add_patron
)

add_patron_button.grid(
    row=1,
    column=3,
    pady=5
)


# ---------------- CHECKOUT BOOK ----------------

checkout_frame = tk.LabelFrame(
    root,
    text="Checkout Book",
    padx=10,
    pady=10
)

checkout_frame.pack(
    fill="x",
    padx=20,
    pady=5
)

tk.Label(
    checkout_frame,
    text="ISBN:"
).grid(row=0, column=0, sticky="w")

checkout_isbn_entry = tk.Entry(
    checkout_frame,
    width=25
)

checkout_isbn_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

tk.Label(
    checkout_frame,
    text="Patron ID:"
).grid(row=0, column=2, sticky="w")

checkout_patron_entry = tk.Entry(
    checkout_frame,
    width=25
)

checkout_patron_entry.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)

checkout_button = tk.Button(
    checkout_frame,
    text="Checkout Book",
    command=checkout_book
)

checkout_button.grid(
    row=1,
    column=3,
    pady=5
)


# ---------------- RETURN BOOK ----------------

return_frame = tk.LabelFrame(
    root,
    text="Return Book",
    padx=10,
    pady=10
)

return_frame.pack(
    fill="x",
    padx=20,
    pady=5
)

tk.Label(
    return_frame,
    text="ISBN:"
).grid(row=0, column=0, sticky="w")

return_isbn_entry = tk.Entry(
    return_frame,
    width=25
)

return_isbn_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

tk.Label(
    return_frame,
    text="Patron ID:"
).grid(row=0, column=2, sticky="w")

return_patron_entry = tk.Entry(
    return_frame,
    width=25
)

return_patron_entry.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)

return_button = tk.Button(
    return_frame,
    text="Return Book",
    command=return_book
)

return_button.grid(
    row=1,
    column=3,
    pady=5
)


# ---------------- LIBRARY INFORMATION ----------------

display_frame = tk.LabelFrame(
    root,
    text="Library Information",
    padx=10,
    pady=10
)

display_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

display_text = tk.Text(
    display_frame,
    height=15,
    width=80
)

display_text.pack(
    fill="both",
    expand=True
)


# Display initial empty library information
update_display()


# ---------------- START PROGRAM ----------------

root.mainloop()