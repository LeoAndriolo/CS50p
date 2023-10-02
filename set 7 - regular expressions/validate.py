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
if re.search(r"^\w+@\w+\.edu$",email, re.IGNORECASE): # [a-zA-Z0-9_] alpha + numeric + _ | \w -> Any word character like [a-zA-Z0-9_]
    print("Valid")
else:
    print("Invalid")