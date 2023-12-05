# importing modules FROM packages
import pkg.mod1, pkg.mod2

pkg.mod1.foo

# from module_name import name(s)
from pkg.mod1 import foo
foo()

# from module_name import <name> as alt_name
from pkg.mod2 import Bar as Qux
x = Qux()
print(x)

# you can import modules from a package with this statement: 'from package_name import module_name_1, module_name_2, module_name_n'

#implementation
from pkg import mod1
foo()


# package initialisation
# __init__ when working with packages
# when a file named __init__.py is a package directory, it is invoked when a package (or a module in the package) is imported

import pkg # this usually does not not do anything unless there's some file with a global variable in the package directory
pkg.A

# init.py file can also be used to automate importation of modules from a package. in this file when pkg is imported, mod1 and mod2 are automatically imported
import pkg
pkg.mod1.foo()
pkg.mod2.bar()

# importing * from a package
# creating more modules to add to this package
# a list named __all__ is added to the init file to update the interpreter with all modules that should be imported when importing

from pkg import *
mod3.grapes()
print(mod4.Pear)
print(dir())

# all list can also be defined in a module
# when importing * from pkg.mod1 only foo() will be imported
from pkg.mod1 import *
print(dir())

foo()

# Subpackages
import pkg.sub_pkg.mod5

pkg.sub_pkg.mod5.plum()

# absolute imports
# relative imports