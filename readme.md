# Library Management System

This is a basic **Library Management System** written in Python.  
It was created as part of a university assignment.

## 🎯 Task Description

The goal was to build an object-oriented system with the following:

- Classes: `Book`, `LibraryMember`, `StudentMember`, `TeacherMember`, and `Library`
- Features: Borrowing and returning books
- OOP concepts: Inheritance, Encapsulation, Polymorphism

## 🧱 Class Overview

- **Book**: Stores book info (title, author, availability)
- **LibraryMember**: Base class with borrow/return logic
- **StudentMember**: Inherits from `LibraryMember`, max 2 books
- **TeacherMember**: Inherits from `LibraryMember`, max 5 books
- **Library**: Manages books and members

## ⚙️ How it works

1. A `Library` object is created.
2. Books are added to the library.
3. A `StudentMember` and `TeacherMember` are created.
4. They borrow and return books based on their limits.
5. Console prints show what happens.

## ▶️ Example Output

```python
Emre borrowed 'Python Crash Course'
Emre borrowed 'Head First Python'
Borrowing limit reached
Mr.Bhuiyan borrowed 'Fluent Python'
Mr.Bhuiyan borrowed 'Effective Python'
...

📌 Notes
The borrowing limit is enforced

Availability is tracked

Code uses simple, clean OOP principles

🛠️ Requirements
Python 3.x

No external libraries

🧑‍💻 Author
Emre Eren – @E2xCoder