import os

file_path = "employees.txt"

if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write("Employee ID, Name, Position, Salary\n")

def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    salary = input("Enter Employee Salary: ")
    
    with open(file_path, 'a') as file:
        file.write(f"{employee_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully.")

def view_all_employees():
    with open(file_path, 'r') as file:
        records = file.readlines()
        for record in records:
            print(record.strip())

def search_employee():
    employee_id = input("Enter Employee ID to search: ")
    with open(file_path, 'r') as file:
        records = file.readlines()
        found = False
        for record in records:
            if record.startswith(employee_id):
                print(record.strip())
                found = True
                break
        if not found:
            print("Employee not found.")

def update_employee():
    employee_id = input("Enter Employee ID to update: ")
    with open(file_path, 'r') as file:
        records = file.readlines()

    updated_records = []
    found = False
    for record in records:
        if record.startswith(employee_id):
            found = True
            name = input("Enter new Name: ")
            position = input("Enter new Position: ")
            salary = input("Enter new Salary: ")
            updated_record = f"{employee_id}, {name}, {position}, {salary}\n"
            updated_records.append(updated_record)
        else:
            updated_records.append(record)
    
    if found:
        with open(file_path, 'w') as file:
            file.writelines(updated_records)
        print("Employee record updated successfully.")
    else:
        print("Employee not found.")

def delete_employee():
    employee_id = input("Enter Employee ID to delete: ")
    with open(file_path, 'r') as file:
        records = file.readlines()

    updated_records = []
    found = False
    for record in records:
        if record.startswith(employee_id):
            found = True
            print(f"Deleting record: {record.strip()}")
        else:
            updated_records.append(record)

    if found:
        with open(file_path, 'w') as file:
            file.writelines(updated_records)
        print("Employee record deleted successfully.")
    else:
        print("Employee not found.")

def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
