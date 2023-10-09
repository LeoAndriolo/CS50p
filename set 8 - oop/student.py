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

class Student:
    def __init__(self, name, house):   # Initializes content of a method (function inside a class)
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
        

def main():
    student = get_student()
    print(student)
    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)   # Constructor call

if __name__ == "__main__":
    main()