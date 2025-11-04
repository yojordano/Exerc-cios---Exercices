students_input = input("Students: ")

students = students_input.split()

students.sort()

print("Class Roll")
for student in students:
    print(student)
