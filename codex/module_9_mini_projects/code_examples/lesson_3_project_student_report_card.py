def grade_message(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

print(f"{name}: {grade_message(marks)}")
