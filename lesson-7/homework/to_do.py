import json
import csv
class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title, description, due_date=None, status='Pending'):
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        return "Task added successfully!"

    def view_tasks(self):
        return [task.to_dict() for task in self.tasks]

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title: task.title = title
                if description: task.description = description
                if due_date: task.due_date = due_date
                if status: task.status = status
                return "Task updated successfully!"
        return "Task not found."

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        return "Task deleted successfully!"

    def filter_tasks(self, status):
        return [task.to_dict() for task in self.tasks if task.status == status]

    def save_tasks(self, filename, format):
        if format == 'json':
            with open(filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f)
        elif format == 'csv':
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
                writer.writeheader()
                for task in self.tasks:
                    writer.writerow(task.to_dict())

    def load_tasks(self, filename, format):
        self.tasks = []
        if format == 'json':
            with open(filename, 'r') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task(**task_data)
                    self.tasks.append(task)
        elif format == 'csv':
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    task = Task(row['task_id'], row['title'], row['description'], row['due_date'], row['status'])
                    self.tasks.append(task)
def main():
    manager = TaskManager()
    while True:
        print("\n1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            print(manager.add_task(task_id, title, description, due_date, status))
        elif choice == '2':
            print("Tasks:")
            for task in manager.view_tasks():
                print(task)
        elif choice == '3':
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep current): ") or None
            description = input("Enter new Description (leave blank to keep current): ") or None
            due_date = input("Enter new Due Date (leave blank to keep current): ") or None
            status = input("Enter new Status (leave blank to keep current): ") or None
            print(manager.update_task(task_id, title, description, due_date, status))
        elif choice == '4':
            task_id = input("Enter Task ID to delete: ")
            print(manager.delete_task(task_id))
        elif choice == '5':
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            print("Filtered Tasks:")
            for task in manager.filter_tasks(status):
                print(task)
        elif choice == '6':
            filename = input("Enter filename to save tasks: ")
            format = input("Enter format (json/csv): ")
            manager.save_tasks(filename, format)
            print("Tasks saved successfully!")
        elif choice == '7':
            filename = input("Enter filename to load tasks: ")
            format = input("Enter format (json/csv): ")
            manager.load_tasks(filename, format)
            print("Tasks loaded successfully!")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()