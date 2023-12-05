# 30-11-2023

# using example of creating a class called Square
# to illustrate how '__init__' works

class Square:
    def __init__(self, sidelength):
        print("Inside init!")
        self.sidelength = sidelength

# adding this bit would create
# a sq object even though the init function
# was not explicitly called
sq = Square(1)
# "Inside init!" is the expected output

# code to show how python automaticallycalls 
# the __contains__method, when creating a program
# to check if a value is contained in an array
my_list = [2, 4, 6]

print(3 in my_list)

# __missing__ is a dunder method, and can be tested
class DictSubclass(dict):
    def __missing__ (self, key):
        print("Hello world!")

my_dict = DictSubclass()
my_dict["this key isn't available"]