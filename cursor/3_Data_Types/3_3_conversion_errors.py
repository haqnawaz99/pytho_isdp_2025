# Module 3 - Lesson 3.3
# Learning objective: fix TypeError and ValueError

# --- Fix 1: TypeError (str + int) ---
age = 20
print("You are " + str(age) + " years old.")

# --- Fix 2: ValueError — only convert valid text ---
text = "123"
number = int(text)
print("Converted:", number)

# --- Fix 3: input without conversion ---
# num = input("Enter number: ")
# print(num + 5)  # TypeError — uncomment to demo

num = int(input("Enter a number: "))
print("Number + 10:", num + 10)

# --- Fix 4: cannot int("45.6") directly ---
value = int(float("45.6"))
print("From decimal string:", value)

# --- Fix 5: simple validation ---
user_text = input("Enter a whole number: ")
if user_text.isdigit():
    n = int(user_text)
    print("Correct:", n)
else:
    print("Please type digits only, like 12")

# Teacher demo: uncomment to show errors (then comment again)
# int("abc")
# int("")

# Practice:
# Write a program that asks for class strength; if isdigit(), convert and print strength + 1

