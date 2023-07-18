# Vidmar P.
# Pyton version 3.10.6 64-bit
# Pytonshell:
#   pip install ....

import sys


class Program:

    # Variable
    i = 0

    # Constructor
    def __init__(self):
        self.i = 10
        pass

    # Function
    def foo(self):
        # DO SOMETHING
        return 30


# MAIN-Program -----------------------------------------------------------------------------------
var = Program()
print("Hello Python !")
print("Class i =", var.i)
print("Function =", var.foo())
