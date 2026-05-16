# Module 6 - Lesson 6.3
# Learning objective: return values

def get_greeting():
    return "Assalamu Alaikum"

message = get_greeting()
print(message)
print(get_greeting())

def greet_name(name):
    return f"Assalamu Alaikum {name}"

print(greet_name("Usman"))

def add_numbers(a, b):
    return a + b

print(add_numbers(15, 25))

def multiply(price, qty):
    return price * qty

bill = multiply(170, 5)
print(f"Bill: {bill} rupees")

def is_pass(marks):
    return marks >= 50

print(is_pass(75))
print(is_pass(42))

def square(n):
    return n * n

print(square(9))

# Use return in an if
def grade_letter(marks):
    if marks >= 80:
        return "B or better"
    return "Keep studying"

print(grade_letter(85))
print(grade_letter(60))

# Practice:
# Function double_number(x) that returns x * 2
# Print result of double_number(7)

