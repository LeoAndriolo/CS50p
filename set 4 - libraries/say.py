# Set 4 Class - Libraries - Packages - Cowsay + Custom sayings lib

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("Hello, " + sys.argv[1])
#     # cowsay.trex("Hello, " + sys.argv[1])

import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])