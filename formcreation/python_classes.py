class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("John", 36)

print(person.name)
print(person.age)

class School:
    def __init__(self, name):
        self.school_name = name
        
        def school(self):
            print(f"School name is: {self.school_name}")
            
            
class BankAccount:
    def __init__(self, balance):
        self.balance = balance #Encapsulation: Keeping balance inside the clas
        
        def deposit(self, amount):
            self.balance = self.balance + amount

            
        def withdraw(self, amount):
            self.balance = self.balance - amount
            print(f"Balance is: {self.balance}")