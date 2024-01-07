from IHM import *
import os


to_do_list = [] # Initialization of empty list
if __name__ == '__main__':

    while True:
        os.system("cls")
        main_page()  # Show the main menu
        choice = user_choice()  # Ask to the user its choice
        leave_program(choice)  # If user wrote "exit", end of the program
        program_choiced(choice, to_do_list)  # Access to the different menu about the user's choice




