class Student:
    def __init__(self, fullname, age):
        self.name = fullname
        self.age = age

s1 = Student("Alice", 20)
print(s1.age)
print(s1.name)