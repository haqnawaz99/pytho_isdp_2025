# 6_3_tuples_and_sets.py

# ==================================================
# 📝 Lists: Tuples and Sets
# ==================================================
# 🎯 Learning Objective: Learn about tuples and sets as data structures
# 📚 Islamic Context: Using Islamic examples to understand tuples and sets

print("📦 Welcome to Tuples and Sets")
print("=" * 50)

# ======================================
# 🔹 What are Tuples and Sets?
# ======================================

print("🔹 What are Tuples and Sets?")
print("-" * 30)
print("Tuples are like lists but cannot be changed (immutable).")
print("Sets are collections of unique items without order.")
print("In Islamic terms: Tuples like fixed prayer times, Sets like unique Islamic virtues!")
print()

# ======================================
# 🔹 Example 1: Basic Tuples
# ======================================

print("🔹 Example 1: Basic Tuples")
print("-" * 30)

# Create tuples with Islamic data
prayer_times = ("5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM")
print(f"Prayer times tuple: {prayer_times}")

student_info = ("Ahmed", 15, "Quran")
print(f"Student info tuple: {student_info}")

# Access tuple elements
print(f"First prayer time: {prayer_times[0]}")
print(f"Student name: {student_info[0]}")
print(f"Student age: {student_info[1]}")

# Tuple length
print(f"Number of prayer times: {len(prayer_times)}")
print()

# ======================================
# 🔹 Example 2: Tuple Immutability
# ======================================

print("🔹 Example 2: Tuple Immutability")
print("-" * 30)

# Create a tuple
islamic_constants = ("Allah", "Muhammad", "Quran")
print(f"Islamic constants: {islamic_constants}")

# Try to modify (this will cause an error)
try:
    islamic_constants[0] = "God"
    print("This won't print")
except TypeError as e:
    print(f"Cannot modify tuple: {e}")

# But we can create a new tuple
new_constants = ("Allah", "Muhammad", "Quran", "Islam")
print(f"New constants tuple: {new_constants}")

# Tuple unpacking
name, age, subject = student_info
print(f"Unpacked: Name={name}, Age={age}, Subject={subject}")
print()

# ======================================
# 🔹 Example 3: Tuple Methods
# ======================================

print("🔹 Example 3: Tuple Methods")
print("-" * 30)

# Count occurrences
prayer_list = ("Fajr", "Dhuhr", "Asr", "Fajr", "Maghrib", "Fajr")
print(f"Prayer tuple: {prayer_list}")
print(f"Number of 'Fajr': {prayer_list.count('Fajr')}")

# Find index
print(f"Index of 'Dhuhr': {prayer_list.index('Dhuhr')}")

# Check if element exists
print(f"Is 'Isha' in prayers? {'Isha' in prayer_list}")
print(f"Is 'Fajr' in prayers? {'Fajr' in prayer_list}")
print()

# ======================================
# 🔹 Example 4: Tuple Concatenation
# ======================================

print("🔹 Example 4: Tuple Concatenation")
print("-" * 30)

# Combine tuples
morning_prayers = ("Fajr",)
afternoon_prayers = ("Dhuhr", "Asr")
evening_prayers = ("Maghrib", "Isha")

all_prayers = morning_prayers + afternoon_prayers + evening_prayers
print(f"All prayers: {all_prayers}")

# Repeat tuples
greeting = ("Assalamu Alaikum",)
repeated_greeting = greeting * 3
print(f"Repeated greeting: {repeated_greeting}")
print()

# ======================================
# 🔹 Example 5: Basic Sets
# ======================================

print("🔹 Example 5: Basic Sets")
print("-" * 30)

# Create sets of Islamic virtues
islamic_virtues = {"Honesty", "Kindness", "Patience", "Humility", "Generosity"}
print(f"Islamic virtues set: {islamic_virtues}")

# Create set from list
prayer_names = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha", "Fajr", "Dhuhr"]
unique_prayers = set(prayer_names)
print(f"Original prayer list: {prayer_names}")
print(f"Unique prayers set: {unique_prayers}")

# Set properties
print(f"Number of unique virtues: {len(islamic_virtues)}")
print(f"Is 'Honesty' in virtues? {'Honesty' in islamic_virtues}")
print()

# ======================================
# 🔹 Example 6: Set Operations
# ======================================

print("🔹 Example 6: Set Operations")
print("-" * 30)

# Add elements to set
islamic_virtues.add("Forgiveness")
print(f"After adding 'Forgiveness': {islamic_virtues}")

# Remove elements
islamic_virtues.remove("Humility")
print(f"After removing 'Humility': {islamic_virtues}")

# Discard (safe remove)
islamic_virtues.discard("NonExistentVirtue")  # No error
print(f"After discarding non-existent: {islamic_virtues}")

# Pop random element
popped_virtue = islamic_virtues.pop()
print(f"Popped virtue: {popped_virtue}")
print(f"Remaining virtues: {islamic_virtues}")
print()

# ======================================
# 🔹 Example 7: Set Union and Intersection
# ======================================

print("🔹 Example 7: Set Union and Intersection")
print("-" * 30)

# Two sets of Islamic qualities
basic_qualities = {"Honesty", "Kindness", "Patience"}
advanced_qualities = {"Wisdom", "Courage", "Patience", "Humility"}

print(f"Basic qualities: {basic_qualities}")
print(f"Advanced qualities: {advanced_qualities}")

# Union (all qualities)
all_qualities = basic_qualities.union(advanced_qualities)
print(f"All qualities (union): {all_qualities}")

# Intersection (common qualities)
common_qualities = basic_qualities.intersection(advanced_qualities)
print(f"Common qualities (intersection): {common_qualities}")

# Difference (unique to first set)
unique_basic = basic_qualities.difference(advanced_qualities)
print(f"Unique to basic: {unique_basic}")

# Symmetric difference (unique to each set)
unique_to_each = basic_qualities.symmetric_difference(advanced_qualities)
print(f"Unique to each set: {unique_to_each}")
print()

# ======================================
# 🔹 Example 8: Set Comprehension
# ======================================

print("🔹 Example 8: Set Comprehension")
print("-" * 30)

# Create set of Islamic names
names = ["Ahmed", "Fatima", "Ali", "Aisha", "Hassan", "Ahmed", "Fatima"]
unique_names = {name for name in names}
print(f"Original names: {names}")
print(f"Unique names set: {unique_names}")

# Create set of long Islamic subjects
subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah", "Seerah", "Tafsir"]
long_subjects = {subject for subject in subjects if len(subject) > 5}
print(f"All subjects: {subjects}")
print(f"Long subjects set: {long_subjects}")

# Create set of high grades
grades = [85, 92, 78, 95, 88, 70, 96, 95, 92]
excellent_grades = {grade for grade in grades if grade >= 90}
print(f"All grades: {grades}")
print(f"Excellent grades set: {excellent_grades}")
print()

# ======================================
# 🔹 Example 9: Converting Between Data Types
# ======================================

print("🔹 Example 9: Converting Between Data Types")
print("-" * 30)

# List to tuple
prayer_list = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
prayer_tuple = tuple(prayer_list)
print(f"Original list: {prayer_list}")
print(f"Converted to tuple: {prayer_tuple}")

# List to set
duplicate_names = ["Ahmed", "Fatima", "Ali", "Ahmed", "Fatima"]
unique_names_set = set(duplicate_names)
print(f"\nList with duplicates: {duplicate_names}")
print(f"Converted to set: {unique_names_set}")

# Tuple to list
student_tuple = ("Ahmed", 15, "Quran")
student_list = list(student_tuple)
print(f"\nOriginal tuple: {student_tuple}")
print(f"Converted to list: {student_list}")

# Set to list
virtues_set = {"Honesty", "Kindness", "Patience"}
virtues_list = list(virtues_set)
print(f"\nOriginal set: {virtues_set}")
print(f"Converted to list: {virtues_list}")
print()

# ======================================
# 🔹 Example 10: Practical Applications
# ======================================

print("🔹 Example 10: Practical Applications")
print("-" * 30)

# Tuple for fixed prayer schedule
prayer_schedule = (
    ("Fajr", "5:00 AM"),
    ("Dhuhr", "12:00 PM"),
    ("Asr", "3:00 PM"),
    ("Maghrib", "6:00 PM"),
    ("Isha", "8:00 PM")
)

print("Prayer Schedule:")
for prayer, time in prayer_schedule:
    print(f"  {prayer}: {time}")

# Set for tracking completed prayers
completed_prayers = {"Fajr", "Dhuhr", "Asr"}
print(f"\nCompleted prayers: {completed_prayers}")

# Check if all prayers are completed
all_prayers_set = {"Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"}
remaining_prayers = all_prayers_set - completed_prayers
print(f"Remaining prayers: {remaining_prayers}")

# Tuple for student record (immutable)
student_record = ("Ahmed", 15, "Quran", 95)
name, age, subject, grade = student_record
print(f"\nStudent Record:")
print(f"  Name: {name}")
print(f"  Age: {age}")
print(f"  Subject: {subject}")
print(f"  Grade: {grade}")

# Set for unique Islamic books
available_books = {"Quran", "Sahih Bukhari", "Sahih Muslim", "Abu Dawud"}
borrowed_books = {"Quran", "Sahih Bukhari"}
available_now = available_books - borrowed_books
print(f"\nAvailable books: {available_books}")
print(f"Borrowed books: {borrowed_books}")
print(f"Available now: {available_now}")
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Work with tuples and sets:")
print("1. Create a tuple of Islamic months")
print("2. Create a set of unique Islamic names")
print("3. Convert a list to tuple and set")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Tuple of Islamic months
islamic_months = ("Muharram", "Safar", "Rabi al-Awwal", "Ramadan")
print(f"1. Islamic months tuple: {islamic_months}")

# 2. Set of unique names
names_list = ["Ahmed", "Fatima", "Ali", "Ahmed", "Fatima"]
unique_names = set(names_list)
print(f"\n2. Original names: {names_list}")
print(f"   Unique names set: {unique_names}")

# 3. Convert list to tuple and set
original_list = ["Quran", "Hadith", "Fiqh", "Quran"]
converted_tuple = tuple(original_list)
converted_set = set(original_list)
print(f"\n3. Original list: {original_list}")
print(f"   Converted to tuple: {converted_tuple}")
print(f"   Converted to set: {converted_set}")

print()
print("🎉 Congratulations! You've learned tuples and sets!")
print("📚 Tuples and sets are powerful data structures for different needs!") 