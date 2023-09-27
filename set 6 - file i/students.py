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
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    # for row in reader:
    #     students.append({"name": row[0], "home": row[1]}) -> Row syntax
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

