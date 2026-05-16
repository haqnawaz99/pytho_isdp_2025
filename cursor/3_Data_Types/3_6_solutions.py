# Module 3 - Quiz solutions

# Q1
age = 15
print(type(age))

# Q2
price = 99.99
print(type(price))

# Q3
# TypeError: cannot concatenate str and int without str()

# Q4
result = int("40") + 10
print(result)

# Q5
students = 28
print("Students: " + str(students))

# Q6
n = int(input("Enter a whole number: "))
print(n * 2)

# Q7
a = int(input("First: "))
b = int(input("Second: "))
print(a + b)

# Q8
print(int(88.7))   # 88

# Q9
value = float(input("Enter decimal e.g. 12.5: "))
print(value)

# Q10
text = input("Enter whole number: ")
if text.isdigit():
    print("OK:", int(text))
else:
    print("Error: digits only")
