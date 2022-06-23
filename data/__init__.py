import_tasks = input("Would you like to import pre-populated tasks? y/n \n")
tasks = []
if import_tasks.lower() == "y":
    from .task_list import *