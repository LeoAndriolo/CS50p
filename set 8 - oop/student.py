# Set 8 Class - Object-Oriented Programming

def main():
    student = get_student()   # Assign Tuple that contains 2 elements per index
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)   # Tuple

if __name__ == "__main__":
    main()