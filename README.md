# task_management
Task Management Application

📌 Overview

This is a simple command-line Task Management System built in Python using SQLite for persistent storage. It allows users to create, read, update, delete, and filter tasks.

🎯 Features

Add a Task: Store tasks with a description, deadline, and status.

View All Tasks: List all tasks along with their status.

View Pending Tasks: Display only tasks that are pending.

View Completed Tasks: Display only completed tasks.

Update a Task: Modify task description or mark as completed.

Delete a Task: Remove a task permanently.

Persistent Storage: Tasks are stored in an SQLite database (tasks.db).

📂 Project Structure

|-- task_manager.py    # Main script for the task manager
|-- tasks.db           # SQLite database file (auto-generated on first run)
|-- README.md          # Documentation file

🛠 Installation & Setup

Prerequisites

Python 3.x installed on your system

Steps to Run the Application

Clone the repository (if applicable):

git clone https://github.com/arjun915/task_management.git
cd task_management

Run the script:

python task_manager.py

This will create a tasks.db(if no existing db present) file and launch the menu.

📜 Usage

Main Menu Options

When you run task_manager.py, you will see:

Task Management System
1. Add a task
2. View all tasks
3. View pending tasks
4. View completed tasks
5. Update a task
6. Delete a task
7. Exit

1️⃣ Add a Task

Enter a description

Enter a deadline (YYYY-MM-DD format, optional)

Enter a status(pending or completed)

2️⃣ View All Tasks

Displays all tasks along with their status.

3️⃣ View Pending Tasks

Shows only tasks that are still pending.

4️⃣ View Completed Tasks

Lists only completed tasks.

5️⃣ Update a Task

Enter task ID

Optionally update description or mark as completed

6️⃣ Delete a Task

Enter the task ID to remove it permanently.

7️⃣ Exit

Closes the application.

🛠 Database Schema

If using SQLite, the tasks table has the following structure:
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    deadline TEXT,
    status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL DEFAULT 'pending'
);

✅ Note

If tasks.db does not exist, it will be created automatically.

Ensure SQLite is enabled in your Python installation.