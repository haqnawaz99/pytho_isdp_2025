# 2_12_teaching_stripping_whitespace.py

# ==================================================
# 📘 Teaching: Stripping Whitespace in Python
# ==================================================

# Sometimes when users type, there are extra spaces at the beginning or end of text.
# Python gives us simple functions to clean those spaces.

# ----------------------------------
# 🔹 1. strip() → Removes spaces from both sides
# ----------------------------------

student_name = "  Muhammad Musa  "
print(student_name.strip())

# ----------------------------------
# 🔹 2. lstrip() → Removes spaces from the left side only
# ----------------------------------

teacher_name = "  Ustad Abdul Wahid"
print(teacher_name.lstrip())

# ----------------------------------
# 🔹 3. rstrip() → Removes spaces from the right side only
# ----------------------------------

institution_name = "Jamia Ashrafia   "
print(institution_name.rstrip())

# ----------------------------------
# 🔹 More Real-Life Examples
# ----------------------------------

# Example 1: Cleaning a city name input
city = "  Lahore  "
print(city.strip())

# Example 2: Cleaning subject name
subject = "  Fiqh"
print(subject.lstrip())

# Example 3: Cleaning Islamic book title
book_title = "Sahih Bukhari   "
print(book_title.rstrip())

# ----------------------------------
# 🔹 Why is Stripping Useful?
# ----------------------------------
# - When users accidentally type extra spaces
# - When reading names, cities, or books from user input
# - When saving data neatly for certificates or records
