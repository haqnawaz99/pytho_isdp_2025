# variable_naming_errors_and_tips.py

# ❌ Error 1: Spaces in variable name
# full name = "Ahmed"
# ✅ Fix:
full_name = "Ahmed"

# ❌ Error 2: Starting with a number
# 1student = "Ali"
# ✅ Fix:
student1 = "Ali"

# ❌ Error 3: Using hyphen or special character
# student-name = "Ayesha"
# ✅ Fix:
student_name = "Ayesha"

# ❌ Error 4: Using Python keyword
# class = "Grade 5"
# ✅ Fix:
student_class = "Grade 5"

# ❌ Error 5: Using capital letters randomly (not error, but not recommended)
StudentName = "Usman"
# ✅ Better:
student_name = "Usman"

# ❌ Error 6: Using symbols like $, %, !
# total$marks = 500
# ✅ Fix:
total_marks = 500

# ❌ Error 7: Very short and unclear name
# x = "Quran"
# ✅ Fix:
subject_name = "Quran"

# ❌ Error 8: Case sensitivity confusion
RollNumber = 23
rollnumber = 45
# ✅ Tip: Stick to one naming style

# ❌ Error 9: Typing long variable names with no underscores
# studentnamefrommadrasahlahore = "Ahmed"
# ✅ Fix:
student_name_from_madrasah_lahore = "Ahmed"

# ❌ Error 10: Using variable before defining
# print(age)
# ✅ Fix:
age = 14
print(age)
