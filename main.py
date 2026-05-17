import os
import json

# --- FILE CONFIG ---

FILE_NAME = "tasks.json"

# --- FILE HANDLING ---

"""
load_tasks() -> list
Loads saved tasks from the JSON file on disk.
Checks if the file exists; returns empty list if not
Attempts to read and parse JSON data
Handles corrupted files with error message and returns empty list
Returns: List of task dictionaries
"""

def load_tasks() -> list:
    """Load tasks from JSON file if it exists."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Corrupted file detected. Starting fresh.")
        return []

"""
save_tasks(tasks: list)
Saves the current task list to the JSON file.

Opens file in write mode

Saves tasks with 4-space indentation for readability

Called automatically after any task modification
"""

def save_tasks(tasks: list):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# --- INPUT VALIDATION HELPERS ---

"""
get_valid_int(prompt: str, min_val: int, max_val: int) -> int
Validates integer input within a range.

Continuously prompts until valid input received

Handles non-integer inputs (ValueError)

Validates number is between min_val and max_val (inclusive)

Returns: Validated integer
"""

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    """Prompts for an integer within a specific inclusive range."""
    while True:
        try:
            choice = int(input(prompt).strip())
            if min_val <= choice <= max_val:
                return choice
            print(f"❌ Invalid choice. Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid number.")


"""
get_valid_confirm(prompt: str) -> bool
Handles yes/no questions with validation.

Converts input to lowercase for case-insensitive comparison

Only accepts 'yes' or 'no'

Returns: True for 'yes', False for 'no'
"""

def get_valid_confirm(prompt: str) -> bool:
    """Prompts for a YES or NO question, returning a boolean."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print("❌ Invalid input. Please type 'YES' or 'NO'.")

"""
get_non_empty_string(prompt: str) -> str
Ensures user input isn't empty or just whitespace.

Strips whitespace from input

Rejects empty strings

Returns: Non-empty string
"""

def get_non_empty_string(prompt: str) -> str:
    """Ensures the user doesn't provide an empty string or whitespace."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("❌ Input cannot be empty. Please try again.")


# --- CORE APPLICATION FUNCTIONS ---

"""
add_task(tasks_list: list)
Creates and adds a new task to the list.

Gets validated task name (non-empty)

Gets completion status (yes/no)

Appends task dictionary: {"title": str, "complete": bool}

Prints success confirmation message
"""

def add_task(tasks_list: list):
    """Add a new task to the list with full validation."""
    task_name = get_non_empty_string("Please enter name of the task: ")
    is_complete = get_valid_confirm("Is the task complete ('YES' or 'NO'): ")

    tasks_list.append({
        "title": task_name, 
        "complete": is_complete
    })
    print(f"✅ Your task '{task_name}' was successfully added.")


"""
view_tasks(tasks_list: list)
Displays all tasks in a formatted list.

Creates centered header ("= Your tasks =")

Shows empty message if no tasks exist

Numbers tasks starting from 1

Shows status emojis: ✅ Done or ❌ Not Done

Prints separator line
"""

def view_tasks(tasks_list: list):
    """Display all current tasks."""
    print(f"\n{' Your tasks ':=^30}")
    
    if not tasks_list:
        print("There are no tasks to view.")
    else:
        for index, task in enumerate(tasks_list, 1):
            status = "✅ Done" if task["complete"] else "❌ Not Done"
            print(f"{index}. {task['title']} [{status}]")
    print("=" * 30)


"""
remove_task(tasks_list: list)
Removes a task by its displayed number.

Checks if task list is empty first

Calls view_tasks() to show current tasks

Gets validated task number (1 to list length)

Removes task using pop() (adjusts for 0-based index)

Confirms removal with task name
"""

def remove_task(tasks_list: list):
    """Remove a task from the list."""
    if not tasks_list:
        print("❌ There are no tasks to remove.")
        return
    
    view_tasks(tasks_list)
    remove_task_id = get_valid_int(
        prompt="\nPlease enter the number of the task to remove: ",
        min_val=1,
        max_val=len(tasks_list)
    )
    
    removed_task = tasks_list.pop(remove_task_id - 1)
    print(f"✅ Task '{removed_task['title']}' removed successfully.")


# --- FUNCTION MAPPING & INTERFACE ---

MENU = {
    1: ("Add Task", add_task),
    2: ("View Tasks", view_tasks),
    3: ("Remove Task", remove_task),
    4: ("Exit", None)
}


"""
run_menu_cycle(tasks_list: list) -> bool
Main menu handler - displays options and executes user choice.

Displays menu with numbered options

Gets validated choice (1-4)

Handles Exit option (choice 4) - returns True

Executes selected function from MENU dictionary

Auto-saves after any modification

Returns: True if exiting, False to continue
"""

def run_menu_cycle(tasks_list: list) -> bool:
    """Displays menu, handles input, and executes choice in a single operational layer.
    
    Returns:
        bool: True if exiting, False to continue.
    """
    print("\nWhat would you like to do:")
    for num, (option_name, _) in MENU.items():
        print(f"{num}. {option_name}")
    
    user_choice = get_valid_int("\nPlease enter your choice: ", 1, len(MENU))
    
    if user_choice == 4:
        print("\nGoodbye! Have a productive day! 👋")
        return True
        
    # Execute the chosen function
    MENU[user_choice][1](tasks_list)
    
    # Save automatically after tasks are added or removed
    save_tasks(tasks_list) 
    return False


"""
main()
Application entry point and main loop.

Prints welcome message

Loads existing tasks from file

Continuously runs menu cycles until user exits

Uses while not run_menu_cycle(tasks) to keep looping
"""

def main():
    """Main application entry point."""
    print("Welcome User!")

    tasks = load_tasks()   # Load any existing data from tasks.json

    while not run_menu_cycle(tasks):
        pass


if __name__ == "__main__":
    main()
