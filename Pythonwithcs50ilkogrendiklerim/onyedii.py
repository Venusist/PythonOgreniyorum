

"""
class Student:
    ...
#sadece ... koyman bile class oluşturmana izin verir


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
    # . allows you to get at something insidef of something else

if __name__ == "__main__":
    main()

"""
#

"""
class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

        #saklamanı sağlar self,


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main()

"""
#
"""
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)
if __name__ == "__main__":
    main()
"""

"""
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

def __str__(self):
    #sadece self alabilir
    return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)
if __name__ == "__main__":
    main()
    """

class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house= input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
    