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

# Row by Row - Sorted
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in sorted(students):
    print(f"{student['name']} is in {student['house']}")

