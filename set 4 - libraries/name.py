# Set 4 Class - Libraries - Sys library

import sys # sys.argv[0] -> Program name

# sys.argv # Argument value
if len(sys.argv) < 2:
    sys.exit("Too few arguments")    
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")    

print("Hello, my name is", sys.argv[1])
    
    