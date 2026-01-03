# Question 1
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Country: {self.country}")

p1 = Person("Ali", 25, "Pakistan")
p2 = Person("Sara", 22, "Canada")

p1.display_details()
p2.display_details()
 
# Question 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

#QUestion 3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display(self):
        print(f"{self.year} {self.make} {self.model}, Doors: {self.doors}")

car = Car("Toyota", "Corolla", 2022, 4)
car.display()

# Question 4
class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

acc = BankAccount("101", 5000)
acc.deposit(2000)
acc.withdraw(3000)
print("Balance:", acc.balance)

# Question 5
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(7)
triangle = Triangle(5, 8)

print("Circle Area:", circle.area())
print("Triangle Area:", triangle.area())

# Question 6
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, department, bonus):
        super().__init__(name, salary)
        self.department = department
        self.bonus = bonus

    def annual_salary(self):
        return (self.salary * 12) + self.bonus

m1 = Manager("Ahmed", 80000, "IT", 200000)
m2 = Manager("Ayesha", 90000, "HR", 250000)

print(m1.annual_salary())
print(m2.annual_salary())

# Question 7
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(self.title, self.author, self.year)

class Ebook(Book):
    def __init__(self, title, author, year, price):
        super().__init__(title, author, year)
        self.price = price

    def display(self):
        print(self.title, self.author, self.year, "Price:", self.price)

ebook = Ebook("Python 101", "John Doe", 2023, 15.99)
ebook.display()


# Question 8
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, color):
        super().__init__("Dog", "Bark")
        self.color = color

    def make_sound(self):
        print(f"{self.color} dog says {self.sound}")

dog = Dog("Brown")
dog.make_sound()

# Question 9
class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def remove_branch(self, branch):
        self.branches.remove(branch)

    def display_branches(self):
        print(self.branches)

bank = Bank("HBL")
bank.add_branch("Lahore")
bank.add_branch("Karachi")
bank.remove_branch("Lahore")
bank.display_branches()

# Question 10
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity

class PersonalCareProduct(Product):
    def __init__(self, pid, name, price, warranty):
        super().__init__(pid, name, price)
        self.warranty = warranty

    def total_price(self, quantity):
        return (self.price * quantity) + (self.warranty * 100)

item = PersonalCareProduct(1, "Trimmer", 3000, 2)
print(item.total_price(2))

# Question 11
class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def transfer(self, amount, target):
        if amount <= self.balance:
            self.withdraw(amount)
            target.deposit(amount)

a1 = BankAccount("1", "Ali", 5000)
a2 = BankAccount("2", "Sara", 3000)

a1.transfer(2000, a2)
print(a1.balance, a2.balance)

# Question 12
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, dept):
        self.departments.append(dept)

    def remove_department(self, dept):
        self.departments.remove(dept)

    def display_departments(self):
        print(self.departments)

uni = University("FAST")
uni.add_department("CS")
uni.add_department("AI")
uni.remove_department("AI")
uni.display_departments()
