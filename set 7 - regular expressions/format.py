# Set 7 Class - Regular Expressions

# First interaction
    # name = input("What's your name? ").strip()

    # if "," in name:
    #     first, last = name.split(", ")
    #     name = f"{first} {last}"

    # print(f"hello, {name}")
    
# re lib
import re

# Groups
    # name = input("What's your name? ").strip()
    # matches = re.search(r"^(.+), *(.+)$", name)
    # if matches:
    #     last, first = matches.groups()
    #     name = f"{first} {last}"
    # print(f"hello, {name}")

# Separated group
    # name = input("What's your name? ").strip()
    # matches = re.search(r"^(.+), *(.+)$", name)
    # if matches:
    #     name = matches.group(2) + " " + matches.group(1)
    # print(f"hello, {name}")

# Walrus syntax
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")