# Set 4 Class - Libraries - Sys library

import sys

# sys.argv # Argument value
if len(sys.argv) < 2:
    print("Too few arguments")    
elif len(sys.argv) > 2:
    print("Too many arguments")    
else:
    print("Hello, my name is", sys.argv[1])
    