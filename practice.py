class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
    
s1 = student("Bob", [99, 98, 97]) 
print(s1.average())