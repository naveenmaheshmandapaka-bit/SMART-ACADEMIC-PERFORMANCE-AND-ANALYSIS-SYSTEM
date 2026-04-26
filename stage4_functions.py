students = []

def add_student():
    name = input("Name: ")
    marks = int(input("Marks: "))
    students.append([name, marks])

def view_students():
    for s in students:
        print(s)

add_student()
view_students()
