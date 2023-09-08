# Exceptions class notes

# P01
# x = int(input("What's x? "))
# print(f"x is {x}")

# cat returs ValueError: invalid literal for int() with base 10: 'cat'

# P02
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}") # Returns NameError for "cat" -> NameError: name 'x' is not defined
#                    # Caused by int() not assigning a value to x

# P03
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")
    
# P04
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
        
# print(f"x is {x}")

# P05

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            # print("x is not an integer")
            pass # Catches error, but doesn't print it

main()
