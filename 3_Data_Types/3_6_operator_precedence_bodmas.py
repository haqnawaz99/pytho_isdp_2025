# operator_precedence_bodmas.py

# ==============================================
# 🧠 Python Math Operator Precedence (BODMAS)
# ==============================================

# 🔹 BODMAS means: Brackets, Orders (Powers), Division, Multiplication, Addition, Subtraction

# ----------------------------
# 1. Expressions without brackets
# ----------------------------
print("1. Without Brackets:")
print(5 + 3 * 2)
print(10 - 4 * 2)
print(6 + 8 / 4)

# ----------------------------
# 2. Expressions with brackets
# ----------------------------
print("\n2. With Brackets:")
print((5 + 3) * 2)
print((10 - 4) * 2)
print((6 + 8) / 4)

# ----------------------------
# 3. Power (exponent) before multiply
# ----------------------------
print("\n3. Power before Multiplication:")
print(2 * 3 ** 2)
print(5 + 2 ** 3)
print((2 + 1) ** 3)

# ----------------------------
# 4. Division and Multiplication (same level → left to right)
# ----------------------------
print("\n4. Division & Multiplication:")
print(12 / 3 * 2)
print(20 / 4 * 5)
print(16 * 2 / 4)

# ----------------------------
# 5. Combination of all (BODMAS in full)
# ----------------------------
print("\n5. Full BODMAS Examples:")
print((4 + 2) * 3 ** 2 - 8 / 4)
print((5 + 3) * (6 - 2) + 2 ** 2)
print(10 + 6 / 2 * 3 - 1)

# ----------------------------
# 6. Islamic/Madrasah Examples
# ----------------------------
print("\n6. Islamic Examples:")
# 1 tasbeeh 33 times in 3 prayers
print((33 * 3) + (33 * 3) + (33 * 3))  

# 30 ajza × 20 pages each – 10 missed pages
print((30 * 20) - 10)  

# 12 students memorize 5 ayat each
print(12 * 5)  

# ----------------------------
# 7. Local Life Examples
# ----------------------------
print("\n7. Pakistani Life Examples:")
# If one book costs 250 and you buy 4
print(250 * 4)

# Electricity bill: 1800 - (fixed discount 300)
print(1800 - 300)

# You divide 1500 rupees equally among 5 friends
print(1500 / 5)

# ----------------------------
# 8. Tasbeeh-style: With & Without Brackets
# ----------------------------
print("\n8. Tasbeeh-style Brackets Impact:")
print(10 + 5 * 3)
print((10 + 5) * 3)
