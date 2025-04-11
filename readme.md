# Mohit's To-Do List Manager

Mohit's To-Do List Manager is a console-based Python application that helps you organize your tasks with a colorful, easy-to-use interface. This project supports adding, viewing, editing, deleting, and marking tasks as completed. All tasks are stored persistently in a `tasks.txt` file.

## Features

- **Add a Task:** Create new tasks by providing a description and a deadline.
- **View Tasks:** Display tasks in a neatly formatted, table-like layout, grouped into "Pending" and "Completed" sections.
- **Edit Task:** Update the description or deadline of an existing task.
- **Delete Task:** Remove tasks permanently from your list.
- **Mark as Completed:** Update a task’s status to "Completed" once finished.
- **Persistent Storage:** Tasks are saved in a `tasks.txt` file so that all data persists between sessions.
- **Fancy User Interface:** Enjoy a colorful, stylish terminal interface with a cool ASCII art banner.

## Installation and Setup

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Git (optional)**: If you plan to clone the repository from GitHub.

### Getting Started

1. **Clone the Repository:**
   git clone https://github.com/your-username/to-do-list-manager.git
2. **Navigate to the Project Directory:**
    cd to-do-list-manager
3. **Run the Application:**
    python todo_list.py

## Usage
When you run the application, you are greeted with an ASCII art banner and a main menu similar to this:

████████╗ ██████╗       ██████╗  ██████╗       ██╗     ██╗███████╗████████╗
╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗      ██║     ██║██╔════╝╚══██╔══╝
   ██║   ██║   ██║█████╗██║  ██║██║   ██║█████╗██║     ██║███████╗   ██║   
   ██║   ██║   ██║╚════╝██║  ██║██║   ██║╚════╝██║     ██║╚════██║   ██║   
   ██║   ╚██████╔╝      ██████╔╝╚██████╔╝      ███████╗██║███████║   ██║   
------------------------------------------------------------
          Welcome to the Mohit's To-Do List Manager!
------------------------------------------------------------

Main Menu:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Mark Task as Completed
6. Exit
Enter your choice:


Simply follow the prompts to manage your tasks. The application ensures that every change is updated in the tasks.txt file, so your data remains intact across sessions.

## File Structure
to-do-list-manager/

├── tasks.txt        # File that stores all your task data.

├── app.py     # Main Python script containing the application logic.

└── README.md        # This file.

### todo_list.py:
Contains all the application logic including task management (add, view, edit, delete, complete) and file handling.

### tasks.txt:
Stores tasks in the following format for each line:
Task ID, Description, Deadline, Status
Example:
1,Complete the programming assignment,2024-12-25,Pending

## Contributing
Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request if you'd like to contribute to the project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.