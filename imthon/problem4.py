class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def get_details(self) -> str:
        return f"Name: {self.name}, Salary: {self.salary}"

    def calculate_bonus(self) -> float:
        return 0.0

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def get_details(self) -> str:
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

    def calculate_bonus(self) -> float:
        return self.salary * 0.10

class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str) -> None:
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self) -> str:
        return f"Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}"

    def calculate_bonus(self) -> float:
        return self.salary * 0.05


emp = Employee("John Doe", 50000)
mgr = Manager("Jane Smith", 80000, "Sales")
dev = Developer("Alice Johnson", 70000, "Python")

print(emp.get_details())  
print(mgr.get_details())  
print(dev.get_details())  

print(f"{mgr.name}'s Bonus: {mgr.calculate_bonus()}")  
print(f"{dev.name}'s Bonus: {dev.calculate_bonus()}")  
