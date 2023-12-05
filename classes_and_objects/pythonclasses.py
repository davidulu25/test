# 27-11-2023
# creating a class
class Medicine:
    arm = "department"

    def responsibility(x):
        print("is supposed to be practicing in 'x' way")


# creating an object (an instance) of Medicine

radiologist = Medicine()

radiologist.arm = "x-rays"
radiologist.responsibility()


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
    # your code goes here
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

car1 = Vehicle("Fer", "convertible", "red", 60000.00)
car2 = Vehicle("Jump", "van", "blue", 10000.00)

# test code
print(car1.description())
print(car2.description())

# 28-11-2023

import array

# creating a Student class
class Students:
    # initialising attributes
    # with a Constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

#creating an object to test Students class
Ru = Students("Rhuoma", 21, "year 2")

print(Ru.grade)

# creating an empty class

# class Empty:

# zero = Empty()

class Empty:
    pass

zero = Empty()

# creating a program to name attributes in an array import file
for name in array.__dict__:
    print (name)

class Flashcard:
    # assigning variables(values) 'Word and 'Meaning
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        # using __str__ to return a string
        # copied this part
        return self.word + '(' + self.meaning + ')'

# almost gave up here

flash = []
print("welcome to python flashcard")

# making a loop to repeat
# until the user stops adding the cards
while(True):
    # wow so this is how to use input in python
    word = input("word: ")
    meaning = input("enter the meaning of the word: ")

    # 🙄
    flash.append(Flashcard(word, meaning))
    option = int (input("enter 0 if you want to add another flashcard: "))
    
    if(option):
        break

# printing all the flashcards
print("\nYour flashcards")    
for i in flash:
    print(">", i)

# creating a Vehicle class
class Vehicle:
    max_speed = ""
    mileage = ""

# creating a Teacher class that inherits
# properties from a Staff parent class
class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Role:", self.role)
        print("Department:", self.dept)
    
# inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # initialise the Parent class
        super().__init__("Teacher", "Science", 25000)

        
teacher = Teacher("Ayo", 29)

# access the Staff method
teacher.show_details()

# 29-11-2023

# creating an empty Vehicle class
class Vehicle:
    pass

# creating a Vehicle class with a child class named Bus
# make capacity function for bus as 50 through inheritance
# create bus child that inherits from vehicle class
# check type of an object
class Vehicle:
    # class attribute/variable
    colour = "white"

    # instance attributes/variables
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
    def print_specs(self):
        print("Vehicle Name:", self.name, "Speed:", self.max_speed, "Mileage:", self.mileage)

    def fare_charge(self, capacity):
        formula = capacity * 100
        return formula

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
       super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self, capacity=50):
       return super().seating_capacity(capacity=50)

    def fare_charge(self, capacity=50):
       formula = (super().fare_charge(capacity=50) + 0.10 * (super().fare_charge(capacity=50)))
       return formula

bus = Bus("School Volvo", 120, 12)
bus.print_specs()

big_bus = Bus("Volvo", 180, 12)
print(big_bus.seating_capacity())

print(bus.colour)

print("Total bus fare is $", bus.fare_charge())

print(type(big_bus))

if (isinstance(big_bus, Vehicle) == True):
    print("big bus is instance of parent class 'Vehicle'")

# Class Polymorphism
# an example that illustrates the classes 'Car', 'Boat' and 'Plane'
# that have a method called move{}:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

# instantiates Car
car1 = Car("Ford", "Mustang")

# instantiates Boat
boat1 = Boat("Ibiza", "Touring 20")

# instantiates Plane
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()
# because of polymorphism, we can use the for loop to execute the same method for the three classes