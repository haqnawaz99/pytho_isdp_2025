# 2_11_teaching_whitespace_tabs_newlines.py

# ==================================================
# 📘 Teaching: Adding Whitespace in Strings
# ==================================================

# In Python, we can add spaces, tabs, and new lines inside text to make it neat and beautiful.

# ----------------------------------
# 🔹 1. Adding a Tab (\t)
# ----------------------------------
# A tab adds extra space, like moving forward before the next word.

student1 = "Muhammad Musa"
student2 = "Muhammad Abdullah"
student3 = "Muhammad Bilal"

# Example 1: Adding tab between two names
print(student1 + "\t" + student2)

# Example 2: Adding tab between three names
print(student1 + "\t" + student2 + "\t" + student3)

# ----------------------------------
# 🔹 2. Adding a Newline (\n)
# ----------------------------------
# A newline moves the next word or sentence to a new line.

madrasah_name = "Jamia Ashrafia"

# Example 1: Adding newline after madrasah name
print(madrasah_name + "\nLahore, Pakistan")

# Example 2: Welcome Message with Newline
print("Welcome to Jamia Ashrafia\nStart your classes at 8 AM")

# ----------------------------------
# 🔹 3. Combining Tabs and Newlines
# ----------------------------------
# We can use both together to format text beautifully.

teacher1 = "Ustad Abdul Wahid"
teacher2 = "Ustad Abu Bakar"
teacher3 = "Ustad Ahmed"
teacher4 = "Ustad Imran"

# Example 1: Teachers list
print("\nTeachers List:")
print("\t" + teacher1)
print("\t" + teacher2)
print("\t" + teacher3)
print("\t" + teacher4)

# Example 2: Subjects list with newlines and tabs
subject1 = "Fiqh"
subject2 = "Hadith"
subject3 = "Tafsir"
subject4 = "Arabic Grammar"

print("\nSubjects Offered:")
print("\t" + subject1)
print("\t" + subject2)
print("\t" + subject3)
print("\t" + subject4)

# ----------------------------------
# 🔹 4. Fun Example: Favorite Books
# ----------------------------------
book1 = "Tafsir Ibn Kathir"
book2 = "Sahih Bukhari"
book3 = "Al-Muwatta"

print("\nFavorite Islamic Books:")
print("\t" + book1)
print("\t" + book2)
print("\t" + book3)

# ----------------------------------
# 🔹 Real-Life Use
# ----------------------------------
# - Making attendance lists
# - Displaying student names cleanly
# - Printing certificates neatly
# - Organizing book or subject names
