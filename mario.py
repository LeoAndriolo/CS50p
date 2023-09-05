# Program to practice loop nesting

# Three blocks
# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# Using functions
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()