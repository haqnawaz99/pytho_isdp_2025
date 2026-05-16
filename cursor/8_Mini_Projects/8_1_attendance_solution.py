# Project 1 - Class Attendance Counter (SOLUTION)

print("=== Class Attendance Counter ===")

total = int(input("Total students in class: "))
absent = int(input("How many absent today? "))

present = total - absent

print(f"Class strength: {total}")
print(f"Absent: {absent}")
print(f"Present today: {present}")

if absent == 0:
    print("Full attendance! MashaAllah.")
else:
    print("Some students are absent. Please follow up.")

if present < total * 0.5:
    print("Warning: less than half class present.")
