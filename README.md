# Python Task Manager (CLI)

A simple but structured command-line task manager built in Python.  
This project was developed step-by-step to practice software engineering fundamentals, clean architecture, and Git workflow discipline.

---

## 🚀 Features

- Add new tasks with validation
- View all tasks in a formatted list
- Remove tasks by selection
- Mark tasks as complete/incomplete
- Clean interactive menu system
- Input validation and error handling

---

## 🧠 Task Data Model

Each task is stored as a Python dictionary:

```python
{
    "title": str,
    "complete": bool
}