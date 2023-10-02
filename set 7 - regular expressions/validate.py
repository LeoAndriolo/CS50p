# Set 7 Class - Regular Expressions

import re

email = input("What's your email? ").strip()

# Condition validation
    # if "@" in email and "." in email:
    #     print("Valid")
    # else:
    #     print("Invalid")

# Using str methods
    # username, domain = email.split("@")

    # if username and domain.endswith(".edu"):
    #     print("Valid")
    # else:
    #     print("Invalid")

# Regular expressions (re) library
if re.search("@",email):
    print("Valid")
else:
    print("Invalid")