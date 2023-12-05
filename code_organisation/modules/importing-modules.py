import modules
print(modules.s)

print(modules.a)

# importing from modules
from modules import a

print(a)

# importing everythimg from a module
from modules import *

print(s.upper())

# importing module with new name
import modules as jamaica

print(jamaica.a)

# importing from modules as alternative name
from modules import s as string, a as alist

s = 'reboot'

print(s)
print(string)