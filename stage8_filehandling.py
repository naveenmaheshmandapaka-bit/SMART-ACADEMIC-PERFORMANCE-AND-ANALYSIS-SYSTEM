import json

students = [{"name": "Ram", "marks": 80}]

with open("students.json", "w") as f:
    json.dump(students, f)

with open("students.json", "r") as f:
    data = json.load(f)
    print(data)
