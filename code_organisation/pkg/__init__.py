__all__ = [
    "mod1",
    "mod2",
    "mod3",
    "mod4"
]

print(f'Invoking __init__.py for {__name__}')
A = ['quux, corge, grault']

# init.py file can also be used to automate importation of modules from a package
import pkg.mod1, pkg.mod2