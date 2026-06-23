task_List = []

def add_Task():

    while True:

        task = input("Enter task: ")

        if task == "":
            break

        task_List.append(task)

def remove_Task():

    remove_task = input("Enter task to remove: ")

    if remove_task in task_List:

        task_List.remove(remove_task)
    else:
        print("Task not found")

def view_Task():

    print(task_List)

add_Task()

view_Task()

remove_Task()

view_Task()