# Python Classes Tutorial (https://github.com/Shahnazi2002)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Mohammad Shahnazi", 20)
print("Name:", p1.name)                              # Name: Mohammad Shahnazi
print("Age:", p1.age)                                # Age: 20


print("\n------------------------\n")


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(self.first_name, self.last_name)


p1 = Person("Mohammad", "Shahnazi", 20)
p2 = Person("Reza", "Hashemi", 32)
p1.full_name()                                       # Mohammad Shahnazi
p2.full_name()                                       # Reza Hashemi


print("\n------------------------\n")


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(self.first_name, self.last_name)


class Student(Person):
    pass


# June 2022