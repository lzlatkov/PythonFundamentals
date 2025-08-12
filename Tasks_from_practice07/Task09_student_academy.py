students_dictionary = {}
students_count = int(input())

for student in range(students_count):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_dictionary:
        students_dictionary[student_name] = []

    students_dictionary[student_name].append(student_grade)

for student, grade in students_dictionary.items():
    if sum(grade) / len(grade) >= 4.50:
        print(f"{student} -> {sum(grade) / len(grade):.2f}")
