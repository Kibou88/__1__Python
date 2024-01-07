def add_task_all(to_do_list):
    """Function to gather all functions in Add functions"""

    name, date, priority = add_message() # Function to save the command entered by user
    to_do_task = add_task(name, date, priority) # Function to add name, date, priority in a 1st list

    to_do_list.append(to_do_task) # Add the previous list in to_do_list
    return to_do_list

def add_message():
    """Function to ask to user the name, date and priority about its task"""
    name = input("What is your task? ")
    date = input("What is it due by? ")
    priority = input("What is the priority: High, Medium or Low? ")
    return name, date, priority

def add_task(name, date, priority):
    """Function to gather the datas from user and save them inside a list"""
    to_do_task = [name, date, priority]
    return to_do_task