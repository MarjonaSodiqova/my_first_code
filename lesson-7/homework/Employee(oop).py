class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    def __init__(self, filename='employees.txt'):
        self.filename = filename

    def add_employee(self, employee):
        with open(self.filename, 'a') as file:
            file.write(f"{employee}\n")
        return "Employee added successfully!"

    def view_all_employees(self):
        try:
            with open(self.filename, 'r') as file:
                employees = file.readlines()
            return [emp.strip() for emp in employees]
        except FileNotFoundError:
            return "No employee records found."

    def search_employee(self, employee_id):
        with open(self.filename, 'r') as file:
            for line in file:
                if line.startswith(employee_id):
                    return line.strip()
        return "Employee not found."

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        employees = self.view_all_employees()
        updated = False

        with open(self.filename, 'w') as file:
            for emp in employees:
                if emp.startswith(employee_id):
                    emp_data = emp.split(', ')
                    if name:
                        emp_data[1] = name
                    if position:
                        emp_data[2] = position
                    if salary:
                        emp_data[3] = salary
                    file.write(', '.join(emp_data) + '\n')
                    updated = True
                else:
                    file.write(emp + '\n')
        return "Employee updated successfully!" if updated else "Employee not found."

    def delete_employee(self, employee_id):
        employees = self.view_all_employees()
        with open(self.filename, 'w') as file:
            deleted = False
            for emp in employees:
                if not emp.startswith(employee_id):
                    file.write(emp + '\n')
                else:
                    deleted = True
        return "Employee deleted successfully!" if deleted else "Employee not found."


def main():
    manager = EmployeeManager()

    while True:
        print("\n Employee Records Manager!")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            employee = Employee(employee_id, name, position, salary)
            print(manager.add_employee(employee))
        
        elif choice == '2':
            print("Employee Records:")
            for emp in manager.view_all_employees():
                print(emp)
        
        elif choice == '3':
            employee_id = input("Enter Employee ID to search: ")
            print("Employee Found:")
            print(manager.search_employee(employee_id))
        
        elif choice == '4':
            employee_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to keep current): ") or None
            position = input("Enter new Position (leave blank to keep current): ") or None
            salary = input("Enter new Salary (leave blank to keep current): ") or None
            print(manager.update_employee(employee_id, name, position, salary))
        
        elif choice == '5':
            employee_id = input("Enter Employee ID to delete: ")
            print(manager.delete_employee(employee_id))
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()