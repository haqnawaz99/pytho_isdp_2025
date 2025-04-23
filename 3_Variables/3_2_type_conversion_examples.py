# all_type_conversions.py

# ====================================================
# 🔄 Python Type Conversions: Step-by-Step Examples
# ====================================================

# 1. Convert string to integer
num_str = "25"
num_int = int(num_str)
print("1. String to Int:", num_int + 5)

# 2. Convert string to float
price_str = "12.75"
price_float = float(price_str)
print("2. String to Float:", price_float + 2.25)

# 3. Convert integer to string
students = 30
students_str = str(students)
print("3. Int to String:", "Total students: " + students_str)

# 4. Convert float to integer (decimal part is removed)
marks = 89.9
rounded_marks = int(marks)
print("4. Float to Int:", rounded_marks)

# 5. Convert string to boolean (non-empty = True, empty = False)
msg1 = "hello"
msg2 = ""
print("5. String to Bool:", bool(msg1), bool(msg2))  # Output: True False

# 6. Convert integer to float
age = 18
age_float = float(age)
print("6. Int to Float:", age_float)

# 7. Convert float to string
temperature = 36.6
temp_str = str(temperature)
print("7. Float to String:", "Temp is " + temp_str)

# 8. Convert input string to integer safely
user_input = input("8. Enter a number: ")
num = int(user_input)
print("You entered:", num, "and its square is:", num * num)

# 9. Convert string representing float to int (multi-step)
height_str = "172.5"
height_float = float(height_str)
height_int = int(height_float)
print("9. String (float) to Int:", height_int)

# 10. Combine string conversion and math
num1 = int(input("10. Enter first number: "))
num2 = int(input("Enter second number: "))
print("Their sum is:", num1 + num2)
