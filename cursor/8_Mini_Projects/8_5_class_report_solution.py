# Project 5 - Class Report (INTEGRATED CAPSTONE) (SOLUTION)

print("=== Class Report System ===")

class_list = [
    {"name": "Ali", "marks": 85, "city": "Lahore"},
    {"name": "Sara", "marks": 42, "city": "Karachi"},
    {"name": "Hassan", "marks": 76, "city": "Multan"},
    {"name": "Aisha", "marks": 91, "city": "Peshawar"},
]


def print_report(students):
    print("--- Student Report ---")
    for student in students:
        status = "Pass" if student["marks"] >= 50 else "Fail"
        print(
            f"{student['name']} | {student['city']} | "
            f"{student['marks']} | {status}"
        )


def count_passed(students):
    count = 0
    for student in students:
        if student["marks"] >= 50:
            count += 1
    return count


def average_marks(students):
    if len(students) == 0:
        return 0.0
    total = 0
    for student in students:
        total += student["marks"]
    return total / len(students)


print_report(class_list)

passed = count_passed(class_list)
average = average_marks(class_list)

print("--- Summary ---")
print(f"Total students: {len(class_list)}")
print(f"Passed: {passed}")
print(f"Failed: {len(class_list) - passed}")
print(f"Class average: {average:.1f}")

top_student = class_list[0]
for student in class_list:
    if student["marks"] > top_student["marks"]:
        top_student = student
print(f"Top student: {top_student['name']} ({top_student['marks']})")
