# Python Classes Tutorial (https://github.com/Shahnazi2002)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



p1 = Person("Mohammad Shahnazi", 20)
print("Name:", p1.name)                                                                                 # Name: Mohammad Shahnazi
print("Age:", p1.age)                                                                                   # Age: 20


print("\n------------------------\n")


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(self.first_name, self.last_name)



p1 = Person("Mohammad", "Shahnazi", 20)
p2 = Person("Reza", "Barghi", 32)
p1.full_name()                                                                                          # Mohammad Shahnazi
p2.full_name()                                                                                          # Reza Barghi


print("\n------------------------\n")


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print(self.first_name, self.last_name)

    def info(self):
        print("I am", self.first_name, self.last_name)


class Student(Person):
    def info(self):
        print("I am a student. My name is", self.first_name, self.last_name)


class Teacher(Person):
    def info(self):
        print("I am a teacher. My name is", self.first_name, self.last_name)



student1 = Student("Mohammad", "Shahnazi")
teacher1 = Teacher("Alireza", "Ghaffari")
student1.full_name()                                                                                    # Mohammad Shahnazi
student1.info()                                                                                         # I am a student. My name is Mohammad Shahnazi
teacher1.full_name()                                                                                    # Alireza Ghaffari
teacher1.info()                                                                                         # I am a teacher. My name is Alireza Ghaffari


print("\n------------------------\n")


class Member:
    def __init__(self, id, first_name, last_name, birthyear):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birthyear = birthyear

    def __str__(self):
        return f"ID: {self.id}\nName: {self.first_name} {self.last_name}\nAge: {2022-self.birthyear}"


m1 = Member(1001, "Mohammad", "Shahnazi", 2002)
print(m1)                                                                                               # ID: 1001
                                                                                                        # Name: Mohammad Shahnazi
                                                                                                        # Age: 20


print("\n------------------------\n")
