MENU = {
    1:"Add Tasks",
    2:"View Tasks",
    3:"Remove Tasks",
    4:"Exit"
}

def add_task(tasks_list):
    """Add new task to the list."""
    # TODO: Implement task addition
    pass

def view_tasks(tasks_list):
    """Display all current tasks."""
    # TODO: Implement task viewing
    pass

def remove_task(tasks_list):
    """Remove a task from the list."""
    # TODO: Implement task removal
    pass

def show_menu(tasks_list: list) -> bool:
    """Displays the menu, handles user input, and routes to the correct function.
    
    Returns:
        bool: True if the user wants to exit, False otherwise.
    """
    print("\nWhat would you like to do:")
    for num,option in MENU.items():
        print(f"{num}. {option}")
    
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