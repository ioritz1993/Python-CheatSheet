class Person():

    def __init__(self, name, years, city):
        self.name = name
        self.years = years
        self.city = city
        
    def __str__(self):
        return "Nombre: {}, Edad: {}, Residencia: {}".format(self.name, self.years, self.city)

        
class Employee(Person):
    
    def __init__(self, name, years, city, salary):
        # With super we can refer to the properties and methods of the parent class
        super().__init__(name, years, city)     
        self.salary = salary
    
    def __str__(self):
        print(super().__str__())
        return "Salary: {}".format(self.salary)

        
employee = Employee("Ioritz", 30, "Muskiz", "500")
print(employee)
print(isinstance(employee, Person))  # Returns True because an employee is always of type Person (Substitution Principle)

print()

person = Person("Eli", 25, "Madrid")
print(person)
print(isinstance(person, Employee))  # Returns False because a person is not always an employee (Substitution Principle)