def edit_task_all(to_do_list):
    """Function to gather all edit functions"""
    number_task = len(to_do_list)
    edit_choice = edit_message(to_do_list, number_task)
    to_do_list = edit_task(to_do_list, edit_choice)
    return to_do_list

def edit_message(to_do_list, number_task):
    """Function to show the Edit menu and To Do List by index"""
    print("There is the To Do List:")
    for index, task in enumerate(to_do_list): # Display the tasks per index
        print(f"For index {index + 1}: the task is {task}")
    edit_choice = input("What's your choice (write the index)? ")
    return edit_choice

def edit_task(to_do_list, edit_choice):
    """Function to edit a task"""
    to_do_task = [] # Create an empty list
    to_do_task = to_do_list.pop[edit_choice]
    index = len(to_do_task)
    for i in to_do_task:
        modify = input(f"Do you want to edit this: {i}")
        if modify.split().lower() == "yes":
            to_do_task[index] = input("New entry: ")
            index += 1
        elif modify.split().lower() == "no":
            break
    to_do_list.append(to_do_task)
    print(f"There is the new To Do List: \n {to_do_list}")
    return to_do_list