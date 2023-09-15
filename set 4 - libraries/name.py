# Set 4 Class - Libraries - Sys library

import sys

# sys.argv # Argument value
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")