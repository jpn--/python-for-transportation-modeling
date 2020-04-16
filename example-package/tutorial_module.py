# This tutorial module does very little, other  
# than demonstrating some features of modules.

# Modules can import other modules.

import numpy as np

# Variables and functions can be defined at the 
# module level.

one_two = (1,2)

def hello():
	print("Hello Function!")

# Code that is defined at the module level
# is all executed once and only once when the
# module is first imported.  If you import the
# same module again, it is not run again. For
# example, this print statement will only appear
# on the first import of this modle.

print("Hello Florida!")
