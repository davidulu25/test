# add numbers and strings to the correct lists using the "append" list
# method
# You must add the numbers 1,2, and 3 to the "numbers" list,
# and the words 'hello' and 'world' to the strings variable


numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

for x in range(3):
    numbers.append(x + 1)

strings.append("hello")
strings.append("world")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)