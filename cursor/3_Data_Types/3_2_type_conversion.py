# Module 3 - Lesson 3.2
# Learning objective: int(), float(), str() and input conversion

# String to int
num_str = "25"
num_int = int(num_str)
print("String to int + 5:", num_int + 5)

# String to float
price_str = "99.50"
price = float(price_str)
print("Price + 0.50:", price + 0.50)

# Int to string
books = 40
print("Books in Maktaba: " + str(books))

# Float to int (truncates decimal)
average = 87.9
print("Marks as int:", int(average))

# input to int
user_age = input("Enter your age (whole number): ")
age = int(user_age)
print("Next year you will be", age + 1)

# Two numbers sum
first = int(input("First number: "))
second = int(input("Second number: "))
print("Sum:", first + second)

# Decimal string: float then int
height_str = "172.5"
height_cm = int(float(height_str))
print("Height in cm (whole):", height_cm)

# Rupees with float
rupees_input = input("Enter amount in rupees (can be decimal): ")
amount = float(rupees_input)
print("Amount:", amount)

# Practice:
# Ask how many copies of a book; convert to int; print total if each costs 50 (use int only for copies)

