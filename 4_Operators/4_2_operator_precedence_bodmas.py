# 3_2_operator_precedence_bodmas.py

# ==================================================
# 🧠 Operators: Operator Precedence (BODMAS)
# ==================================================
# 🎯 Learning Objective: Understand brackets and order of operations
# 📚 Madrasa Context: Tasbeeh, ajza, and local-life calculations

print("🧠 Welcome to Operator Precedence (BODMAS)")
print("=" * 50)

print("\nBODMAS means:")
print("1) Brackets ( )")
print("2) Orders (powers) **")
print("3) Division /, //, %, and Multiplication * (left to right)")
print("4) Addition + and Subtraction - (left to right)")

# ----------------------------------
# 1. Without brackets
# ----------------------------------
print("\n1. Without Brackets:")
print("5 + 3 * 2 =", 5 + 3 * 2)
print("10 - 4 * 2 =", 10 - 4 * 2)
print("6 + 8 / 4 =", 6 + 8 / 4)

# ----------------------------------
# 2. With brackets
# ----------------------------------
print("\n2. With Brackets:")
print("(5 + 3) * 2 =", (5 + 3) * 2)
print("(10 - 4) * 2 =", (10 - 4) * 2)
print("(6 + 8) / 4 =", (6 + 8) / 4)

# ----------------------------------
# 3. Power before multiplication
# ----------------------------------
print("\n3. Power before Multiplication:")
print("2 * 3 ** 2 =", 2 * 3 ** 2)
print("5 + 2 ** 3 =", 5 + 2 ** 3)
print("(2 + 1) ** 3 =", (2 + 1) ** 3)

# ----------------------------------
# 4. Islamic/Madrasah examples
# ----------------------------------
print("\n4. Madrasa Examples:")
print("Tasbeeh: 33 times in 3 prayers =", (33 * 3) + (33 * 3) + (33 * 3))
print("30 ajza × 20 pages each – 10 missed pages =", (30 * 20) - 10)
print("12 students memorize 5 ayat each =", 12 * 5)

