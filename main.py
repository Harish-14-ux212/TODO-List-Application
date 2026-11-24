
from task_manager import (
    add_task,
    view_tasks,
    complete_task,
    delete_task
)


def main():
    while True:
        print("\n" + "=" * 40)
        print("          TO-DO LIST APPLICATION")
        print("=" * 40)

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        print("=" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thank you for using To-Do List Application!")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")


if __name__ == "__main__":
    main()
