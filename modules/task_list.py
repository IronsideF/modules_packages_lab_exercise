

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    not_complete = get_tasks_by_status(list, False)
    # for task in list:
    #     if task["completed"] == False:
    #         not_complete.append(task)
    return not_complete
    


## Get a list of completed tasks
def get_completed_tasks(list):
    complete = get_tasks_by_status(list, True)
    # for task in list:
    #     if task["completed"] == True:
    #         complete.append(task)
    return complete

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    task_list = []
    for task in list:
        if task["time_taken"] >= time:
            task_list.append(task)
    return task_list

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task

# Extension (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    task_list = []
    for task in list:
        if task["completed"] == status:
            task_list.append(task)
    return task_list

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)




