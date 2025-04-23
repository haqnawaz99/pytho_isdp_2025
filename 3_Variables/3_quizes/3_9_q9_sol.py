# 3_1_q9_sol.py

# =======================================================
# ✅ Task 9: Compare Marks (Solution)
# =======================================================

a = int(input("Enter marks of Student A: "))
b = int(input("Enter marks of Student B: "))

if a > b:
    print("Student A scored more.")
elif b > a:
    print("Student B scored more.")
else:
    print("Both scored the same.")