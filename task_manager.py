import sqlite3
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                deadline TEXT,
                status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL DEFAULT 'pending'
            )
        """)
        self.conn.commit()

    def add_task(self, description, deadline=None,status=None):
        self.cursor.execute("INSERT INTO tasks (description, deadline, status) VALUES (?, ? ,?)", (description, deadline,status))
        self.conn.commit()
        print("Task added successfully!")

    def view_tasks(self, status=None):
        query = "SELECT * FROM tasks" if not status else "SELECT * FROM tasks WHERE status = ?"
        self.cursor.execute(query, (status,) if status else ())
        tasks = self.cursor.fetchall()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(task)

    def update_task(self, task_id, description=None, status=None):
        if description:
            self.cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, task_id))
        if status:
            self.cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        self.conn.commit()
        print("Task updated successfully!")

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
        print("Task deleted successfully!")

    def close(self):
        self.conn.close()

# Command-line menu
def main():
    task_manager = TaskManager()
    while True:
        print("\nTask Management System")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Update a task")
        print("6. Delete a task")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ") or None
            status = input("Enter new status (pending/completed) or leave blank: ") or None
            task_manager.add_task(desc, deadline,status)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.view_tasks("pending")
        elif choice == "4":
            task_manager.view_tasks("completed")
        elif choice == "5":
            task_id = int(input("Enter task ID to update: "))
            new_desc = input("Enter new description (or leave blank): ") or None
            new_status = input("Enter new status (pending/completed) or leave blank: ") or None
            task_manager.update_task(task_id, new_desc, new_status)
        elif choice == "6":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "7":
            print("Exiting...")
            task_manager.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
