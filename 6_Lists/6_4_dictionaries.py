# 6_4_dictionaries.py

# ==================================================
# 📝 Lists: Dictionaries
# ==================================================
# 🎯 Learning Objective: Learn about dictionaries as key-value data structures
# 📚 Islamic Context: Using Islamic examples to understand dictionaries

print("📖 Welcome to Dictionaries")
print("=" * 50)

# ======================================
# 🔹 What is a Dictionary?
# ======================================

print("🔹 What is a Dictionary?")
print("-" * 30)
print("A dictionary stores data as key-value pairs.")
print("Each key has a corresponding value, like a real dictionary.")
print("In Islamic terms: Like a dictionary of prayer times or student records!")
print()

# ======================================
# 🔹 Example 1: Basic Dictionary Creation
# ======================================

print("🔹 Example 1: Basic Dictionary Creation")
print("-" * 30)

# Create a dictionary of prayer times
prayer_times = {
    "Fajr": "5:00 AM",
    "Dhuhr": "12:00 PM",
    "Asr": "3:00 PM",
    "Maghrib": "6:00 PM",
    "Isha": "8:00 PM"
}
print(f"Prayer times: {prayer_times}")

# Create a student dictionary
student = {
    "name": "Ahmed",
    "age": 15,
    "subject": "Quran",
    "grade": 95
}
print(f"Student info: {student}")
print()

# ======================================
# 🔹 Example 2: Accessing Dictionary Values
# ======================================

print("🔹 Example 2: Accessing Dictionary Values")
print("-" * 30)

# Access values using keys
print(f"Fajr prayer time: {prayer_times['Fajr']}")
print(f"Dhuhr prayer time: {prayer_times['Dhuhr']}")

# Access student information
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")
print(f"Student subject: {student['subject']}")
print(f"Student grade: {student['grade']}")

# Using get() method (safer)
print(f"Fajr time (using get): {prayer_times.get('Fajr')}")
print(f"Non-existent prayer: {prayer_times.get('Tahajjud', 'Not found')}")
print()

# ======================================
# 🔹 Example 3: Modifying Dictionaries
# ======================================

print("🔹 Example 3: Modifying Dictionaries")
print("-" * 30)

# Add new key-value pairs
prayer_times["Tahajjud"] = "2:00 AM"
print(f"After adding Tahajjud: {prayer_times}")

# Update existing values
prayer_times["Fajr"] = "5:15 AM"
print(f"After updating Fajr: {prayer_times}")

# Add student information
student["class"] = "10th Grade"
student["teacher"] = "Maulana Ali"
print(f"Updated student info: {student}")
print()

# ======================================
# 🔹 Example 4: Dictionary Methods
# ======================================

print("🔹 Example 4: Dictionary Methods")
print("-" * 30)

# Get all keys
prayer_keys = list(prayer_times.keys())
print(f"Prayer names: {prayer_keys}")

# Get all values
prayer_values = list(prayer_times.values())
print(f"Prayer times: {prayer_values}")

# Get all items
prayer_items = list(prayer_times.items())
print(f"Prayer items: {prayer_items}")

# Check if key exists
print(f"Is 'Fajr' in prayers? {'Fajr' in prayer_times}")
print(f"Is 'Tahajjud' in prayers? {'Tahajjud' in prayer_times}")

# Dictionary length
print(f"Number of prayers: {len(prayer_times)}")
print()

# ======================================
# 🔹 Example 5: Nested Dictionaries
# ======================================

print("🔹 Example 5: Nested Dictionaries")
print("-" * 30)

# Student with detailed information
detailed_student = {
    "name": "Ahmed",
    "age": 15,
    "grades": {
        "Quran": 95,
        "Hadith": 88,
        "Fiqh": 92
    },
    "schedule": {
        "Monday": "Quran",
        "Tuesday": "Hadith",
        "Wednesday": "Fiqh"
    }
}

print(f"Detailed student: {detailed_student}")

# Access nested values
print(f"Student's Quran grade: {detailed_student['grades']['Quran']}")
print(f"Monday's subject: {detailed_student['schedule']['Monday']}")

# Islamic school with multiple students
islamic_school = {
    "name": "Al-Noor Islamic School",
    "students": {
        "Ahmed": {"age": 15, "grade": "10th", "subject": "Quran"},
        "Fatima": {"age": 14, "grade": "9th", "subject": "Hadith"},
        "Ali": {"age": 16, "grade": "11th", "subject": "Fiqh"}
    }
}

print(f"\nSchool: {islamic_school['name']}")
print(f"Ahmed's information: {islamic_school['students']['Ahmed']}")
print()

# ======================================
# 🔹 Example 6: Dictionary Operations
# ======================================

print("🔹 Example 6: Dictionary Operations")
print("-" * 30)

# Copy dictionary
original_prayers = {"Fajr": "5:00 AM", "Dhuhr": "12:00 PM"}
copied_prayers = original_prayers.copy()
print(f"Original: {original_prayers}")
print(f"Copy: {copied_prayers}")

# Update dictionary
morning_prayers = {"Fajr": "5:15 AM", "Sunrise": "6:30 AM"}
original_prayers.update(morning_prayers)
print(f"After update: {original_prayers}")

# Remove items
removed_time = original_prayers.pop("Sunrise")
print(f"Removed time: {removed_time}")
print(f"After removal: {original_prayers}")

# Clear dictionary
temp_dict = {"temp": "value"}
temp_dict.clear()
print(f"After clear: {temp_dict}")
print()

# ======================================
# 🔹 Example 7: Dictionary Comprehension
# ======================================

print("🔹 Example 7: Dictionary Comprehension")
print("-" * 30)

# Create dictionary from lists
prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
times = ["5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM"]

prayer_schedule = {prayer: time for prayer, time in zip(prayers, times)}
print(f"Prayer schedule: {prayer_schedule}")

# Create dictionary with conditions
grades = [85, 92, 78, 95, 88]
students = ["Ahmed", "Fatima", "Ali", "Hassan", "Aisha"]

passing_students = {student: grade for student, grade in zip(students, grades) if grade >= 80}
print(f"Passing students: {passing_students}")

# Transform existing dictionary
original_grades = {"Quran": 85, "Hadith": 92, "Fiqh": 78}
letter_grades = {subject: "A" if grade >= 90 else "B" if grade >= 80 else "C" 
                for subject, grade in original_grades.items()}
print(f"Original grades: {original_grades}")
print(f"Letter grades: {letter_grades}")
print()

# ======================================
# 🔹 Example 8: Dictionary Iteration
# ======================================

print("🔹 Example 8: Dictionary Iteration")
print("-" * 30)

# Iterate through keys
print("Prayer times:")
for prayer in prayer_times.keys():
    print(f"  {prayer}: {prayer_times[prayer]}")

# Iterate through values
print(f"\nAll prayer times: {list(prayer_times.values())}")

# Iterate through items
print("\nPrayer schedule:")
for prayer, time in prayer_times.items():
    print(f"  {prayer} prayer at {time}")

# Iterate through nested dictionary
print("\nStudent grades:")
for subject, grade in detailed_student["grades"].items():
    print(f"  {subject}: {grade}%")
print()

# ======================================
# 🔹 Example 9: Dictionary Applications
# ======================================

print("🔹 Example 9: Dictionary Applications")
print("-" * 30)

# Islamic calendar
islamic_calendar = {
    "Muharram": {"days": 30, "special": "Day of Ashura"},
    "Ramadan": {"days": 30, "special": "Month of Fasting"},
    "Dhul Hijjah": {"days": 30, "special": "Month of Hajj"}
}

print("Islamic Calendar:")
for month, info in islamic_calendar.items():
    print(f"  {month}: {info['days']} days - {info['special']}")

# Prayer status tracker
prayer_status = {
    "Fajr": True,
    "Dhuhr": True,
    "Asr": False,
    "Maghrib": True,
    "Isha": False
}

print(f"\nPrayer Status:")
completed = sum(prayer_status.values())
total = len(prayer_status)
print(f"  Completed: {completed}/{total} prayers")

for prayer, completed in prayer_status.items():
    status = "✅" if completed else "❌"
    print(f"  {prayer}: {status}")

# Islamic book library
library = {
    "Quran": {"copies": 5, "available": 3},
    "Sahih Bukhari": {"copies": 2, "available": 1},
    "Sahih Muslim": {"copies": 2, "available": 2},
    "Abu Dawud": {"copies": 1, "available": 0}
}

print(f"\nLibrary Status:")
for book, info in library.items():
    borrowed = info["copies"] - info["available"]
    print(f"  {book}: {info['available']}/{info['copies']} available ({borrowed} borrowed)")
print()

# ======================================
# 🔹 Example 10: Advanced Dictionary Operations
# ======================================

print("🔹 Example 10: Advanced Dictionary Operations")
print("-" * 30)

# Merge dictionaries
morning_schedule = {"Fajr": "5:00 AM", "Sunrise": "6:30 AM"}
afternoon_schedule = {"Dhuhr": "12:00 PM", "Asr": "3:00 PM"}
evening_schedule = {"Maghrib": "6:00 PM", "Isha": "8:00 PM"}

# Method 1: Using update()
full_schedule = {}
full_schedule.update(morning_schedule)
full_schedule.update(afternoon_schedule)
full_schedule.update(evening_schedule)
print(f"Full schedule (update): {full_schedule}")

# Method 2: Using | operator (Python 3.9+)
# full_schedule = morning_schedule | afternoon_schedule | evening_schedule

# Method 3: Using ** unpacking
full_schedule_alt = {**morning_schedule, **afternoon_schedule, **evening_schedule}
print(f"Full schedule (unpacking): {full_schedule_alt}")

# Dictionary with default values
from collections import defaultdict

# Count prayer completions
prayer_count = defaultdict(int)
weekly_prayers = ["Fajr", "Dhuhr", "Asr", "Fajr", "Maghrib", "Fajr", "Isha"]

for prayer in weekly_prayers:
    prayer_count[prayer] += 1

print(f"\nPrayer count this week: {dict(prayer_count)}")

# Group students by grade
students_by_grade = defaultdict(list)
student_records = [
    {"name": "Ahmed", "grade": "10th"},
    {"name": "Fatima", "grade": "9th"},
    {"name": "Ali", "grade": "10th"},
    {"name": "Aisha", "grade": "9th"}
]

for student in student_records:
    students_by_grade[student["grade"]].append(student["name"])

print(f"Students by grade: {dict(students_by_grade)}")
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Work with dictionaries:")
print("1. Create a dictionary of Islamic months and their days")
print("2. Create a student dictionary with grades")
print("3. Count occurrences of prayer names in a list")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Islamic months dictionary
islamic_months = {
    "Muharram": 30,
    "Safar": 29,
    "Rabi al-Awwal": 30,
    "Ramadan": 30
}
print(f"1. Islamic months: {islamic_months}")

# 2. Student with grades
student_grades = {
    "name": "Ahmed",
    "Quran": 95,
    "Hadith": 88,
    "Fiqh": 92
}
print(f"\n2. Student grades: {student_grades}")

# 3. Count prayer occurrences
prayer_list = ["Fajr", "Dhuhr", "Asr", "Fajr", "Maghrib", "Fajr"]
prayer_count = {}
for prayer in prayer_list:
    prayer_count[prayer] = prayer_count.get(prayer, 0) + 1
print(f"\n3. Prayer count: {prayer_count}")

print()
print("🎉 Congratulations! You've learned dictionaries!")
print("📚 Dictionaries are powerful for storing and organizing related data!") 