import os
import json
from datetime import datetime

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Generate task ID
def generate_id(tasks):
    if not tasks:
        return "T101"

    numbers = [int(task["id"][1:]) for task in tasks]
    return "T" + str(max(numbers) + 1)


# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Enter High, Medium or Low.")
        return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    try:
        date = datetime.strptime(due_date, "%Y-%m-%d")
        if date.strftime("%Y-%m-%d") != due_date:
            raise ValueError
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    task = {
        "id": generate_id(tasks),
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added.")


# View tasks by priority
def view_by_priority(tasks):
    if not tasks:
        print("No tasks available.")
        return

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_tasks = sorted(
        tasks,
        key=lambda task: priority_order[task["priority"]]
    )

    for task in sorted_tasks:
        print(
            f'{task["id"]} │ {task["title"]} │ '
            f'{task["priority"]} │ {task["due_date"]}'
        )


# Show pending tasks
def show_pending(tasks):
    pending = [
        task for task in tasks
        if task["status"] == "Pending"
    ]

    if not pending:
        print("No pending tasks.")
        print("You are all caught up!")
        return

    for task in pending:
        print(
            f'{task["id"]} │ {task["title"]} │ '
            f'{task["priority"]} │ {task["due_date"]} │ Pending'
        )


# Complete a task
def complete_task(tasks):
    task_id = input("Enter task ID: ").strip().upper()

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Done":
                print(f"Task {task_id} is already completed.")
                return

            task["status"] = "Done"
            save_tasks(tasks)

            print(f"Task {task_id} marked as done.")

            pending_count = sum(
                1 for t in tasks if t["status"] == "Pending"
            )

            print(f"Pending tasks: {pending_count}")
            return

    print(f"Task {task_id} not found.")


# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n===== DAILY TASK MANAGER =====")
        print("1. Add Task")
        print("2. View by Priority")
        print("3. Show Pending Tasks")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_by_priority(tasks)

        elif choice == "3":
            show_pending(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            print("Thank you for using Daily Task Manager!")
            break

        else:
            print("Invalid menu option. Try again.")


if __name__ == "__main__":
    main()