# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")

# Function to mark a task as completed
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Task '{tasks[task_index - 1]['task']}' marked as completed.")
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        task_index = int(input("Enter the task number to mark as completed: "))
        complete_task(task_index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
