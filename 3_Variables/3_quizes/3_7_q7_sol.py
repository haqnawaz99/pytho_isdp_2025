# 3_1_q7_sol.py

# =======================================================
# ✅ Task 7: Quran Ajza Percentage (Solution)
# =======================================================

ajza = int(input("Enter number of ajza memorized: "))
percentage = (ajza / 30) * 100

# Using +
print("You have memorized " + str(percentage) + "% of the Quran.")

# Using f-string
print(f"You have memorized {percentage}% of the Quran.")