students = []

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        marks = int(input("Marks: "))
        students.append([name, marks])

    elif ch == 2:
        for s in students:
            print(s)

    elif ch == 3:
        break
