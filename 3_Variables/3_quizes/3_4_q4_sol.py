# 3_1_q4_sol.py

# =======================================================
# ✅ Task 4: Sweets Division (Solution)
# =======================================================

total_sweets = int(input("Enter total number of sweets: "))
students = int(input("Enter number of students: "))

# Floor division and modulus
each_student = total_sweets // students
leftover = total_sweets % students

# Using +
print("Each student gets " + str(each_student) + " sweets.")
print("Leftover sweets: " + str(leftover))

# Using f-string
print(f"Each student gets {each_student} sweets.")
print(f"Leftover sweets: {leftover}")