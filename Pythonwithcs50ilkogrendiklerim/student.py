
"""
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name=input("Name: ")
    house = input("House: ")
    return [name, house]
#() koysaydık olmazdı eror verirdi gruplandırma için []kullandık list yapar gibi


if __name__ == "__main__":
    main()
"""
#
"""
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()
"""
#

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name=input("Name: ")
    house= input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()

