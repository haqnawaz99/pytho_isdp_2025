# 6_1_basic_lists.py

# ==================================================
# 📝 Lists: Basic List Concepts
# ==================================================
# 🎯 Learning Objective: Understand what lists are and how to create them
# 📚 Islamic Context: Using Islamic examples to learn lists

print("📋 Welcome to Lists and Data Structures")
print("=" * 50)

# ======================================
# 🔹 What is a List?
# ======================================

print("🔹 What is a List?")
print("-" * 30)
print("A list is like a container that holds multiple items.")
print("Lists help us organize and store related data together.")
print("In Islamic terms: Like a list of daily prayers or Islamic subjects!")
print()

# ======================================
# 🔹 Example 1: Simple List Creation
# ======================================

print("🔹 Example 1: Simple List Creation")
print("-" * 30)

# Create a list of Islamic greetings
islamic_greetings = ["Assalamu Alaikum", "Wa Alaikum Assalam", "Bismillah"]
print(f"Islamic greetings: {islamic_greetings}")

# Create a list of prayer names
prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
print(f"Daily prayers: {prayers}")

# Create a list of Islamic subjects
subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah", "Seerah"]
print(f"Islamic subjects: {subjects}")
print()

# ======================================
# 🔹 Example 2: List with Different Data Types
# ======================================

print("🔹 Example 2: List with Different Data Types")
print("-" * 30)

# List with mixed data types
student_info = ["Ahmed", 15, "Quran", True]
print(f"Student info: {student_info}")
print(f"Name: {student_info[0]}")
print(f"Age: {student_info[1]}")
print(f"Favorite subject: {student_info[2]}")
print(f"Is student: {student_info[3]}")
print()

# ======================================
# 🔹 Example 3: Accessing List Elements
# ======================================

print("🔹 Example 3: Accessing List Elements")
print("-" * 30)

# Islamic names list
islamic_names = ["Ahmed", "Fatima", "Ali", "Aisha", "Hassan"]
print(f"All names: {islamic_names}")

# Access individual elements
print(f"First name: {islamic_names[0]}")
print(f"Second name: {islamic_names[1]}")
print(f"Third name: {islamic_names[2]}")
print(f"Last name: {islamic_names[-1]}")
print(f"Second to last: {islamic_names[-2]}")
print()

# ======================================
# 🔹 Example 4: List Length and Basic Operations
# ======================================

print("🔹 Example 4: List Length and Basic Operations")
print("-" * 30)

# Prayer times list
prayer_times = ["5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM"]
print(f"Prayer times: {prayer_times}")
print(f"Number of prayers: {len(prayer_times)}")

# Check if element exists
print(f"Is 'Fajr' in prayers? {'Fajr' in prayers}")
print(f"Is '5:00 AM' in prayer times? {'5:00 AM' in prayer_times}")
print()

# ======================================
# 🔹 Example 5: Adding Elements to Lists
# ======================================

print("🔹 Example 5: Adding Elements to Lists")
print("-" * 30)

# Start with basic Islamic virtues
virtues = ["Honesty", "Kindness"]
print(f"Original virtues: {virtues}")

# Add more virtues
virtues.append("Patience")
print(f"After adding patience: {virtues}")

virtues.append("Humility")
print(f"After adding humility: {virtues}")

# Add multiple elements
virtues.extend(["Generosity", "Forgiveness"])
print(f"After extending: {virtues}")
print()

# ======================================
# 🔹 Example 6: Removing Elements from Lists
# ======================================

print("🔹 Example 6: Removing Elements from Lists")
print("-" * 30)

# List of Islamic activities
activities = ["Prayer", "Quran Reading", "Dhikr", "Helping Others", "Studying"]
print(f"Original activities: {activities}")

# Remove by value
activities.remove("Dhikr")
print(f"After removing 'Dhikr': {activities}")

# Remove by index
removed_activity = activities.pop(1)
print(f"Removed activity: {removed_activity}")
print(f"After pop(1): {activities}")

# Remove last element
last_activity = activities.pop()
print(f"Removed last activity: {last_activity}")
print(f"After pop(): {activities}")
print()

# ======================================
# 🔹 Example 7: List Slicing
# ======================================

print("🔹 Example 7: List Slicing")
print("-" * 30)

# Islamic months list
islamic_months = ["Muharram", "Safar", "Rabi al-Awwal", "Rabi al-Thani", 
                  "Jumada al-Awwal", "Jumada al-Thani", "Rajab", "Shaban",
                  "Ramadan", "Shawwal", "Dhul Qadah", "Dhul Hijjah"]

print(f"All months: {islamic_months}")

# Get first 3 months
first_three = islamic_months[0:3]
print(f"First three months: {first_three}")

# Get last 3 months
last_three = islamic_months[-3:]
print(f"Last three months: {last_three}")

# Get months 3 to 6
middle_months = islamic_months[2:6]
print(f"Middle months (3-6): {middle_months}")

# Get every second month
every_second = islamic_months[::2]
print(f"Every second month: {every_second}")
print()

# ======================================
# 🔹 Example 8: List Methods
# ======================================

print("🔹 Example 8: List Methods")
print("-" * 30)

# Islamic books list
books = ["Quran", "Sahih Bukhari", "Sahih Muslim"]
print(f"Original books: {books}")

# Sort the list
books.sort()
print(f"Sorted books: {books}")

# Reverse the list
books.reverse()
print(f"Reversed books: {books}")

# Count occurrences
duplicate_books = ["Quran", "Hadith", "Quran", "Fiqh", "Quran"]
print(f"Books with duplicates: {duplicate_books}")
print(f"Number of 'Quran' books: {duplicate_books.count('Quran')}")

# Find index
print(f"Index of 'Hadith': {duplicate_books.index('Hadith')}")
print()

# ======================================
# 🔹 Example 9: List with Numbers
# ======================================

print("🔹 Example 9: List with Numbers")
print("-" * 30)

# Student grades
quran_grades = [85, 92, 78, 95, 88]
print(f"Quran grades: {quran_grades}")

# Calculate statistics
total = sum(quran_grades)
average = total / len(quran_grades)
highest = max(quran_grades)
lowest = min(quran_grades)

print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")

# Prayer count for the week
weekly_prayers = [5, 5, 4, 5, 3, 5, 5]
print(f"Weekly prayers completed: {weekly_prayers}")
print(f"Total prayers this week: {sum(weekly_prayers)}")
print(f"Average prayers per day: {sum(weekly_prayers)/len(weekly_prayers):.1f}")
print()

# ======================================
# 🔹 Example 10: Nested Lists
# ======================================

print("🔹 Example 10: Nested Lists")
print("-" * 30)

# List of students with their information
students = [
    ["Ahmed", 15, "Quran"],
    ["Fatima", 14, "Hadith"],
    ["Ali", 16, "Fiqh"],
    ["Aisha", 13, "Aqeedah"]
]

print("Students information:")
for student in students:
    print(f"Name: {student[0]}, Age: {student[1]}, Subject: {student[2]}")

# Access specific student
print(f"\nFirst student: {students[0]}")
print(f"First student's name: {students[0][0]}")
print(f"First student's age: {students[0][1]}")
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create lists for:")
print("1. A list of 3 Islamic names")
print("2. A list of prayer times")
print("3. A list of your grades in Islamic subjects")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Islamic names list
names = ["Ahmed", "Fatima", "Ali"]
print(f"1. Islamic names: {names}")

# 2. Prayer times list
times = ["5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM"]
print(f"2. Prayer times: {times}")

# 3. Grades list
grades = [85, 92, 78]
print(f"3. Grades: {grades}")
print(f"   Average grade: {sum(grades)/len(grades):.1f}")

print()
print("🎉 Congratulations! You've learned basic lists!")
print("📚 Lists help you organize and manage multiple pieces of data!") 