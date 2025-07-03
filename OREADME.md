<!-- <!-- ** Reggie's 🐍 Python Level-Up Project that progresses in skill level. It includes: -->

* An intro
* Basic Python commands
* Class & method building
* API creation
* A final capstone project goal

# 🐍 Python Level-Up Project

Welcome! This is a hands-on tutorial and self-guided learning path to help you become proficient in Python through real code, not just theory. It’s designed to walk you through:

1. Basic Python commands
2. Writing classes and methods
3. Creating a basic API
4. Building a final capstone project: a rotating assignment web app

---

## 🧰 Step 1 — Python Basics

Before building anything advanced, master the basics. Here are some fundamental Python commands and concepts.

### Variables and Types
```python
name = "Alice"
age = 30
is_active = True
````

### Lists and Loops

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Conditionals

```python
if age > 18:
    print("Adult")
else:
    print("Minor")
```

### Functions

```python
def greet(name):
    return f"Hello, {name}!"
```

---

## 🧱 Step 2 — Building Classes and Methods

Object-Oriented Programming (OOP) lets you organize and structure code for reuse and clarity.

### Create a Class

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def summary(self):
        return f"{self.title} by {self.author}"
```

### Instantiate and Use the Class

```python
my_book = Book("1984", "George Orwell")
print(my_book.summary())
```

---

## 🌐 Step 3 — Create a Basic API (with Flask)

Flask is a lightweight Python framework for building web APIs.

### Install Flask

```bash
pip install flask
```

### Example Flask App

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify(message="Pong!")

if __name__ == '__main__':
    app.run(debug=True)
```

Run the app:

```bash
python app.py
```

---

## 🎯 Final Goal — Weekly Assignment Web App

By the end of this project, you’ll build a small website that:

* Shows a list of weekly reading assignments
* Rotates the list based on a number someone calls out at the end of a meeting (e.g., rotates by 3 items)
* Stores the list using Python structures (or optionally a database)
* Has a simple web interface (optional using Flask or FastAPI)

### Stretch Goals

* Add a form for inputting new readings
* Use sessions or save state to remember past rotations
* Add search capabilities for the user b/c it has a databse
* Deploy the app using Render or Replit

---

## 🔁 How to Use This Project

1. Clone this repo and work through each section step by step.
2. Add your own notes and commit changes as you learn.
3. Share your progress or get feedback by opening issues or PRs.
4. Keep pushing yourself — every few weeks, revisit and refactor!

Happy hacking 🚀

