# w3docs-pythonstrings

string_var ="hello, {}".format("world")
print(string_var)

# string slicing
string_var = "hello"
print(string_var[1:4])

# find
print(string_var.find('lo'))

# count
print(string_var.count('o'))

# upper
print(string_var.upper())

# lower
string_up = string_var.upper()
print("\n"+string_up)
lowstring = string_up.lower()
print(lowstring)

# strip
d_string = string_var
d_string += " space  "
print(d_string)
print(d_string.strip())

# split
print(string_var.split('l'))
print(string_var.split('e'))

# Multiline strings
b ="""this string
is longer than
usual\n"""
print(b)

# string: array of characters
print(b[15]+"\n")

# looping through a string
# looping through letters in a string
for x in string_var:
    print(x)

# check string
print("longer" in b)

# capitalize()
print(string_var.capitalize())

# centre
print(string_var.center(8))

# to encode a string
print(string_up.encode())

# endswith
print(string_var.endswith("zion"))

# expand tabs
txt = "M\ti\tn\ti\ts\tt\tr\ty"
print(txt.expandtabs(3))

# format: places/'formats' a specified value
# into a placeholder contained in the string
print("can this stick? {plugin}".format(plugin = "Sure"))

# index: returns the position of a specified value in a string
# usually the first occurence of said value
print(b.index('r'))

# isalnum() : returns True if all
# characters in a string are alphanumeric
print(lowstring.isalnum())

# isalpha returns True if all
# characters in a string are alphabets
print(lowstring.isalpha())

# these group of string 'manipulators' check
# for a condition in a string and return
# a Boolean value
print(lowstring.isascii())
print(lowstring.isdecimal())
print(lowstring.isdigit())
print(lowstring.isidentifier())
print(lowstring.islower())
print(lowstring.isnumeric())
print(lowstring.isprintable())
print(lowstring.isspace())
print(string_up.istitle())
print(lowstring.isupper())

# join
stringArray = (string_var, string_up, "world")
print(";".join(stringArray))

# rjust(): justifies a string to right alignment
r_align = (string_var.capitalize()).rjust(17)
print(r_align)

# ljust(): justifies a string to left alignment
print((string_var.capitalize()).ljust(4))

# lower, converts a string into lower case
print(string_up.lower())