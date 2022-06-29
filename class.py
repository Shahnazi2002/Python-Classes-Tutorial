# Python Classes Tutorial (https://github.com/Shahnazi2002)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



p1 = Person("Mohammad", 20)
print("Name:", p1.name)                                                                                 # Name: Mohammad
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
p1.full_name()                                                                                          # Mohammad Shahnazi                                                                                         # Reza Barghi


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


class MyClass:
    pass


class Car:
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def __str__(self):
        return f"\n{self.__class__.__name__}:\nColor: {self.color}\nBuild Year: {self.year}"


class Taxi(Car):
    pass


class Bus(Car):
    pass



obj = MyClass()
print(obj.__class__.__name__)                                                                           # MyClass

car1 = Car("Black", 2021)
print(car1)                                                                                             # Car:
                                                                                                        # Color: Black
                                                                                                        # Build Year: 2021
car2 = Taxi("Yellow", 2015)
print(car2)                                                                                             # Taxi:
                                                                                                        # Color: Yellow
                                                                                                        # Build Year: 2015
car3 = Bus("Red", 2018)
print(car3)                                                                                             # Bus:
                                                                                                        # Color: Red
                                                                                                        # Build Year: 2018


print("\n------------------------\n")


class Person:
    def __init__(self, first_name, last_name, birthyear):
        self.name = f"{first_name} {last_name}"
        self.age = 2022 - birthyear

    def info(self):
        print(f"\nName: {self.name}\nAge: {self.age}")


class Student(Person):
    def __init__(self, first_name, last_name, birthyear, university):
        super().__init__(first_name, last_name, birthyear)
        self.university = university

    def info(self):
        print(f"\nName: {self.name}\nAge: {self.age}\nUniversity: {self.university}")


class Driver(Person):
    def __init__(self, first_name, last_name, birthyear, licence_class):
        super().__init__(first_name, last_name, birthyear)
        self.licence_class = licence_class

    def info(self):
        print(f"\nName: {self.name}\nAge: {self.age}\nLicence: Class {self.licence_class}")



p1 = Person("Reza", "Barghi", 2004)
p1.info()                                                                                               # Name: Reza Barghi
                                                                                                        # Age: 18
p2 = Student("Mohammad", "Shahnazi", 2002, "Azarbaijan Shahid Madani University")
p2.info()                                                                                               # Name: Mohammad Shahnazi
                                                                                                        # Age: 20
                                                                                                        # University: Azarbaijan Shahid Madani University
p3 = Driver("Amin", "Shahnazi", 1985, "A")
p3.info()                                                                                               # Name: Amin Shahnazi
                                                                                                        # Age: 37
                                                                                                        # Licence: Class A


print("\n------------------------\n")
