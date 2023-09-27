# Set 6 Class - File I/O - Students

# Row by Row - List
    # with open("students.csv") as file:
    #     for line in file:
    #         row = line.rstrip().split(",")
    #         print(f"{row[0]} is in {row[1]}")

# Row by Row - Associated list
    # with open("students.csv") as file:
    #     for line in file:
    #         name, house = line.rstrip().split(",")
    #         print(f"{name} is in {house}")

# Row by Row - Sorted Dict - Lambda
    # students = []

    # with open("students.csv") as file:
    #     for line in file:
    #         name, house = line.rstrip().split(",")
    #         student = {"name": name, "house": house}
    #         students.append(student)

    # # def get_name(student):
    # #     return student["name"]

    # for student in sorted(students, key=lambda student: student["name"]):
    #     print(f"{student['name']} is in {student['house']}")

# csv Function
    # Reading
        # import csv

        # students = []

        # with open("students.csv") as file:
        #     reader = csv.DictReader(file)
        #     for row in reader:
        #         students.append({"name": row["name"], "home": row["home"]})

        # for student in sorted(students, key=lambda student: student["name"]):
        #     print(f"{student['name']} is from {student['home']}")

# Writting
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})