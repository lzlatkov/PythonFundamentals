students = []
searched_course = ""

while True:
    student = input()
    if ":" not in student:
        searched_course = student
        break
    name, id_, course = student.split(":")
    students.append({'name': name, 'ID': id_, 'course': course})

for student in students:
    if searched_course.startswith(student['course'][0:5]):
        print(f"{student['name']} - {student['ID']}")

###########################################################################

students_dict = {}
command = input()

while ":" in command:
    info = command.split(":")
    name, id, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    command = input()
course = " ".join(command.split("_"))

for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')


