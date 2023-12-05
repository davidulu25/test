# create two lists x_list and y_list
# that contain 10 instances of the variables x and y
# create a list called big_list, that contains
# the variables x and y 10 times each by concatenating
# the two lists created

x = object()
y = object()

# TODO: change this code
x_list = ([x] * 10)
y_list = ([y] * 10)
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")