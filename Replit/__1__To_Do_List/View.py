def view_task_all(to_do_list):
    """Function to gather all functions in View modules"""
    if to_do_list != []: # If the list is not empty
        view_choice = view_message() # Function to show the View menu with options and input user
        view_test_choice(view_choice) # Function to test the user's choice, if it's not good => bye bye

        if view_choice == "1":
            view_all(to_do_list) # Function to show all To Do List
        elif view_choice == "2":
            view_priority_sort_list(to_do_list) # Function to show all To Do List sorted by priority

def view_message():
    """Function to show the type of view and ask the user to choice"""
    print("You have 2 choices:")
    print("1. View all task in To Do list")
    print("2. View tasks by priority in this order: High, Medium, Low")
    view_choice = input("What's your choice? ")
    return view_choice

def view_test_choice(view_choice):
    """Function to test the user's choice
    If choice is not good => break"""
    if view_choice != "1" and view_choice != "2":
        print("Your choice is not good!")
        print("Au revoir!!")
        exit()

def view_all(to_do_list):
    """Function to show all To Do List"""
    print("There are all To Do List:")
    print(to_do_list)
    print("\n")

def view_priority_sort_list(to_do_list):
    """Function to show the To Do List about the priority from the highest to the lowest"""
    priority_order ={"High": "0", "Medium": "1", "Low": "2"}
    to_do_list.sort(key=lambda x: priority_order[x[2]]) # Sort the list function to the sub list index 2 (priority)
    print("There is the To Do List sorted by priority:")
    print(to_do_list)
