class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 500000
        self.designation = "SDE"

# create an obj/instance of the class

sam = employee()

print(sam.id)
print(sam.salary)