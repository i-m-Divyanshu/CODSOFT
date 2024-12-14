# List to hold tasks
tasks_collection = []

def display_all_tasks():
    if not tasks_collection:
        print("Currently, there are no tasks to display.")
    else:
        for idx, task in enumerate(tasks_collection, start=1):
            print(f"{idx}. {task}")

def add_task_to_list():

    task_description = input("Please provide the task details: ")
    tasks_collection.append(task_description)
    print("The task has been added successfully.")

def update_existing_task():

    display_all_tasks()
    task_idx = int(input("Enter the number of the task you wish to update: "))
    if 1 <= task_idx <= len(tasks_collection):
        new_description = input("Enter the new task description: ")
        tasks_collection[task_idx - 1] = new_description
        print("The task has been updated successfully.")
    else:
        print("Invalid task number, please try again.")

def delete_task_from_list():

    display_all_tasks()
    task_idx = int(input("Enter the number of the task to delete: "))
    if 1 <= task_idx <= len(tasks_collection):
        tasks_collection.pop(task_idx - 1)
        print("The task has been removed.")
    else:
        print("Invalid task number, please try again.")

def start_application():

    while True:
        print("\n--- To-Do Task Manager ---")
        print("1. Show All Tasks")
        print("2. Add New Task")
        print("3. Modify Existing Task")
        print("4. Delete Task")
        print("5. Exit Application")
        
        selection = input("Please choose an option (1-5): ")

        if selection == '1':
            display_all_tasks()
        elif selection == '2':
            add_task_to_list()
        elif selection == '3':
            update_existing_task()
        elif selection == '4':
            delete_task_from_list()
        elif selection == '5':
            print("Thank you for using the To-Do Task Manager. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    start_application()
