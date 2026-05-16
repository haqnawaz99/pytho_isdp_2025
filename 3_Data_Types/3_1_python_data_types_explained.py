# python_data_types_explained.py

# ======================================
# 📘 Python Basic Data Types Explained
# ======================================

# 1. 🔢 Integer (int)
# Integers are whole numbers without a decimal point
print("1. Integer Example:")
age = 17
print("Age:", age)
print("Data type of age is:", type(age))  # Output: <class 'int'>

print()  # Empty line for readability

# 2. 💸 Float (float)
# Floats are numbers that contain a decimal point
print("2. Float Example:")
price = 12.99
print("Price:", price)
print("Data type of price is:", type(price))  # Output: <class 'float'>

print()

# 3. 📝 String (str)
# Strings are a series of characters (letters, numbers, symbols) enclosed in quotes
print("3. String Example:")
name = "Ahmed"
print("Name:", name)
print("Data type of name is:", type(name))  # Output: <class 'str'>

print()

# 4. ✅ Boolean (bool)
# Boolean can be only True or False (note the capital letters)
print("4. Boolean Example:")
is_student = True
print("Is student:", is_student)
print("Data type of is_student is:", type(is_student))  # Output: <class 'bool'>

print()

# 5. 📋 List (list)
# Lists can store multiple values in one variable using square brackets
print("5. List Example:")
subjects = ["Quran", "Hadith", "Fiqh"]
print("Subjects:", subjects)
print("Data type of subjects is:", type(subjects))  # Output: <class 'list'>

print()

# 6. 📦 NoneType
# None represents the absence of a value (used to declare empty variables)
print("6. NoneType Example:")
future_data = None
print("Future data:", future_data)
print("Data type of future_data is:", type(future_data))  # Output: <class 'NoneType'>

print()

# Bonus: Using underscores for readability in large numbers (still treated as numbers)
print("7. Bonus: Readable Numbers")
population = 220_000_000  # Same as 220000000
print("Population of Pakistan:", population)
print("Data type of population is:", type(population))  # Output: <class 'int'>

# ============================================
# 8. ❌ Mixing int with str: Causes an Error
# ============================================

# This will cause an error because Python cannot directly add a string and a number
# Uncomment the following line to see the error

# print("Your age is: " + 17)  # ❌ TypeError

# ✅ Correct way: Convert int to string using str()
print("8. Type Conversion Example:")
age = 17
print("Your age is: " + str(age))  # ✅ Now it works!

# Another way (using comma, which auto-handles types)
print("Your age is:", age)  # ✅ Also works without conversion
