# Set 6 Class - File I/O - Students

# Row by Row - List
    # with open("students.csv") as file:
    #     for line in file:
    #         row = line.rstrip().split(",")
    #         print(f"{row[0]} is in {row[1]}")

# Row by Row - Dict
    # with open("students.csv") as file:
    #     for line in file:
    #         name, house = line.rstrip().split(",")
    #         print(f"{name} is in {house}")

# Row by Row - Sorted
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

