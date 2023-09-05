# Program to simulates a cat meowing

# Hardcoded
# print("meow")
# print("meow")
# print("meow")

# While Loop
    # Decreasing
# i = 3
# while i != 0:
#     print("meow")
#     i -= 1

    # Increasing
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# For Loop
# for _ in range(3): # "_" is used just because
#     print("meow")

# Print + Operators
# print("meow\n" * 3, end="")

# Input validation
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# Function Meow
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")