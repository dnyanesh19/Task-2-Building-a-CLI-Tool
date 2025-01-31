import argparse
import json
import os

TASKS_FILE = "tasks.json"  # This file will store the tasks

# Load existing tasks from a JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"Task '{task_name}' added!")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if tasks:
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not done"
            print(f"{index + 1}. {task['task']} - {status}")
    else:
        print("No tasks found!")

# Mark a task as complete
def complete_task(task_index):
    tasks = load_tasks()
    try:
        task = tasks[task_index - 1]  # Index starts from 1 in CLI
        task["done"] = True
        save_tasks(tasks)
        print(f"Task {task_index} marked as complete!")
    except IndexError:
        print("Invalid task number!")

# Delete a task
def delete_task(task_index):
    tasks = load_tasks()
    try:
        task = tasks.pop(task_index - 1)  # Remove task by index
        save_tasks(tasks)
        print(f"Task '{task['task']}' deleted!")
    except IndexError:
        print("Invalid task number!")

# Main function to handle command-line input
def main():
    parser = argparse.ArgumentParser(description="Task Management CLI Tool")
    
    # Add command options
    parser.add_argument("-a", "--add", help="Add a new task", type=str)
    parser.add_argument("-l", "--list", help="List all tasks", action="store_true")
    parser.add_argument("-c", "--complete", help="Mark a task as complete", type=int)
    parser.add_argument("-d", "--delete", help="Delete a task", type=int)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Add task
    if args.add:
        add_task(args.add)
    
    # List tasks
    elif args.list:
        list_tasks()
    
    # Complete a task
    elif args.complete:
        complete_task(args.complete)
    
    # Delete a task
    elif args.delete:
        delete_task(args.delete)
    
    else:
        print("Invalid command! Use -h for help.")

if __name__ == "__main__":
    main()
