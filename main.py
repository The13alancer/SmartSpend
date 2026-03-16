from task_manager import TaskManager
from storage import load_tasks, save_tasks


def display_menu():
    print("\n=== PriorityFlow Task Scheduler ===")
    print("1. Add Task")
    print("2. View Highest-Priority Task")
    print("3. Complete Highest-Priority Task")
    print("4. List Pending Tasks")
    print("5. List Completed Tasks")
    print("6. Exit")


def print_task(task):
    print(f"\nID       : {task['id']}")
    print(f"Title    : {task['title']}")
    print(f"Priority : {task['priority']}")
    print(f"Due Date : {task['due_date'] if task['due_date'] else 'N/A'}")
    print(f"Created  : {task['created_at']}")
    print(f"Status   : {task['status']}")


def main():
    data = load_tasks()
    manager = TaskManager(data["pending"], data["completed"])

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            try:
                priority = int(input("Enter priority (1 = highest, 5 = lowest): "))
            except ValueError:
                print("Priority must be a number.")
                continue

            due_date = input("Enter due date (optional): ")
            success, message = manager.add_task(title, priority, due_date)
            print(message)

            if success:
                save_tasks(manager.export_data())

        elif choice == "2":
            task = manager.peek_next_task()
            if task:
                print_task(task)
            else:
                print("No pending tasks.")

        elif choice == "3":
            success, message = manager.complete_next_task()
            print(message)

            if success:
                save_tasks(manager.export_data())

        elif choice == "4":
            tasks = manager.list_pending_tasks()
            if not tasks:
                print("No pending tasks.")
            else:
                print("\n=== Pending Tasks ===")
                for task in tasks:
                    print_task(task)

        elif choice == "5":
            tasks = manager.list_completed_tasks()
            if not tasks:
                print("No completed tasks.")
            else:
                print("\n=== Completed Tasks ===")
                for task in tasks:
                    print_task(task)

        elif choice == "6":
            if save_tasks(manager.export_data()):
                print("Tasks saved.")
            else:
                print("Warning: Could not save tasks, but exiting anyway.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
