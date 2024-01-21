def remove_task_all(to_do_list):
    """Function to gather all remove functions"""
    number_task = len(to_do_list) - 1
    edit_choice = remove_message(to_do_list, number_task)
    to_do_list = remove_task(to_do_list, edit_choice)
    return to_do_list

def remove_message(to_do_list, number_task):
    """Function to show the Remove menu and To Do List by index"""
    print("There is the To Do List:")
    for i in number_task: # Display the tasks per index
        print(f"For index {i}: the task is {to_do_list[i]}")
    remove_choice = input("What's your choice (write the index)? ")
    return remove_choice

def remove_task(to_do_list, remove_choice):
    """Function to Remove a task from the To Do List"""
    task_removed = to_do_list.pop(remove_choice)
    print("The task has been remove successful: ", task_removed)
    return to_do_list