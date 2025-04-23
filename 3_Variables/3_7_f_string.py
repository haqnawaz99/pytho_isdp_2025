# f_string_comparison_examples.py

# =====================================================
# 🔁 Comparison: Without f-strings vs With f-strings
# =====================================================

# 1. Name Introduction
name = "Ahmed"

# Without f-string
print("My name is " + name)

# With f-string
print(f"My name is {name}")

print()

# 2. Name + Age
age = 15

# Without f-string
print(name + " is " + str(age) + " years old.")

# With f-string
print(f"{name} is {age} years old.")

print()

# 3. Islamic Example – Memorized Ajza
student = "Hafiz Usman"
ajza = 18

# Without f-string
print(student + " has memorized " + str(ajza) + " ajza of the Quran.")

# With f-string
print(f"{student} has memorized {ajza} ajza of the Quran.")

print()

# 4. Marks Summary
marks = 85

# Without f-string
print(name + " scored " + str(marks) + " marks in the test.")

# With f-string
print(f"{name} scored {marks} marks in the test.")

print()

# 5. Local Shop Bill
item = "Flour"
price = 135
kg = 5

# Without f-string
print(str(kg) + " kg of " + item + " costs " + str(price * kg) + " rupees.")

# With f-string
print(f"{kg} kg of {item} costs {price * kg} rupees.")

print()

# 6. Tasbeeh Tracker
tasbeeh = 33
prayers = 5
total_tasbeeh = tasbeeh * prayers

# Without f-string
print("You recited " + str(tasbeeh) + " tasbeeh in each prayer, total: " + str(total_tasbeeh) + ".")

# With f-string
print(f"You recited {tasbeeh} tasbeeh in each prayer, total: {total_tasbeeh}.")

print()

# 7. Age Next Year
student_name = "Fatima"
current_age = 13

# Without f-string
print(student_name + " will be " + str(current_age + 1) + " years old next year.")

# With f-string
print(f"{student_name} will be {current_age + 1} years old next year.")

print()

# 8. Using input (same output both ways)
your_name = input("Enter your name: ")
your_class = input("Which class are you in? ")

# Without f-string
print("You are " + your_name + " and you are in class " + your_class + ".")

# With f-string
print(f"You are {your_name} and you are in class {your_class}.")
