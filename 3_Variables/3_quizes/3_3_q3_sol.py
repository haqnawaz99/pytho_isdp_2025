# task2_solution.py

# ==================================================
# ✅ Task 2: Total Marks Calculator (Solution)
# ==================================================

# Step 1: Ask for marks of 3 subjects
mark1 = input("Enter marks of subject 1: ")
mark2 = input("Enter marks of subject 2: ")
mark3 = input("Enter marks of subject 3: ")

# Step 2: Convert to integers
mark1 = int(mark1)
mark2 = int(mark2)
mark3 = int(mark3)

# Step 3: Add the marks
total = mark1 + mark2 + mark3

# Step 4: Print using +
print("Total marks are: " + str(total))

# Step 5: Print using f-string
print(f"Total marks are: {total}")
