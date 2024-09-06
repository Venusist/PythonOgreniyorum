"""
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""
#
"""
students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

"""
#
"""
students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
"""
#

students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    #anonymous function lambda
    print(f"{student['name']} is in {student['house']}")