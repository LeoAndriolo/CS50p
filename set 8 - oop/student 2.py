# Set 8 Class - Object-Oriented Programming

class Student:
    def __init__(self, name, house):   # Initializes content of a method (function inside a class)
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()