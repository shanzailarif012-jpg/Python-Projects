# 📚 Library Management System

A command-line **Library Management System** built in Python using **Object-Oriented Programming (OOP)**. This project simulates real-world library operations — managing books with multiple copies, issuing and returning books to students, searching the catalog, and tracking which student has which books.

## 📌 Features

- **Add Book** — Register a new book with title, author, book ID, and total copies
- **Issue Book** — Issue a book to a student (checks copy availability first)
- **Return Book** — Return a book and update availability
- **Show All Books** — Display the full catalog with availability counts
- **Search Book** — Search books by title (case-insensitive)
- **Show Student's Books** — View all books currently issued to a specific student
- **Multiple Copies Support** — Each book tracks total copies vs. available copies
- **Menu-Driven Interface** — Simple, loop-based CLI menu for easy navigation

## 🛠️ Tech Stack

- **Language:** Python 3
- **Concepts Used:** Object-Oriented Programming (Classes, Constructors, Encapsulation), Dictionaries (including dictionary values that are lists), Loops, Conditional Logic, String Methods (`.lower()`), f-strings

## 📂 Project Structure

```
library-management-system/
│
├── library_system.py    # Main program file (Book & Library classes + program entry point)
└── README.md             # Project documentation
```

## 🧠 How It Works

The project is built using two main classes:

### `Book` Class
Represents a single book title and handles copy-level operations:
- `__init__()` — Initializes book details (title, author, book ID, total copies, available copies)
- `issue_copy()` — Reduces available copies by one (if any are available)
- `return_copy()` — Increases available copies by one (if not already at max)
- `display()` — Prints the book's details and availability

### `Library` Class
Manages the entire book catalog and student borrowing records, and drives the program:
- `__init__()` — Initializes an empty dictionary for books and an empty dictionary for student records
- `add_book()` — Creates a new `Book` object and adds it to the catalog
- `issue_book()` — Finds the book, issues a copy, and logs it under the student's record
- `return_book()` — Verifies the student actually holds the book, then returns the copy
- `show_all_books()` — Loops through and displays every book in the catalog
- `search_book()` — Searches books by title using a case-insensitive substring match
- `show_student_books()` — Displays all books currently issued to a given student
- `run()` — Runs the main menu loop until the user exits

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/shanzailarif012-jpg/<Python-Projects>.git
   ```
2. Navigate into the project folder:
   ```bash
   cd <repo-name>
   ```
3. Run the program:
   ```bash
   python library_system.py
   ```

## 🎮 Menu Options

```
1. Add Book
2. Issue Book
3. Return Book
4. Show All Books
5. Search Book
6. Show Student's Books
7. Exit
```

## 💡 Example Usage

```
Menu Options
1.Add Book
2.Issue Book
3.Return Book
4.Show All Books
5.Search Book
6.Show Student's Books
7.Exit
Enter Choice Option: 1
Enter Title: Harry Potter
Enter Author: J.K. Rowling
Enter Book_ID: B001
Enter Total_Copies: 2
Book Added Successfully
```

## ⚠️ Known Limitations

- Data is stored **only in memory** — all books and student records are lost when the program is closed (no file/database persistence yet)
- No handling for non-numeric input where numbers are expected (e.g., entering letters for "Total Copies" will crash the program)
- No due dates or fine calculation for late returns
- Book IDs must be entered exactly the same way each time (no ID auto-generation yet)

## 🚀 Future Improvements

- [ ] Add persistent storage using **JSON** or **SQLite**
- [ ] Add `try/except` error handling for invalid inputs
- [ ] Add due dates and fine calculation for late returns
- [ ] Add student registration with unique student IDs
- [ ] Search by author or book ID in addition to title
- [ ] Build a GUI or web interface (Tkinter / Flask)

## 👤 Author

**Shanzail Arif**
Dev_Shanzail 

GitHub: [@shanzailarif012-jpg](https://github.com/shanzailarif012-jpg)

## 📄 License

This project is open source and available for learning purposes.