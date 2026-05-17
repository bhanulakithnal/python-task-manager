MENU = {
    1:"Add Tasks",
    2:"View Tasks",
    3:"Remove Tasks",
    4:"Exit"
}

def add_task(tasks_list):
    """Add new task to the list."""
    task_name = input("Please enter name of the task: ").strip()
    if not task_name:
        print("Task name can't be empty.")
        return

    while True:
        is_complete = input("Is the task complete ('YES' or 'NO'): ").strip().lower()

        if is_complete in ['yes', 'no']:
            if is_complete == 'yes':
                is_complete = True
            else:
                is_complete = False
            break
        print("Invalid input. Please type 'YES' or 'NO'.")

    tasks_list.append({"title" : task_name, "complete":is_complete})

    print(f"✅ Your task '{task_name}' was succesfully added.")

def view_tasks(tasks_list):
    """Display all current tasks."""
    print("\n------------ Your tasks ------------")
    if tasks_list:
        for index, task in enumerate(tasks_list, 1):
            status = "✅ Done" if tasks_list["complete"] else "❌ Not done"
            print(f"{index}.{tasks_list['title']} [{status}]")
    else:
        print("There are no tasks to view.")
    print("----------------------\n")

def remove_task(tasks_list):
    """Remove a task from the list."""
    # TODO: Implement task removal
    pass

def show_menu(tasks_list)->bool:
    """Displays the menu."""
    print("\nWhat would you like to do:")
    for num, option in MENU.items():
        print(f"{num}. {option}")
    
    return handle_menu_action(tasks_list)

def handle_menu_action(tasks_list: list) -> bool:
    """Handles user input, and routes to the correct function.
    
    Returns:
        bool: True if the user wants to exit, False otherwise
    """
    try:
        user_choice = int(input("\nPlease enter your choice: ").strip())
        
        if user_choice == 1:
            add_task(tasks_list)
        elif user_choice == 2:
            view_tasks(tasks_list)
        elif user_choice == 3:
            remove_task(tasks_list)
        elif user_choice == 4:
            print("\nGoodbye! Have a productive day! 👋")
            return True
        else:
            print("Please enter a number between 1 and 4.")
    except ValueError:
        print("Please enter a number between 1 and 4.")
    return False

def main():
    """Main application entry point."""
    print("Welcome User!")

    # Keeping state local to the main function execution
    tasks = []

    while True:
        if show_menu(tasks):
            break

if __name__ == "__main__":
    main()