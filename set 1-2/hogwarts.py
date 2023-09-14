# Code to practice lists/len/dict

# Simple For loop
# students = ["Herminone", "Harry", "Ron"]

# for student in students:
#     print(student)

# Using len() -> Lenght
# students = ["Herminone", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# Using dict() -> Dictionary
# students = ["Herminone", "Harry", "Ron","Draco"]
# houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]

# students = {
#     "Hermione":"Gryffindor",
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco":"Slytherin"
#     }

# print(students["Hermione"])
# for student in students:
#     print(student, students[student], sep=" ")

# More complex dictionary
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronous": "Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=" ")