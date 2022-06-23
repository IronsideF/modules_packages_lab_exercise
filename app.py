from modules.output import *
from modules.task_list import *
# from data.task_list import *
from modules.input import *
import_tasks = input("Would you like to import pre-populated tasks? y/n \n")
tasks = []
if import_tasks.lower() == "y":
    from data.task_list import *



while (True):
    print_menu()
    option = user_option_selection()
    # option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        # description = input("Enter task description to search for: ")
        task = get_task_with_description(tasks, user_description_input())
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        # time = int(input("Enter task duration: "))
        print_list(get_tasks_taking_at_least(tasks, user_time_input()))
    elif option == '6':
        # description = input("Enter task description to search for: ")
        print(get_task_with_description(tasks, user_description_input()))
    elif option == '7':
        # description = input("Enter description: ")
        # time_taken = int(input("Enter time taken: "))
        task = create_task(user_description_input(), user_time_input())
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")