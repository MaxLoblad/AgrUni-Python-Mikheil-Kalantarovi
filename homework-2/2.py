subjects = {
    'math': {'George': 85, 'Salome': 78, 'David': 92},
    'physics': {'George': 90, 'David': 75, 'Salome': 88},
    'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

students = {}

for subject, grades in subjects.items():
    for student, score in grades.items():
        if student not in students:
            students[student] = {}
        students[student][subject] = score

print(students)
