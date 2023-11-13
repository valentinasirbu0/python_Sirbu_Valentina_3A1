class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, Salary: ${self.salary}, Department: {self.department}"

    def manage_team(self):
        return f"{self.name} is managing the {self.department} team."


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        return f"{super().display_info()}, Salary: ${self.salary}, Programming Language: {self.programming_language}"

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        return f"{super().display_info()}, Salary: ${self.salary}, Sales Target: ${self.sales_target}"

    def make_sale(self):
        return f"{self.name} made a sale and met the sales target."


manager = Manager(name="John Smith", employee_id=1001, salary=80000, department="Marketing")
print(manager.display_info())
print(manager.manage_team())

engineer = Engineer(name="Alice Johnson", employee_id=2001, salary=90000, programming_language="Python")
print(engineer.display_info())
print(engineer.write_code())

salesperson = Salesperson(name="Bob Miller", employee_id=3001, salary=75000, sales_target=150000)
print(salesperson.display_info())
print(salesperson.make_sale())
