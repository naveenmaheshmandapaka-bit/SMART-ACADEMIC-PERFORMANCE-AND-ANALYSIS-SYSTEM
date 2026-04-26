students = []

def add_student():
    student = {
        "id": len(students)+1,
        "name": input("Name: "),
        "marks": int(input("Marks: "))
    }
    students.append(student)

add_student()
print(students)
