lines = int(input())
students = {}

for _ in range(lines):
    info = input().split()
    name = info[0]
    grade = float(info[1])

    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for student, grades in students.items():
    average = sum(grades) / len(grades)
    formatted_grades = [f"{grade:.2f}" for grade in grades]
    print(f"{student} -> {' '.join(formatted_grades)} (avg: {average:.2f})")
