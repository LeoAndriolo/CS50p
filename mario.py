# Program to practice loop nesting

# Three blocks
# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# Using functions
def main():
    # print_column(3)
    # print_row(4)
    print_square(3)

# def print_column(height):
#     # 1 Method
#     # for _ in range(height):
#     #     print("#")

#     # 2 Method
#     print("#\n" * height, end="")

# def print_row(width):
#     print("?" * width)

def print_square(size):
    # for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            # print brick
            print("#", end="")

        # 
        print()

main()