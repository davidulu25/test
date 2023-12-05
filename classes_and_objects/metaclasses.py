# datacamp - python metaclasss tutorial

# everything in python is an object
class TestClass:
    pass

my_test_class = TestClass()
print(my_test_class)

# python classes can be created dynamically
temp = type(TestClass)

print(temp)

print(type(type))

# now creating the class dynamically
class DataCamp:
    pass

DataCampClass = type('Data Camp', (), {})
print(DataCampClass)
print(DataCamp())

# code above uses another way of creating a class, which is with the built-in type() function in python.
#   the type() function takes in three arguments; the name of the new class, a tuple of base classes (which is empty in this case, and can be left empty), and a dictionary containing the attributes and methods of the new class(also empty here).

# working more indepth with type()
PythonClass = type('PythonClass', (), {'start_date': 'August 2018', 'instructor': 'John Wick'})

print(PythonClass.start_date, PythonClass.instructor)
print(PythonClass)

# using the tuple argument
PythonClass = type('PythonClass', (DataCamp,), {'start_date': 'August 2018', 'instructor': 'John Wick'})

print(PythonClass)

# __class__ attribute enables to check the TYPE of instance that it is called on

article = "(strings) metaclasses"
j = article.__class__
print (j)

# also checking type using type(type)
print(type(article))

# checking the type() of str tells us that its 'type'
print(type(str))

# checking __class__ of __class__ should return 'type'
print(article.__class__.__class__) # or ...(j.class)

# creating custom Metaclasses
# in python we can customise the class creation process by passing  the metaclass keyword into the class definition.

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass

print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))

# when defining a class and no metaclass is defined the default 'type' metaclass will be used. and, if a metaclass is given and it is not an instance of type(), then it is used directly as the metaclass.

# __new__ and __init__

class MetaOne(type):
    def __new__(cls, name, bases, dict):
        pass

class MetaTwo():
    def __init__(self, name, bases, dict):
        pass