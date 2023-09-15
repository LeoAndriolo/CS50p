# Set 4 Class - Libraries - Packages - Cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    # cowsay.trex("Hello, " + sys.argv[1])