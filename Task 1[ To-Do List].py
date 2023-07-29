def print_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task(todo_dict):
    task = input("Enter a new task: ")
    todo_dict[len(todo_dict) + 1] = task
    print("Task added successfully.")

def view_tasks(todo_dict, completed_dict):
    print("Choices:")
    print_menu()
    print("\nTasks:")
    print("To Do:")
    for task_num, task in todo_dict.items():
        if task_num not in completed_dict:
            print(f"{task_num}. {task}")
    print("\nCompleted:")
    for task_num, task in completed_dict.items():
        print(f"{task_num}. \033[1m{task}\033[0m")  # Bold formatting for completed tasks

def mark_completed(todo_dict, completed_dict):
    view_tasks(todo_dict, completed_dict)
    task_num = int(input("Enter the task number to mark as completed: "))
    if task_num not in todo_dict:
        print("Invalid task number.")
    else:
        task = todo_dict.pop(task_num)
        completed_dict[task_num] = task
        print(f"Marking task '{task}' as completed.")

def delete_task(todo_dict, completed_dict):
    view_tasks(todo_dict, completed_dict)
    task_num = int(input("Enter the task number to delete: "))
    if task_num not in todo_dict:
        print("Invalid task number.")
    else:
        task = todo_dict.pop(task_num)
        print(f"Deleting task '{task}'.")

def main():
    todo_dict = {}
    completed_dict = {}
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task(todo_dict)
        elif choice == '2':
            view_tasks(todo_dict, completed_dict)
            print("\n\n")
        elif choice == '3':
            mark_completed(todo_dict, completed_dict)
        elif choice == '4':
            delete_task(todo_dict, completed_dict)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
