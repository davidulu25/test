import re

# python string manipulation

# basics

# concatenation
str1 = "Bel"
str2 = "lum"

print(str1 + str2)

# char selection
word = "Dominion"
char = word[2]
print(char)

# len , used to get size of string
print(len(word))

# replace()
print(word.replace("inion", "ain"))

# count
print(word.count('i'))

# * repeats an object a given number of times
print(str2 * 6)

# split(), for splitting
word_i = word.split('i')
print(word_i)
for x in word_i:
    print(x)

word_o = word.split('o')
print(word_o)
for x in word_o:
    print(x)