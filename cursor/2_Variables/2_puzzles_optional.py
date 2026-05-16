# Module 2 - OPTIONAL (adopted from claude variable puzzles)
# Predict output BEFORE you run each section.

print("=== Variable Logic Puzzles ===")
print()

# Puzzle 1: reassignment
print("--- Puzzle 1 ---")
city = "Lahore"
city = "Karachi"
city = "Islamabad"
print(city)

# Puzzle 2: swap with temp variable
print("--- Puzzle 2 ---")
first = "Fajr"
second = "Isha"
print("Before:", first, second)
temp = first
first = second
second = temp
print("After:", first, second)

# Puzzle 3: combine then reassign
print("--- Puzzle 3 ---")
a = "Assalamu"
b = "Alaikum"
greeting = a + " " + b
print(greeting)
a = "Welcome"
print(a, b, greeting)

# Puzzle 4: your turn
# Create x = 10, then x = x + 5. What is x? Write prediction first:
x = 10
x = x + 5
print("Puzzle 4 x =", x)
