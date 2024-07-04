import os

TODO_FILE = 'todo_list.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        tasks = [line.strip() for line in file]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)
    task_no = int(input("Enter the task number to update: "))
    if 0 < task_no <= len(tasks):
        new_task = input("Enter the new task description: ")
        tasks[task_no - 1] = new_task
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    task_no = int(input("Enter the task number to delete: "))
    if 0 < task_no <= len(tasks):
        tasks.pop(task_no - 1)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
