# Set 6 Class - File I/O - Names

# Class Intro
# names = []

# for _ in range(3):
    #     names.append(input("What's your name? "))

    # for name in sorted(names):
    #     print(f"hello, {name}")

# I/O Intro
    # name = input("What's your name? ")

    # file = open("names.txt", "a") # w - write / a - append
    # file.write(f"{name}\n")
    # file.close()

# Using With
    # Writing on file
        # name = input("What's your name? ")

        # with open("names.txt", "a") as file:
        #     file.write(f"{name}\n")

    # Readind from file
        # First method
            # with open("names.txt", "r") as file: # r - read
            #     lines = file.readlines()

            # for line in lines:
            #     print("hello,",line) # Could use [, end=""] or [.rstrip()]

        # Second method
            # with open("names.txt", "r") as file: # r - read
            #     for line in file:
            #         print("hello,",line.rstrip())

# Using Sorted
names = []

with open("names.txt") as file: # r - read
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")