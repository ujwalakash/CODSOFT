class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, due_date=None):
        task = {'name': task_name, 'completed': False, 'due_date': due_date}
        self.tasks.append(task)
        print(f"Task '{task_name}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("\n--- Your To-Do List ---")
        for i, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else " "
            due_info = f" (Due: {task['due_date']})" if task['due_date'] else ""
            print(f"{i + 1}. [{status}] {task['name']}{due_info}")
        print("-----------------------")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f"Task '{self.tasks[task_index]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    def update_task(self, task_index, new_name=None, new_due_date=None):
        if 0 <= task_index < len(self.tasks):
            if new_name:
                self.tasks[task_index]['name'] = new_name
            if new_due_date:
                self.tasks[task_index]['due_date'] = new_due_date
            print(f"Task '{self.tasks[task_index]['name']}' updated.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['name']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (optional, e.g., YYYY-MM-DD): ")
            todo_list.add_task(task_name, due_date if due_date else None)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                task_num = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_completed(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            try:
                task_num = int(input("Enter the task number to update: ")) - 1
                new_name = input("Enter new task name (leave blank to keep current): ")
                new_due_date = input("Enter new due date (leave blank to keep current): ")
                todo_list.update_task(task_num, new_name if new_name else None, new_due_date if new_due_date else None)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            try:
                task_num = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '6':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()