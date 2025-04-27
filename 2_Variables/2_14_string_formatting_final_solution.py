# 2_13_string_formatting_final_solution.py

# ==================================================
# ✅ Final Paper: String Formatting in Python (Solution)
# ==================================================

# ----------------------------------
# 🔹 Section 1: title(), upper(), lower()
# ----------------------------------

# Q1
full_name = "muhammad abdullah"
print(full_name.title())

# Q2
madrasah_name = "jamia ashrafia"
print(madrasah_name.upper())

# Q3
city_name = "LaHorE"
print(city_name.lower())

# ----------------------------------
# 🔹 Section 2: Whitespace (Tabs and Newlines)
# ----------------------------------

# Q4
student1 = "Ahmad"
student2 = "Bilal"
print(student1 + "\t" + student2)

# Q5
print("Welcome to Jamia Ashrafia\nClass: Darja Oola")

# Q6
print("\nSubjects Offered:")
print("\tFiqh")
print("\tHadith")
print("\tTafsir")

# ----------------------------------
# 🔹 Section 3: Stripping Whitespace
# ----------------------------------

# Q7
teacher_name = "  Ustad Abdul Wahid  "
print(teacher_name.strip())

# Q8
book_title = "  Tafsir Ibn Kathir"
print(book_title.lstrip())

# Q9
city_with_space = "Lahore   "
print(city_with_space.rstrip())
