#hello World
#Task Manager assignment

class Task:
    # A class Task that defines the data and logic for tasks
    def __init__(self, description, urgency):
        # init is a function that contains the field variables of Task
        # description describes the name of the task
        self.description = description
        # Urgency will be used to set the urgency of the added tasks
        self.urgency = urgency
        # 'completed' here is a part of the set status of the task
        self.completed = False

    def complete(self):
        # complete here is the function used to declare that the status of the task is completed
        self.completed = True

    def __str__(self):
        # this function prints out the task that the user wants to see in the form of an 'f' statement.
        # status here defaults the status of a task to 'Pending' if the user has not completed the task
        status = "Completed" if self.completed else "Pending"
        # The 'f' statement that will be printed out
        return f"[{status}] {self.description} (Urgency: {self.urgency})"
    
class TaskManager:
    # A class TaskManager that Implements the logic for managing multiple tasks
    def __init__(self):
        # init creates the list in which the Tasks would be stored
        self.tasks = []

    def add_task(self, description, urgency):
            # this function adds and creates the task by taking the given vlaues from the use. 
            task = Task(description, urgency)
            # the append function adds the created taskto the list
            self.tasks.append(task)
            # 'f' statement of this function
            print(f"Task added: {task}")

    def complete_task(self, task_index):
        # this function pulls out the task out of the list to be declared completed. This function requires the user to enter the index of the tasks.
        if 0 < task_index < len(self.tasks):
                # this is a loop that pulls out the task with the specified index number. You can do something similar with a for loop
                self.tasks[task_index].complete()
                print(f"Task completed: {self.tasks[task_index]}")
        else:
                print("Invalid task index.")

    def view_tasks(self):
        # this function pulls out the tasks using their specified index numbers for the user to be viewed
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

    def view_completed_tasks(self):
        # this function creates a different list of tasks using their status 'completed' to compile them.
        completed_tasks = [task for task in self.tasks if task.completed]
        if not completed_tasks:
            print("No completed tasks.")
        else:
            print("Completed Tasks:")
        for task in completed_tasks:
            print(task)

    def view_incomplete_tasks(self):
        # this function creates a different list of tasks using their status 'Pending' to compile them.
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if not incomplete_tasks:
            print("No incomplete tasks.")
        else:
            print("Incomplete Tasks:")
        for task in incomplete_tasks:
                print(task)
def app():
    # the function that Implements the interactivity with the user (inputs/outputs).
    task_manager = TaskManager()

    while True:
        print("Hello there user, this is Task Manager !")
        print("Here to help you keep up with your daily life .")
        print("You can do the following things by pressing their index numbers :")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View All Tasks")
        print("4. View Completed Tasks")
        print("5. View Incomplete Tasks")
        print("6. Exit")
        print("Enjoy :)")

        choice = input("Choose an option (1-6): ")
        # choice is the variable for the input that the user chooses to do

        if choice == '1':
            description = input("Enter task description: ")
            urgency = input("Enter task urgency (1-5): ")
            task_manager.add_task(description, urgency)
        elif choice == '2':
            task_manager.view_incomplete_tasks()
            task_index = int(input("Enter the index of the task to complete: "))
            task_manager.complete_task(task_index)
        elif choice == '3':
            task_manager.view_tasks()
        elif choice == '4':
            task_manager.view_completed_tasks()
        elif choice == '5':
            task_manager.view_incomplete_tasks()
        elif choice == '6':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    # I dont know how this works lol. :)
    app()

    # The end 
    # Thank You
