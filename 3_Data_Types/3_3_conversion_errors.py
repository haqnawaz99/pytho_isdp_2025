# conversion_errors_students_must_know.py

# ====================================================
# ⚠️ Common Type Conversion Errors (and Fixes)
# ====================================================

# 1. ❌ Converting a non-numeric string to int
# number = int("abc")  # ❌ ValueError
# ✅ Fix:
text = "123"
number = int(text)
print("Fixed Example 1:", number)

# 2. ❌ Mixing int and str without converting
# age = 20
# print("You are " + age + " years old.")  # ❌ TypeError
# ✅ Fix:
age = 20
print("Fixed Example 2:", "You are " + str(age) + " years old.")

# 3. ❌ Converting an empty string to int
# num = int("")  # ❌ ValueError
# ✅ Fix:
if "".isdigit():
    num = int("")
    print(num)
else:
    print("Fixed Example 3: Cannot convert empty string to integer.")

# 4. ❌ Trying to convert strings with spaces or characters
# x = int("12 years")  # ❌ ValueError
# ✅ Fix:
clean = "12"
x = int(clean)
print("Fixed Example 4:", x)

# 5. ❌ Trying to convert a float string directly to int
# x = int("45.6")  # ❌ ValueError
# ✅ Fix:
float_val = float("45.6")
int_val = int(float_val)
print("Fixed Example 5:", int_val)

# 6. ❌ Using float() on strings with invalid commas or characters
# val = float("1,000.50")  # ❌ ValueError
# ✅ Fix:
val_str = "1000.50"
val = float(val_str)
print("Fixed Example 6:", val)

# 7. ❌ Forgetting to convert input before math
# num = input("Enter a number: ")
# print(num + 5)  # ❌ TypeError
# ✅ Fix:
num = int(input("Enter a number: "))
print("Fixed Example 7:", num + 5)

# 8. ❌ Using bool conversion without understanding truthy/falsy
print("Fixed Example 8:")
print(bool(""))       # False
print(bool("hello"))  # True
print(bool("False"))  # True → because it's a non-empty string

# 9. ❌ Using str() on None without checking
val = None
val_str = str(val)
print("Fixed Example 9:", val_str)  # Output: 'None'

# 10. ❌ Forgetting nested conversion (e.g., float → int from input)
# x = int(input("Enter price (e.g., 12.5): "))  # ❌ ValueError
# ✅ Fix:
x = float(input("Enter price (e.g., 12.5): "))
print("Fixed Example 10:", int(x))
