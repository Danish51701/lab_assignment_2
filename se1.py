class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def display_table(self):
        for emp in self.employees:
            print("{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

    def sort_table(self, key):
        if key == 1:  # Sort by Age
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:  # Sort by Name
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:  # Sort by Salary
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter")

# Sample data
employee1 = Employee("161E90", "Ramu", 35, 59000)
employee2 = Employee("171E22", "Tejas", 30, 82100)
employee3 = Employee("171G55", "Abhi", 25, 100000)
employee4 = Employee("152K46", "Jaya", 32, 85000)

# Create EmployeeTable
employee_table = EmployeeTable()
employee_table.add_employee(employee1)
employee_table.add_employee(employee2)
employee_table.add_employee(employee3)
employee_table.add_employee(employee4)

# User input for sorting parameter
sorting_option = int(input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))
employee_table.sort_table(sorting_option)

# Display sorted table
print("\nSorted Employee Table:")
employee_table.display_table()
