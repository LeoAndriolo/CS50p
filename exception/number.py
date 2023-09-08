# Exceptions class notes

# x = int(input("What's x? "))
# print(f"x is {x}")

# cat returs ValueError: invalid literal for int() with base 10: 'cat'

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
