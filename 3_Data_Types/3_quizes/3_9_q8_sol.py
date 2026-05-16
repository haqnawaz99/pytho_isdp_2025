# 3_1_q8_sol.py

# =======================================================
# ✅ Task 8: Basic Report Card (Solution)
# =======================================================

name = input("Enter your name: ")
class_name = input("Enter your class: ")
m1 = int(input("Marks of subject 1: "))
m2 = int(input("Marks of subject 2: "))
m3 = int(input("Marks of subject 3: "))

total = m1 + m2 + m3
average = total / 3

print(f"{name} from class {class_name} scored {total} marks.")
print(f"Average marks: {average}")