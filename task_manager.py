
from storage import load_tasks, save_tasks


def add_task():
    tasks = load_tasks()

    task_name = input("Enter your task: ").strip()

    if not task_name:
        print("Task cannot be empty.")
        return

    new_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": new_id,
        "title": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(f"ID: {task['id']}")
        print(f"Task: {task['title']}")
        print(f"Status: {status}")
        print("--------------------------------")


def complete_task():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed.")
            else:
                task["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
            return

    print("Task ID not found.")


def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return

    print("Task ID not found.")
