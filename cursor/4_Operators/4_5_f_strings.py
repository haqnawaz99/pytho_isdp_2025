# Module 4 - Lesson 4.5
# Learning objective: f-strings with variables and expressions

name = "Ahmed"
print("Without f-string:", "My name is " + name)
print(f"My name is {name}")

age = 15
print(name + " is " + str(age) + " years old.")
print(f"{name} is {age} years old.")

student = "Hafiz Usman"
ajza = 18
print(f"{student} has memorized {ajza} ajza.")

marks = 85
print(f"{name} scored {marks} marks.")

price = 170
kg = 5
print(f"{kg} kg sugar costs {price * kg} rupees.")

city = "Multan"
print(f"I live in {city}.")

your_name = input("Enter your name: ")
your_class = input("Enter your class: ")
print(f"You are {your_name} and you study in class {your_class}.")

print(f"Next year {name} will be {age + 1} years old.")

# Practice:
# book_price = 300, count = 4 — print total with f-string and * inside {}

