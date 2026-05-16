# Module 6 - Quiz solutions

# Q1
def say_hello():
    print("Hello")

say_hello()

# Q2
def list_three_subjects():
    print("Math")
    print("Urdu")
    print("Science")

list_three_subjects()

# Q3
def greet(name):
    print(f"Welcome {name}")

greet("Hassan")

# Q4
def show_total(price, qty):
    print(price * qty)

show_total(120, 3)

# Q5
def get_slogan():
    return "Pakistan Zindabad"

print(get_slogan())

# Q6
def add(a, b):
    return a + b

print(add(20, 30))

# Q7
def is_adult(age):
    return age >= 18

print(is_adult(16))
print(is_adult(20))

# Q8
def discount_price(price, percent=10):
    return price - price * percent / 100

print(discount_price(1000))
print(discount_price(1000, 20))

# Q9
def full_name(first, last):
    return first + " " + last

print(full_name("Hafiz", "Ali"))

# Q10
def check_pass(marks):
    if marks >= 50:
        return "Pass"
    return "Fail"

print(check_pass(55))
print(check_pass(40))
