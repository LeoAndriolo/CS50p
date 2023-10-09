# Set 8 Class - Object-Oriented Programming

# Intro logic
    # def main():
    #     student = get_student()   # Assign Tuple that contains 2 elements per index
    #     if student[0] == "Padma":
    #         student[1] = "Ravenclaw"
    #     print(f"{student[0]} from {student[1]}")
        

    # def get_student():
    #     name = input("Name: ")
    #     house = input("House: ")
    #     # return (name, house)   # Tuple does NOT support item assigment
    #     return [name, house]   # Lists support item assigment

    # if __name__ == "__main__":
    #     main()

# OOP
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")
    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name,"house": house}   # Dicts support item assigment

if __name__ == "__main__":
    main()