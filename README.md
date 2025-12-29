# major project for my job grow data structures and algorithms internship program 

# 📚 Library Management System (Linked List Based)

A **console-based Library Management System** implemented in Python using a **singly linked list** as the core data structure.  
This project intentionally avoids Python’s built-in containers (like `dict`) to strengthen understanding of **data structures, OOP, and program design**.

---

## 🚀 Features

- Add new books to the library
- Increase stock of existing books
- Remove books (only if no copies are issued)
- Issue books
- Return books
- Search books by **name or author**
- Display all available books
- Robust input validation and error handling
- Platform-independent terminal UI (Windows / Linux / macOS)

---

## 🧠 Core Concepts Used

- Object-Oriented Programming (OOP)
- Singly Linked List (manual implementation)
- Encapsulation and abstraction
- Exception handling (`ValueError`)
- Modular design principles
- Console User Interface (CUI)

---

## 🏗 Project Structure

library_system/
│
├── main.py # Entry point (menu & user interaction)
├── library.py # Core library logic (linked list operations)
├── models.py # Data models (Book class)
├── utils.py # Helper utilities (clear screen, pause)
└── README.md # Project documentation


---

## 📘 Data Structure Design

### Book Node
Each book is represented as a node in a singly linked list.

**Attributes:**
- `name`
- `ID`
- `author`
- `total`
- `available`
- `next` (pointer to next book)

---

### Library
The `Library` class manages the linked list and exposes all operations such as:
- Add / remove books
- Issue / return books
- Search and list books

---

## 🧪 Operations Supported

| Operation      | Description |
|----------------|-------------|
| Add Book       | Adds a new book with a unique ID |
| Add Stock      | Increases total and available copies |
| Remove Book    | Removes a book only if no copies are issued |
| Issue Book     | Decreases available count |
| Return Book    | Increases available count |
| Search Book    | Search by name or author |
| List Books     | Display all books |

---

## ⚠ Constraints Enforced

- Book IDs must be unique
- Total stock must be positive
- Books cannot be removed if copies are issued
- Books cannot be issued if out of stock
- Books cannot be returned if none were issued

---

## ▶️ How to Run

### Requirements
- Python **3.10+** (required for `match-case`)

### Run the program
```bash
python main.py

# 👤 Author

Developed by Srijan Kargupta
Focused on mastering data structures, OOP, and backend fundamentals through hands-on projects.