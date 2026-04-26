students = [["ram", 80], ["ravi", 70]]

name = input("Search Name: ").lower()

for s in students:
    if s[0].lower() == name:
        print("Found:", s)
