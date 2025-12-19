# library_app.py
# Clean, heavily commented, single-file Library Management GUI using customtkinter (CTk).
# This application manages users, books, and borrowing records, persisting data to JSON files.
#
# Usage:
# 1. pip install customtkinter
# 2. python library_app.py

import json                                     # Standard library for handling JSON data (saving/loading).
import os                                       # Standard library, although not strictly needed here, often useful for file paths.
from datetime import datetime                   # Used to record the timestamp when a book is borrowed.
import customtkinter as ctk                     # Imports the custom Tkinter library for a modern look.
from tkinter import messagebox                  # Standard, reliable Tkinter dialogs for user feedback (errors, success).

# --- Filenames for persistent storage ---
USERS_FILE = "users.json"                       # File to store user credentials and roles (admin/member).
BOOKS_FILE = "books.json"                       # File to store book inventory data (title, author, availability).
BORROWED_FILE = "borrowed_books.json"           # File to store active borrowing records (who has which book).


# --- Utility functions for safe JSON read/write ---


def safe_load_json(path, default):
    """
    Load JSON from `path`. If file doesn't exist or is invalid, return `default`.
    This prevents crashes when JSON files are missing or corrupt.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:  # Open the file specified by 'path' in read mode ('r').
            return json.load(f)                     # Attempt to parse the JSON content and return it.
    except (FileNotFoundError, json.JSONDecodeError):
        # Catch errors if the file is missing or the content is malformed JSON.
        return default                              # If an error occurs, return the safe default value (e.g., {} or []).


def safe_save_json(path, data):
    """
    Save `data` to `path` as JSON, creating/overwriting the file safely.
    """
    with open(path, "w", encoding="utf-8") as f:      # Open the file in write mode ('w'), creating it if it doesn't exist.
        # Dump the Python data structure into the file as formatted JSON (indent=4).
        json.dump(data, f, indent=4, ensure_ascii=False)


# --- Main application class ---


class LibraryApp:
    def __init__(self):
        """
        Initialize the main window, load data, and show the login screen.
        """
        # Appearance settings for customtkinter
        ctk.set_appearance_mode("dark")                 # Set the overall application theme to "dark" mode.
        ctk.set_default_color_theme("blue")             # Set the primary color for widgets to "blue".

        # Create main window (the root container)
        self.root = ctk.CTk()                           # Instantiate the main customtkinter window.
        self.root.title("Library Management System")    # Set the window title displayed in the title bar.
        self.root.geometry("900x620")                   # Set the initial size of the window (width x height).

        # Load persisted data (users, books, borrowed records) using the utility function
        # Users stored as dict: {username: {"password": "...", "role": "admin"/"member"}}
        self.users = safe_load_json(USERS_FILE, {})     # Load user data; defaults to an empty dict if file is missing.
        # Ensure there is a default admin if none exists
        if not self.users:                              # Check if the loaded user dictionary is empty (first run).
            # Default admin account for first run; encourage changing later.
            self.users["admin"] = {"password": "admin", "role": "admin"}

        # Books stored as dict: {isbn: {"title": str, "author": str, "available": bool}}
        self.books = safe_load_json(BOOKS_FILE, {})     # Load book inventory; defaults to an empty dict.

        # Borrowed stored as list of records: {"isbn": str, "borrower": username, "borrow_date": str}
        self.borrowed_books = safe_load_json(BORROWED_FILE, []) # Load borrowed records; defaults to an empty list.

        # Container where frames/pages will be swapped (this is the central area of the app)
        self.container = ctk.CTkFrame(self.root)        # Create a frame inside the root window to hold dynamic content.
        # Pack the container to fill all available space in the root window, with some padding.
        self.container.pack(fill="both", expand=True, padx=16, pady=12)

        # Track current user session info
        self.current_user = None                        # Initialize session variable; None until successful login.

        # Show login page initially
        self.show_login_frame()                         # Call the method to display the initial login screen.

    # --------------------------
    # Persistence helpers
    # --------------------------
    def save_all(self):
        """Save users, books, and borrowed_books to disk."""
        safe_save_json(USERS_FILE, self.users)          # Save the current state of user data.
        safe_save_json(BOOKS_FILE, self.books)          # Save the current state of book inventory.
        safe_save_json(BORROWED_FILE, self.borrowed_books) # Save the current state of borrowing records.

    # --------------------------
    # Frame management helpers
    # --------------------------
    def clear_container(self):
        """Destroy everything currently inside the container frame."""
        for widget in self.container.winfo_children():   # Iterate over all widgets currently in the container.
            widget.destroy()                            # Destroy each widget to clear the previous screen/frame.

    def show_login_frame(self):
        """Display the login screen."""
        self.clear_container()                          # Clear any existing content in the container.
        LoginFrame(self.container, self)                # Instantiate and display the LoginFrame inside the container.

    def show_register_frame(self):
        """Display the registration screen."""
        self.clear_container()                          # Clear existing content.
        RegisterFrame(self.container, self)             # Instantiate and display the RegisterFrame.

    def show_admin_dashboard(self):
        """Display the admin dashboard."""
        self.clear_container()                          # Clear existing content.
        AdminDashboard(self.container, self)            # Instantiate and display the AdminDashboard.

    def show_member_dashboard(self):
        """Display the member dashboard."""
        self.clear_container()                          # Clear existing content.
        MemberDashboard(self.container, self)           # Instantiate and display the MemberDashboard.

    def run(self):
        """Start event loop."""
        self.root.mainloop()                            # Start the Tkinter event loop, which keeps the GUI running.


# --------------------------
# Login Frame
# --------------------------
class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, app: LibraryApp):
        """
        Login screen with username/password fields and buttons.
        On successful login, redirects to admin or member dashboard.
        """
        super().__init__(parent)                        # Initialize the CTkFrame, placing it inside the 'parent' container.
        self.app = app                                  # Store a reference to the main LibraryApp instance.
        self.pack(fill="both", expand=True)             # Make the frame fill the entire container area.

        # Title
        # Create a large, bold label for the screen title.
        ctk.CTkLabel(self, text="Library Login", font=ctk.CTkFont(size=28, weight="bold")).pack(pady=(24, 10))

        # Username input
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=320) # Create username entry field.
        self.username_entry.pack(pady=8)                # Place the entry field on the screen.

        # Password input
        # Create password entry field; 'show="*" ' masks the input text.
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=320)
        self.password_entry.pack(pady=8)                # Place the password entry field.

        # Login button
        # Button linked to the 'self.login' method.
        ctk.CTkButton(self, text="Login", width=200, command=self.login).pack(pady=(12, 6))

        # Quick register and note area
        # Button to switch to the registration screen.
        ctk.CTkButton(self, text="Register new account", width=200, command=self.app.show_register_frame).pack(pady=6)
        # Informational label about the default admin account.
        ctk.CTkLabel(self, text="Default admin: admin / admin (change after first login)", text_color="#a0a0a0").pack(pady=(8, 0))

    def login(self):
        """Authenticate user and navigate to the correct dashboard."""
        username = self.username_entry.get().strip()    # Retrieve and clean the entered username.
        password = self.password_entry.get()            # Retrieve the entered password.

        # Validate inputs
        if not username or not password:                # Check if either field is empty.
            # Show a warning messagebox if input is missing.
            messagebox.showwarning("Input required", "Please enter username and password.")
            return                                      # Stop further execution of the function.

        # Authenticate
        user = self.app.users.get(username)             # Get the user data dictionary based on the entered username.
        # Check if user exists AND if the password matches.
        if user and user.get("password") == password:
            # Save session info and navigate based on role
            # Store the current user's username and role in the main app instance.
            self.app.current_user = {"username": username, "role": user.get("role", "member")}
            if self.app.current_user["role"] == "admin": # Check if the authenticated user is an admin.
                self.app.show_admin_dashboard()         # Display the admin interface.
            else:
                self.app.show_member_dashboard()        # Display the member interface.
        else:
            # Invalid credentials
            messagebox.showerror("Login failed", "Invalid username or password.")


# --------------------------
# Register Frame
# --------------------------
class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, app: LibraryApp):
        """
        Simple registration screen to create a new admin/member account.
        Validates basic input and prevents duplicate usernames.
        """
        super().__init__(parent)                        # Initialize the CTkFrame.
        self.app = app                                  # Store the main app reference.
        self.pack(fill="both", expand=True)             # Make the frame fill the container.

        # Title
        ctk.CTkLabel(self, text="Register New User", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(20, 12))

        # Username entry
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Choose a username", width=360)
        self.username_entry.pack(pady=8)

        # Password entry
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Choose a password", show="*", width=360)
        self.password_entry.pack(pady=8)

        # Role selection (admin or member) using an OptionMenu widget
        self.role_var = ctk.StringVar(value="member")   # Create a string variable, defaulting the role to "member".
        # Create a dropdown menu for selecting the user role.
        ctk.CTkOptionMenu(self, variable=self.role_var, values=["member", "admin"]).pack(pady=8)

        # Buttons
        ctk.CTkButton(self, text="Register", width=200, command=self.register).pack(pady=(12, 6)) # Register button.
        ctk.CTkButton(self, text="Back to Login", width=200, command=self.app.show_login_frame).pack(pady=6) # Back button.

    def register(self):
        """Create new user if validation passes."""
        username = self.username_entry.get().strip()    # Get the cleaned username.
        password = self.password_entry.get()            # Get the password.
        role = self.role_var.get()                      # Get the selected role.

        # Basic validation
        if not username or not password:                # Check for empty fields.
            messagebox.showwarning("Input required", "Username and password cannot be empty.")
            return

        if username in self.app.users:                  # Check if the username is already taken.
            messagebox.showerror("Duplicate user", "Username already exists.")
            return

        # Save new user
        self.app.users[username] = {"password": password, "role": role} # Add new user data to the dictionary.
        self.app.save_all()                             # Save the updated users dictionary to the JSON file.
        messagebox.showinfo("Success", "Registration successful! You may now log in.") # Success message.
        self.app.show_login_frame()                     # Redirect to the login screen.


# --------------------------
# Admin Dashboard
# --------------------------
class AdminDashboard(ctk.CTkFrame):
    def __init__(self, parent, app: LibraryApp):
        """
        Admin view: add/remove books, borrow/return on behalf of members,
        view borrowers list, and logout.
        """
        super().__init__(parent)                        # Initialize the CTkFrame.
        self.app = app                                  # Store the main app reference.
        self.pack(fill="both", expand=True, padx=8, pady=8) # Fill the container with padding.

        # Header frame
        header = ctk.CTkFrame(self)                     # Create a frame specifically for the header bar.
        header.pack(fill="x", pady=(6, 12))             # Pack the header to fill the width.
        # Welcome label showing current admin's username.
        ctk.CTkLabel(header, text=f"Admin Dashboard — {self.app.current_user['username']}", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=10)
        # Logout button placed on the right side of the header.
        ctk.CTkButton(header, text="Logout", fg_color="red", hover_color="#c33", command=self.logout).pack(side="right", padx=10)

        # Action buttons area frame
        actions = ctk.CTkFrame(self)                    # Frame for the main action buttons.
        actions.pack(fill="x", pady=(4, 12))            # Pack to fill the width.
        # Buttons for various administrative tasks, linked to their respective modal methods.
        ctk.CTkButton(actions, text="Add Book", command=self.add_book_window).pack(side="left", padx=8, pady=6)
        ctk.CTkButton(actions, text="Remove Book", command=self.remove_book_window).pack(side="left", padx=8, pady=6)
        ctk.CTkButton(actions, text="Borrow for Member", command=self.borrow_book_window).pack(side="left", padx=8, pady=6)
        ctk.CTkButton(actions, text="Return Book", command=self.return_book_window).pack(side="left", padx=8, pady=6)
        ctk.CTkButton(actions, text="View Borrowers", command=self.view_borrowers).pack(side="left", padx=8, pady=6)

        # Book summary area frame
        summary_frame = ctk.CTkFrame(self)              # Frame to contain the book inventory list.
        summary_frame.pack(fill="both", expand=True, pady=(6, 8)) # Fill remaining space.
        ctk.CTkLabel(summary_frame, text="Books Inventory (ISBN - Title - Author - Available)", font=ctk.CTkFont(weight="bold")).pack(pady=(6, 4))
        # Textbox to display books list; height set to a fixed value.
        self.books_text = ctk.CTkTextbox(summary_frame, height=320)
        self.books_text.pack(fill="both", expand=True, padx=12, pady=8)
        self.refresh_books_text()                       # Populate the textbox on load.

    def logout(self):
        """Log out and return to login screen."""
        self.app.current_user = None                    # Clear the current user session data.
        self.app.show_login_frame()                     # Navigate back to the login screen.

    def refresh_books_text(self):
        """Update the textbox showing books inventory."""
        self.books_text.configure(state="normal")       # Enable the textbox for editing.
        self.books_text.delete("0.0", "end")            # Clear all existing content.
        
        if not self.app.books:                          # Check if the books dictionary is empty.
            self.books_text.insert("0.0", "No books in inventory.\n") # Display message if no books exist.
        else:
            lines = []                                  # List to hold the formatted text lines.
            for isbn, book in self.app.books.items():   # Iterate through all books in the inventory.
                # Format book details: ISBN - Title - Author - Availability status (Yes/No).
                is_available = 'Yes' if book.get('available', True) else 'No'
                lines.append(f"{isbn} - {book['title']} - {book['author']} - {is_available}")
            self.books_text.insert("0.0", "\n".join(lines)) # Insert the compiled list of books.
        self.books_text.configure(state="disabled")     # Disable the textbox so the user cannot manually edit the list.

    # ---- Admin modal windows ----
    def add_book_window(self):
        """Open modal to add a new book to inventory."""
        win = ctk.CTkToplevel(self)                     # Create a new top-level window (modal dialog).
        win.title("Add New Book")
        win.geometry("420x260")

        # Title input
        ctk.CTkLabel(win, text="Title").pack(pady=(12, 4))
        title_e = ctk.CTkEntry(win, width=360)
        title_e.pack()

        # Author input
        ctk.CTkLabel(win, text="Author").pack(pady=(8, 4))
        author_e = ctk.CTkEntry(win, width=360)
        author_e.pack()

        # ISBN input
        ctk.CTkLabel(win, text="ISBN").pack(pady=(8, 4))
        isbn_e = ctk.CTkEntry(win, width=360)
        isbn_e.pack()

        def add_book():
            """Internal function to handle the book creation logic."""
            title = title_e.get().strip()               # Get and clean the input title.
            author = author_e.get().strip()             # Get and clean the input author.
            isbn = isbn_e.get().strip()                 # Get and clean the input ISBN.
            
            if not (title and author and isbn):         # Check if any required field is empty.
                messagebox.showwarning("Missing data", "All fields are required.")
                return
            if isbn in self.app.books:                  # Check for ISBN duplication.
                messagebox.showerror("Duplicate ISBN", "A book with this ISBN already exists.")
                return
            
            # Add the new book to the main app's dictionary.
            self.app.books[isbn] = {"title": title, "author": author, "available": True}
            self.app.save_all()                         # Persist the change to the BOOKS_FILE.
            self.refresh_books_text()                   # Update the book list display in the dashboard.
            messagebox.showinfo("Success", f"Book '{title}' added.")
            win.destroy()                               # Close the modal window.

        ctk.CTkButton(win, text="Add Book", command=add_book).pack(pady=12) # Button to trigger the 'add_book' logic.

    def remove_book_window(self):
        """Open modal to remove a book by ISBN; only removable if available."""
        win = ctk.CTkToplevel(self)
        win.title("Remove Book")
        win.geometry("420x180")

        ctk.CTkLabel(win, text="ISBN to remove").pack(pady=(12, 4))
        isbn_e = ctk.CTkEntry(win, width=360)
        isbn_e.pack()

        def remove_book():
            """Internal function to handle the book removal logic."""
            isbn = isbn_e.get().strip()
            if not isbn:
                messagebox.showwarning("Input required", "Please enter an ISBN.")
                return
            
            book = self.app.books.get(isbn)             # Retrieve book data.
            if not book:
                messagebox.showerror("Not found", "Book not found.")
                return
            
            # Check if the book is currently borrowed.
            if not book.get("available", True):
                messagebox.showerror("Unavailable", "Cannot remove a borrowed book.")
                return
            
            del self.app.books[isbn]                    # Remove the book entry from the dictionary.
            self.app.save_all()                         # Persist the inventory change.
            self.refresh_books_text()                   # Update the book list display.
            messagebox.showinfo("Removed", "Book removed successfully.")
            win.destroy()

        ctk.CTkButton(win, text="Remove Book", command=remove_book).pack(pady=12)

    def borrow_book_window(self):
        """Admin borrows a book on behalf of a member (records it as borrowed)."""
        win = ctk.CTkToplevel(self)
        win.title("Borrow Book for Member")
        win.geometry("420x220")

        # Member Username input
        ctk.CTkLabel(win, text="Member username").pack(pady=(12, 4))
        user_e = ctk.CTkEntry(win, width=360)
        user_e.pack()

        # ISBN input
        ctk.CTkLabel(win, text="Book ISBN").pack(pady=(8, 4))
        isbn_e = ctk.CTkEntry(win, width=360)
        isbn_e.pack()

        def borrow_for_member():
            """Internal function to handle the forced borrowing logic."""
            member_username = user_e.get().strip()
            isbn = isbn_e.get().strip()

            if not member_username or not isbn:
                messagebox.showwarning("Input required", "Both username and ISBN are required.")
                return
            
            member = self.app.users.get(member_username) # Check if user exists.
            # Check if the user exists and is a 'member' (not an admin trying to borrow for another admin).
            if not member or member.get("role") != "member":
                messagebox.showerror("Invalid member", "Member not found or not a member account.")
                return
            
            book = self.app.books.get(isbn)             # Retrieve book data.
            # Check if book exists and is currently available.
            if not book or not book.get("available", True):
                messagebox.showerror("Unavailable", "Book not found or not available.")
                return
            
            # Mark unavailable and add borrowed record
            self.app.books[isbn]["available"] = False   # Set the book status to unavailable.
            record = {
                "isbn": isbn,
                "borrower": member_username,
                # Store current timestamp for the borrow date.
                "borrow_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.app.borrowed_books.append(record)      # Add the new borrowing record to the list.
            self.app.save_all()
            self.refresh_books_text()
            messagebox.showinfo("Success", "Book borrowed successfully.")
            win.destroy()

        ctk.CTkButton(win, text="Borrow", command=borrow_for_member).pack(pady=12)

    def return_book_window(self):
        """Admin returns a book by ISBN (removes borrowed record and marks available)."""
        win = ctk.CTkToplevel(self)
        win.title("Return Book")
        win.geometry("420x180")

        ctk.CTkLabel(win, text="ISBN to return (Admin override)").pack(pady=(12, 4))
        isbn_e = ctk.CTkEntry(win, width=360)
        isbn_e.pack()

        def return_book():
            """Internal function to handle the forced return logic."""
            isbn = isbn_e.get().strip()
            if not isbn:
                messagebox.showwarning("Input required", "Please enter ISBN.")
                return
            
            found_record = False
            # Iterate over a copy of the list to safely remove elements during iteration (list(...)).
            for rec in list(self.app.borrowed_books):
                if rec.get("isbn") == isbn:             # Check if this record matches the ISBN.
                    self.app.borrowed_books.remove(rec) # Remove the borrowing record.
                    found_record = True
                    
                    # Mark book available (only if the book still exists in the inventory)
                    if isbn in self.app.books:
                        self.app.books[isbn]["available"] = True
                    
                    self.app.save_all()
                    self.refresh_books_text()
                    messagebox.showinfo("Returned", "Book returned successfully.")
                    win.destroy()
                    return                              # Exit the function after successful return.
            
            # This runs only if the loop finishes without finding a match.
            messagebox.showerror("Not found", "No active borrowing record found for this ISBN.")

        ctk.CTkButton(win, text="Return Book", command=return_book).pack(pady=12)

    def view_borrowers(self):
        """Show a window listing all current borrowers and borrowed dates."""
        win = ctk.CTkToplevel(self)
        win.title("Borrowers List")
        win.geometry("700x420")

        if not self.app.borrowed_books:                 # Check if the list of borrowed books is empty.
            ctk.CTkLabel(win, text="No books are currently borrowed.").pack(pady=20)
            return

        # Scrollable frame for borrower rows
        frame = ctk.CTkScrollableFrame(win, width=660, height=360) # Frame that supports scrolling for the list.
        frame.pack(padx=12, pady=12)

        # Header row frame
        header = ctk.CTkFrame(frame)
        header.pack(fill="x", padx=8, pady=(4, 8))
        # Header labels for alignment and identification.
        ctk.CTkLabel(header, text="ISBN", width=20, anchor="w", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=6)
        ctk.CTkLabel(header, text="Title", width=220, anchor="w", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=6)
        ctk.CTkLabel(header, text="Borrower", width=140, anchor="w", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=6)
        ctk.CTkLabel(header, text="Borrow Date", width=200, anchor="w", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=6)

        # Rows for each borrowed record
        for rec in self.app.borrowed_books:             # Iterate through all active borrowing records.
            isbn = rec.get("isbn", "Unknown")
            borrower = rec.get("borrower", "Unknown")
            borrow_date = rec.get("borrow_date", "Unknown")
            # Get the book title from the inventory using the ISBN.
            title = self.app.books.get(isbn, {}).get("title", "Unknown")

            row = ctk.CTkFrame(frame)                   # Create a new frame for each record row.
            row.pack(fill="x", padx=8, pady=2)
            # Display the data fields in separate labels inside the row frame.
            ctk.CTkLabel(row, text=isbn, anchor="w", width=20).pack(side="left", padx=6)
            ctk.CTkLabel(row, text=title, anchor="w", width=220).pack(side="left", padx=6)
            ctk.CTkLabel(row, text=borrower, anchor="w", width=140).pack(side="left", padx=6)
            ctk.CTkLabel(row, text=borrow_date, anchor="w", width=200).pack(side="left", padx=6)


# --------------------------
# Member Dashboard
# --------------------------
class MemberDashboard(ctk.CTkFrame):
    def __init__(self, parent, app: LibraryApp):
        """
        Member view: see available books, borrow/return own books, logout.
        """
        super().__init__(parent)
        self.app = app
        self.pack(fill="both", expand=True, padx=8, pady=8)

        # Header with logout
        header = ctk.CTkFrame(self)
        header.pack(fill="x", pady=(6, 12))
        # Welcome label for the member.
        ctk.CTkLabel(header, text=f"Member Dashboard — {self.app.current_user['username']}", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=10)
        ctk.CTkButton(header, text="Logout", fg_color="red", hover_color="#c33", command=self.logout).pack(side="right", padx=10)

        # Available books area frame
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, pady=(6, 8))

        ctk.CTkLabel(frame, text="Available Books (to borrow)", font=ctk.CTkFont(weight="bold")).pack(pady=(6, 4))
        self.books_text = ctk.CTkTextbox(frame, height=320) # Textbox to list available books.
        self.books_text.pack(fill="both", expand=True, padx=12, pady=8)
        self.refresh_books_text()                       # Load the initial list of available books.

        # Action buttons for members
        ctk.CTkButton(self, text="Borrow a Book", command=self.open_borrow_window).pack(pady=6)
        ctk.CTkButton(self, text="Return a Book", command=self.open_return_window).pack(pady=6)

    def logout(self):
        """Logout and show login screen."""
        self.app.current_user = None
        self.app.show_login_frame()

    def refresh_books_text(self):
        """Show formatted list of available books in the textbox."""
        self.books_text.configure(state="normal")
        self.books_text.delete("0.0", "end")

        # Filter the main book list to include only books where 'available' is True.
        available = [(isbn, b) for isbn, b in self.app.books.items() if b.get("available", True)]
        
        if not available:
            self.books_text.insert("0.0", "No books are currently available.\n")
        else:
            lines = []
            # Add a formatted header line for readability.
            lines.append(f"{'ISBN':<16} {'Title':<36} {'Author'}")
            lines.append("-" * 80)
            
            for isbn, book in available:
                # Truncate the title to fit the display width.
                title = (book.get("title") or "")[:34]
                author = book.get("author") or ""
                # Use f-string formatting with < alignment/width specification.
                lines.append(f"{isbn:<16} {title:<36} {author}")
            self.books_text.insert("0.0", "\n".join(lines))

        self.books_text.configure(state="disabled")

    def open_borrow_window(self):
        """Open a modal where member can borrow an available book by ISBN."""
        win = ctk.CTkToplevel(self)
        win.title("Borrow a Book")
        win.geometry("420x180")

        ctk.CTkLabel(win, text="ISBN to borrow").pack(pady=(12, 4))
        isbn_e = ctk.CTkEntry(win, width=360)
        isbn_e.pack()

        def borrow():
            """Internal function to handle the member's borrowing logic."""
            isbn = isbn_e.get().strip()
            if not isbn:
                messagebox.showwarning("Input required", "Please enter ISBN.")
                return
            
            book = self.app.books.get(isbn)
            if not book or not book.get("available", True):
                messagebox.showerror("Unavailable", "Book not found or not available.")
                return
            
            # Mark borrowed in the main inventory
            self.app.books[isbn]["available"] = False
            record = {
                "isbn": isbn,
                "borrower": self.app.current_user["username"], # Use the logged-in user's name.
                "borrow_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.app.borrowed_books.append(record)
            self.app.save_all()
            self.refresh_books_text()                       # Update the list of available books.
            messagebox.showinfo("Success", "Book borrowed successfully.")
            win.destroy()

        ctk.CTkButton(win, text="Borrow", command=borrow).pack(pady=12)

    def open_return_window(self):
        """Open a modal to select a book the user borrowed and return it."""
        win = ctk.CTkToplevel(self)
        win.title("Return a Book")
        win.geometry("520x300")

        # Find books borrowed by current user
        # Filter the borrowed_books list for records matching the current user's username.
        my_borrowed = [rec for rec in self.app.borrowed_books if rec.get("borrower") == self.app.current_user["username"]]

        if not my_borrowed:
            ctk.CTkLabel(win, text="You have no borrowed books to return.").pack(pady=20)
            return

        # Show borrowed entries in a textbox for convenience
        listbox = ctk.CTkTextbox(win, height=160)
        listbox.pack(padx=12, pady=10, fill="both", expand=False)
        
        for rec in my_borrowed:
            isbn = rec.get("isbn")
            title = self.app.books.get(isbn, {}).get("title", "Unknown")
            # Insert borrowed book details into the display box.
            listbox.insert("end", f"ISBN: {isbn} | Title: {title} | Borrowed: {rec.get('borrow_date')}\n")
            
        listbox.configure(state="disabled")

        ctk.CTkLabel(win, text="Enter ISBN to return").pack(pady=(8, 4))
        isbn_e = ctk.CTkEntry(win, width=360)
        isbn_e.pack()

        def do_return():
            """Internal function to handle the member's return logic."""
            isbn = isbn_e.get().strip()
            if not isbn:
                messagebox.showwarning("Input required", "Please enter ISBN.")
                return
            
            # Iterate over a copy of the list for safe removal.
            for rec in list(self.app.borrowed_books):
                # Check if record matches ISBN AND the current borrower.
                if rec.get("isbn") == isbn and rec.get("borrower") == self.app.current_user["username"]:
                    self.app.borrowed_books.remove(rec) # Remove the record.
                    
                    if isbn in self.app.books:
                        self.app.books[isbn]["available"] = True # Mark available.
                        
                    self.app.save_all()
                    self.refresh_books_text()
                    messagebox.showinfo("Returned", "Book returned successfully.")
                    win.destroy()
                    return
            
            messagebox.showerror("Not found", "You have not borrowed a book with this ISBN.")

        ctk.CTkButton(win, text="Return", command=do_return).pack(pady=10)


# --------------------------
# Run the app
# --------------------------
if __name__ == "__main__":
    app = LibraryApp()                              # Create an instance of the main application class.
    app.run()                                       # Start the GUI application's main loop.