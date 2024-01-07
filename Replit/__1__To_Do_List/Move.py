def move_task_all(to_do_list):
    """Function to gather all Move functions"""
    number_task = len(to_do_list)

    move_task = move_message(to_do_list, number_task)
    move_test_choice(move_task, number_task)
    to_do_list = function_move_task(move_task, to_do_list, number_task)

    return to_do_list

def move_message(to_do_list, number_task):
    """Function to show Move menu and bring user choice"""
    print(f"You have {number_task} To Dos. There is: ")
    print(to_do_list)
    print(f"\nThe 1st task has number 0, the last task has number {number_task-1}.")
    move_task = int(input("Which task do you want to move? "))

    return move_task

def move_test_choice(move_task, number_task):
    """Function to test the user choice and if its between 0 and length to_do_list -1"""

    if move_task < 0 and move_task > number_task:
        print("You are choice is not good")
        print("Bye bye")
        exit()

def function_move_task(move_task, to_do_list, number_task):
    """Function to move a task"""
    print(f"You will move the task {to_do_list[move_task]}")
    if move_task == 0:
        print(f"You can move by adding an new index: 1 to {number_task}")
    elif move_task == number_task:
        print(f"You can move to modify an new index: 0 to {number_task - 1}")

    index = int(input("What's is the new position: "))
    task = to_do_list[move_task]
    to_do_list.insert(index, task)
    to_do_list.pop(move_task)
    print("There is the new list:")
    print(to_do_list)

    return to_do_list