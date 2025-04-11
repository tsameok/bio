import os

class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task added: {task}')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f'Task removed: {removed_task}')
        else:
            print("Invalid task number.")

def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            manager.add_task(task)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: ")) - 1
                manager.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
