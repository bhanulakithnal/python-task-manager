import os
import json

# --- FILE CONFIG ---

FILE_NAME = "tasks.json"

# --- FILE HANDLING ---

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


def save_tasks(tasks: list):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# --- INPUT VALIDATION HELPERS ---

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


def get_valid_confirm(prompt: str) -> bool:
    """Prompts for a YES or NO question, returning a boolean."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print("❌ Invalid input. Please type 'YES' or 'NO'.")


def get_non_empty_string(prompt: str) -> str:
    """Ensures the user doesn't provide an empty string or whitespace."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("❌ Input cannot be empty. Please try again.")


# --- CORE APPLICATION FUNCTIONS ---

def add_task(tasks_list: list):
    """Add a new task to the list with full validation."""
    task_name = get_non_empty_string("Please enter name of the task: ")
    is_complete = get_valid_confirm("Is the task complete ('YES' or 'NO'): ")

    tasks_list.append({
        "title": task_name, 
        "complete": is_complete
    })
    print(f"✅ Your task '{task_name}' was successfully added.")


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


def main():
    """Main application entry point."""
    print("Welcome User!")

    tasks = load_tasks()   # Load any existing data from tasks.json

    while not run_menu_cycle(tasks):
        pass


if __name__ == "__main__":
    main()