# 3_1_q8_sol.py

# =======================================================
# ✅ Task 8: Basic Report Card (Solution)
# =======================================================

# Step 1: Ask user for name and class
name = input("Enter your name: ")
class_name = input("Enter your class: ")

# Step 2: Ask for marks of 3 subjects
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

# Step 3: Calculate total and average
total = mark1 + mark2 + mark3
average = total / 3

# Step 4: Print details using f-string
print(f"\n{name} from class {class_name} has the following result:")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
