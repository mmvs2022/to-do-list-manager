import os
import time

# ANSI escape sequences for colors and styles
RESET   = "\033[0m"
BOLD    = "\033[1m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"

TASKS_FILE = 'tasks.txt'

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Prints a fancy ASCII art banner and border."""
    clear_screen()
    banner = f"""
{BOLD}{CYAN}
████████╗ ██████╗       ██████╗  ██████╗       ██╗     ██╗███████╗████████╗
╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗      ██║     ██║██╔════╝╚══██╔══╝
   ██║   ██║   ██║█████╗██║  ██║██║   ██║█████╗██║     ██║███████╗   ██║   
   ██║   ██║   ██║╚════╝██║  ██║██║   ██║╚════╝██║     ██║╚════██║   ██║   
   ██║   ╚██████╔╝      ██████╔╝╚██████╔╝      ███████╗██║███████║   ██║   
{RESET}
    """
    print(banner)
    print(BOLD + MAGENTA + "=" * 60 + RESET)
    print(BOLD + YELLOW + "          Welcome to the Mohit's To-Do List Manager!" + RESET)
    print(BOLD + MAGENTA + "=" * 60 + RESET + "\n")

def load_tasks():
    """
    Load tasks from the tasks file.
    Each task is stored as: id,description,deadline,status
    Returns a list of dictionaries.
    """
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) < 4:
                    continue
                try:
                    task = {
                        'id': int(parts[0].strip()),
                        'description': parts[1].strip(),
                        'deadline': parts[2].strip(),
                        'status': parts[3].strip()
                    }
                    tasks.append(task)
                except ValueError:
                    continue
    return tasks

def save_tasks(tasks):
    """
    Save tasks to the tasks file.
    Overwrites the file with the current tasks list.
    """
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            line = f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n"
            file.write(line)

def get_next_id(tasks):
    """
    Determine the next task ID based on the maximum existing task ID.
    """
    if not tasks:
        return 1
    else:
        max_id = max(task['id'] for task in tasks)
        return max_id + 1

def add_task():
    """
    Prompt the user for a new task description and deadline,
    then save the new task to the file.
    """
    clear_screen()
    print_banner()
    tasks = load_tasks()
    description = input(GREEN + BOLD + "Enter task description: " + RESET)
    deadline = input(GREEN + BOLD + "Enter deadline (YYYY-MM-DD): " + RESET)
    new_task = {
        'id': get_next_id(tasks),
        'description': description,
        'deadline': deadline,
        'status': 'Pending'
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(GREEN + "\nTask added successfully! (Task saved to tasks.txt)" + RESET)
    time.sleep(2)

def view_tasks():
    """
    Display the list of tasks in a formatted, table-like layout,
    grouping them by status (Pending and Completed).
    """
    clear_screen()
    print_banner()
    tasks = load_tasks()
    
    print(BOLD + BLUE + "To-Do List Overview" + RESET)
    print("=" * 60)
    
    if not tasks:
        print(YELLOW + "No tasks found. Your to-do list is empty!" + RESET)
    else:
        # Separate tasks by their status
        pending_tasks = [task for task in tasks if task['status'].lower() == 'pending']
        completed_tasks = [task for task in tasks if task['status'].lower() == 'completed']
        
        # Display pending tasks
        print(MAGENTA + "\nPending Tasks:" + RESET)
        if pending_tasks:
            header = f"{'ID':<5} {'Task Description':<40} {'Deadline':<15}"
            print(BOLD + header + RESET)
            print(BOLD + "-" * len(header) + RESET)
            for task in pending_tasks:
                print(f"{CYAN}{str(task['id']):<5} {task['description']:<40} {task['deadline']:<15}{RESET}")
        else:
            print(YELLOW + "   No pending tasks." + RESET)
        
        # Display completed tasks
        print(MAGENTA + "\nCompleted Tasks:" + RESET)
        if completed_tasks:
            header = f"{'ID':<5} {'Task Description':<40} {'Deadline':<15}"
            print(BOLD + header + RESET)
            print(BOLD + "-" * len(header) + RESET)
            for task in completed_tasks:
                print(f"{CYAN}{str(task['id']):<5} {task['description']:<40} {task['deadline']:<15}{RESET}")
        else:
            print(YELLOW + "   No completed tasks." + RESET)
    
    input("\nPress Enter to return to the main menu...")


def edit_task():
    """
    Edit the description and deadline of an existing task.
    """
    clear_screen()
    print_banner()
    tasks = load_tasks()
    if not tasks:
        print(YELLOW + "No tasks to edit." + RESET)
        time.sleep(2)
        return

    try:
        task_id = int(input(GREEN + "Enter the task ID to edit: " + RESET))
    except ValueError:
        print(RED + "Invalid input. Please enter a valid task ID." + RESET)
        time.sleep(2)
        return

    found = False
    for task in tasks:
        if task['id'] == task_id:
            found = True
            new_description = input(GREEN + "Enter new description (leave blank to keep current): " + RESET)
            new_deadline = input(GREEN + "Enter new deadline (YYYY-MM-DD) (leave blank to keep current): " + RESET)
            if new_description:
                task['description'] = new_description
            if new_deadline:
                task['deadline'] = new_deadline
            save_tasks(tasks)
            print(GREEN + "\nTask updated successfully!" + RESET)
            time.sleep(2)
            break

    if not found:
        print(RED + "Task not found." + RESET)
        time.sleep(2)

def delete_task():
    """
    Delete a task by its ID.
    """
    clear_screen()
    print_banner()
    tasks = load_tasks()
    if not tasks:
        print(YELLOW + "No tasks to delete." + RESET)
        time.sleep(2)
        return

    try:
        task_id = int(input(GREEN + "Enter the task ID to delete: " + RESET))
    except ValueError:
        print(RED + "Invalid input. Please enter a valid task ID." + RESET)
        time.sleep(2)
        return

    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(updated_tasks) == len(tasks):
        print(RED + "Task not found." + RESET)
        time.sleep(2)
    else:
        save_tasks(updated_tasks)
        print(GREEN + "\nTask deleted successfully!" + RESET)
        time.sleep(2)

def mark_completed():
    """
    Mark a given task as completed.
    """
    clear_screen()
    print_banner()
    tasks = load_tasks()
    if not tasks:
        print(YELLOW + "No tasks to mark as completed." + RESET)
        time.sleep(2)
        return

    try:
        task_id = int(input(GREEN + "Enter the task ID to mark as completed: " + RESET))
    except ValueError:
        print(RED + "Invalid input. Please enter a valid task ID." + RESET)
        time.sleep(2)
        return

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            save_tasks(tasks)
            print(GREEN + "\nTask marked as completed!" + RESET)
            time.sleep(2)
            return

    print(RED + "Task not found." + RESET)
    time.sleep(2)

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        clear_screen()
        print_banner()
        print(BOLD + CYAN + "Main Menu:" + RESET)
        print(CYAN + "1. Add Task" + RESET)
        print(CYAN + "2. View Tasks" + RESET)
        print(CYAN + "3. Edit Task" + RESET)
        print(CYAN + "4. Delete Task" + RESET)
        print(CYAN + "5. Mark Task as Completed" + RESET)
        print(CYAN + "6. Exit" + RESET)
        choice = input(GREEN + "\nEnter your choice: " + RESET)
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_completed()
        elif choice == '6':
            clear_screen()
            print_banner()
            print(YELLOW + "Exiting the Fancy To-Do List Manager. Goodbye!" + RESET)
            time.sleep(2)
            break
        else:
            print(RED + "Invalid choice. Please try again." + RESET)
            time.sleep(2)

if __name__ == "__main__":
    main_menu()
