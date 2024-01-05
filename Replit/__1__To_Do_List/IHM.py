def main_page():
    """Function to show the main menu to the user"""
    print("Welcome to the To Do List:")
    print("1 - Add a To Do")
    print("2 - View a To Do")
    print("3 - Move a To Do")
    print("4 - Edit a To Do")
    print("5 - Remove a To Do")
    print("exit - To quit the program\n")


def user_choice():
    """Function which permit to the user a choice"""
    choice = input("What's is your choice: ")
    return choice


def leave_program(choice):
    """Function to test if the user wrote 'exit'

    The word can be in different manner
    The function will convert in lower case"""
    if choice.lower() == "exit":
        print("Bye bye")
        exit()


def program_choiced(choice, to_do_list):
    """Function to access in the different menu about the user choice"""
    from Add import add_task_all
    from View import view_task_all
    # from Move import *
    # from Edit import *
    # from Remove import *

    match choice:
        case "1":
            name = "Add"
            welcome_message(name)
            to_do_list = add_task_all(to_do_list)
            # print(to_do_list)
            return to_do_list
        case "2":
            name = "View"
            welcome_message(name)
            view_task_all(to_do_list)
        case "3":
            name = "Move"
            welcome_message(name)
        case "4":
            name = "Edit"
            welcome_message(name)
        case "5":
            name = "Remove"
            welcome_message(name)
        case _:
            print("Your choice is out of the list")
            print("Bye bye")
            exit()

def welcome_message(name):
    """Function to show a welcome message
    It's the same message for all choices. ONLY the name change"""
    import os
    os.system("cls")
    print(f"\nWelcome to {name} menu\n")