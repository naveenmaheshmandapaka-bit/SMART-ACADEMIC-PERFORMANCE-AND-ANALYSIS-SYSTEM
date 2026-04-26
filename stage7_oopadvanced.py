class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

s = Student("Ram", 80)
s.display()
