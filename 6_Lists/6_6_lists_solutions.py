# 6_6_lists_solutions.py

# ==================================================
# 📝 Lists: Quiz Solutions
# ==================================================
# 🎯 Learning Objective: Check your answers
# 📚 Islamic Context: Complete solutions with explanations

print("📝 Lists and Data Structures Quiz Solutions")
print("=" * 50)
print("📌 These are the complete solutions.")
print("Compare with your answers to learn.")
print()

# ======================================
# 🔹 Section 1: Basic Lists - Solutions
# ======================================

print("🔹 Section 1: Basic Lists - Solutions")
print("-" * 40)

# Q1. Create a list of Islamic greetings - Solution
print("Q1. Create a list of Islamic greetings - Solution:")
islamic_greetings = ["Assalamu Alaikum", "Wa Alaikum Assalam", "Bismillah"]
print(f"Islamic greetings: {islamic_greetings}")
print("Explanation: Simple list creation with Islamic greetings")
print()

# Q2. Create a list of daily prayers - Solution
print("Q2. Create a list of daily prayers - Solution:")
daily_prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
print(f"Daily prayers: {daily_prayers}")
print(f"Number of prayers: {len(daily_prayers)}")
print("Explanation: List with prayer names and using len() function")
print()

# ======================================
# 🔹 Section 2: List Operations - Solutions
# ======================================

print("🔹 Section 2: List Operations - Solutions")
print("-" * 40)

# Q3. Add and remove elements from a list - Solution
print("Q3. Add and remove elements from a list - Solution:")
islamic_virtues = ["Honesty", "Kindness"]
print(f"Original virtues: {islamic_virtues}")

islamic_virtues.append("Patience")
print(f"After adding patience: {islamic_virtues}")

islamic_virtues.remove("Kindness")
print(f"After removing kindness: {islamic_virtues}")
print("Explanation: Using append() to add and remove() to delete elements")
print()

# Q4. Sort and reverse a list - Solution
print("Q4. Sort and reverse a list - Solution:")
islamic_names = ["Fatima", "Ahmed", "Zainab", "Ali"]
print(f"Original names: {islamic_names}")

islamic_names.sort()
print(f"Sorted names: {islamic_names}")

islamic_names.reverse()
print(f"Reversed names: {islamic_names}")
print("Explanation: Using sort() for alphabetical order and reverse() to flip order")
print()

# ======================================
# 🔹 Section 3: List Comprehension - Solutions
# ======================================

print("🔹 Section 3: List Comprehension - Solutions")
print("-" * 40)

# Q5. Create a list comprehension for personalized greetings - Solution
print("Q5. Create a list comprehension for personalized greetings - Solution:")
names = ["Ahmed", "Fatima", "Ali"]
greetings = [f"Assalamu Alaikum {name}" for name in names]
print(f"Names: {names}")
print(f"Personalized greetings: {greetings}")
print("Explanation: List comprehension with f-string formatting")
print()

# Q6. Filter high grades using list comprehension - Solution
print("Q6. Filter high grades using list comprehension - Solution:")
all_grades = [85, 92, 78, 95, 88, 70, 96]
high_grades = [grade for grade in all_grades if grade >= 90]
print(f"All grades: {all_grades}")
print(f"High grades (90+): {high_grades}")
print("Explanation: List comprehension with conditional filtering")
print()

# ======================================
# 🔹 Section 4: Tuples - Solutions
# ======================================

print("🔹 Section 4: Tuples - Solutions")
print("-" * 40)

# Q7. Create a tuple of prayer times - Solution
print("Q7. Create a tuple of prayer times - Solution:")
prayer_times = ("5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM")
print(f"Prayer times tuple: {prayer_times}")
print(f"First prayer time: {prayer_times[0]}")
print(f"Last prayer time: {prayer_times[-1]}")
print("Explanation: Tuple creation and accessing elements by index")
print()

# Q8. Tuple unpacking - Solution
print("Q8. Tuple unpacking - Solution:")
student_info = ("Ahmed", 15, "Quran")
name, age, subject = student_info
print(f"Student tuple: {student_info}")
print(f"Unpacked - Name: {name}, Age: {age}, Subject: {subject}")
print("Explanation: Tuple unpacking assigns values to multiple variables")
print()

# ======================================
# 🔹 Section 5: Sets - Solutions
# ======================================

print("🔹 Section 5: Sets - Solutions")
print("-" * 40)

# Q9. Create a set of unique Islamic virtues - Solution
print("Q9. Create a set of unique Islamic virtues - Solution:")
islamic_virtues_set = {"Honesty", "Kindness", "Patience", "Humility", "Generosity"}
print(f"Islamic virtues set: {islamic_virtues_set}")

islamic_virtues_set.add("Forgiveness")
print(f"After adding forgiveness: {islamic_virtues_set}")
print("Explanation: Set creation and adding elements with add() method")
print()

# Q10. Set operations - Solution
print("Q10. Set operations - Solution:")
basic_qualities = {"Honesty", "Kindness", "Patience"}
advanced_qualities = {"Wisdom", "Courage", "Patience", "Humility"}

common_qualities = basic_qualities.intersection(advanced_qualities)
print(f"Basic qualities: {basic_qualities}")
print(f"Advanced qualities: {advanced_qualities}")
print(f"Common qualities: {common_qualities}")
print("Explanation: Using intersection() to find common elements")
print()

# ======================================
# 🔹 Section 6: Dictionaries - Solutions
# ======================================

print("🔹 Section 6: Dictionaries - Solutions")
print("-" * 40)

# Q11. Create a dictionary of prayer times - Solution
print("Q11. Create a dictionary of prayer times - Solution:")
prayer_schedule = {
    "Fajr": "5:00 AM",
    "Dhuhr": "12:00 PM",
    "Asr": "3:00 PM",
    "Maghrib": "6:00 PM",
    "Isha": "8:00 PM"
}
print(f"Prayer schedule: {prayer_schedule}")
print(f"Fajr time: {prayer_schedule['Fajr']}")
print("Explanation: Dictionary creation with key-value pairs")
print()

# Q12. Dictionary operations - Solution
print("Q12. Dictionary operations - Solution:")
student = {"name": "Ahmed", "age": 15, "subject": "Quran"}
print(f"Original student: {student}")

student["grade"] = 95
print(f"After adding grade: {student}")

print(f"Student keys: {list(student.keys())}")
print(f"Student values: {list(student.values())}")
print("Explanation: Adding new key-value pairs and accessing keys/values")
print()

# ======================================
# 🔹 Section 7: Complex Data Structures - Solutions
# ======================================

print("🔹 Section 7: Complex Data Structures - Solutions")
print("-" * 40)

# Q13. Nested lists - Solution
print("Q13. Nested lists - Solution:")
students = [
    ["Ahmed", 15, "Quran"],
    ["Fatima", 14, "Hadith"],
    ["Ali", 16, "Fiqh"]
]
print(f"Students list: {students}")

for student in students:
    print(f"Name: {student[0]}, Age: {student[1]}, Subject: {student[2]}")
print("Explanation: List containing other lists and iterating through them")
print()

# Q14. Nested dictionaries - Solution
print("Q14. Nested dictionaries - Solution:")
detailed_student = {
    "name": "Ahmed",
    "grades": {
        "Quran": 95,
        "Hadith": 88,
        "Fiqh": 92
    }
}
print(f"Detailed student: {detailed_student}")
print(f"Quran grade: {detailed_student['grades']['Quran']}")
print("Explanation: Dictionary containing another dictionary")
print()

# ======================================
# 🔹 Section 8: Data Structure Conversions - Solutions
# ======================================

print("🔹 Section 8: Data Structure Conversions - Solutions")
print("-" * 40)

# Q15. Convert between data structures - Solution
print("Q15. Convert between data structures - Solution:")
prayer_list = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
print(f"Original list: {prayer_list}")

# Convert to tuple
prayer_tuple = tuple(prayer_list)
print(f"Converted to tuple: {prayer_tuple}")

# Convert to set
prayer_set = set(prayer_list)
print(f"Converted to set: {prayer_set}")

# Convert to dictionary
prayer_dict = {prayer: f"Time for {prayer}" for prayer in prayer_list}
print(f"Converted to dictionary: {prayer_dict}")
print("Explanation: Converting between different data structures")
print()

# ======================================
# 🔹 Section 9: Practical Applications - Solutions
# ======================================

print("🔹 Section 9: Practical Applications - Solutions")
print("-" * 40)

# Q16. Prayer tracker - Solution
print("Q16. Prayer tracker - Solution:")
completed_prayers = {"Fajr", "Dhuhr", "Asr"}
all_prayers = {"Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"}

remaining_prayers = all_prayers - completed_prayers
print(f"Completed prayers: {completed_prayers}")
print(f"All prayers: {all_prayers}")
print(f"Remaining prayers: {remaining_prayers}")
print("Explanation: Using set difference to find remaining prayers")
print()

# Q17. Grade calculator - Solution
print("Q17. Grade calculator - Solution:")
grades = [85, 92, 78, 95, 88]
print(f"Grades: {grades}")

total = sum(grades)
average = total / len(grades)
highest = max(grades)
lowest = min(grades)

print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print("Explanation: Using built-in functions for calculations")
print()

# ======================================
# 🔹 Section 10: Advanced Operations - Solutions
# ======================================

print("🔹 Section 10: Advanced Operations - Solutions")
print("-" * 40)

# Q18. List filtering and mapping - Solution
print("Q18. List filtering and mapping - Solution:")
islamic_subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah", "Seerah"]
print(f"All subjects: {islamic_subjects}")

# Filter long subjects
long_subjects = [subject for subject in islamic_subjects if len(subject) > 5]
print(f"Long subjects: {long_subjects}")

# Map to uppercase
uppercase_subjects = [subject.upper() for subject in islamic_subjects]
print(f"Uppercase subjects: {uppercase_subjects}")
print("Explanation: Combining filtering and mapping in list comprehensions")
print()

# Q19. Dictionary comprehension - Solution
print("Q19. Dictionary comprehension - Solution:")
subjects = ["Quran", "Hadith", "Fiqh"]
grades = [95, 88, 92]

subject_grades = {subject: grade for subject, grade in zip(subjects, grades)}
print(f"Subject grades: {subject_grades}")

# Add letter grades
letter_grades = {subject: "A" if grade >= 90 else "B" if grade >= 80 else "C" 
                for subject, grade in subject_grades.items()}
print(f"Letter grades: {letter_grades}")
print("Explanation: Dictionary comprehension with conditional logic")
print()

# ======================================
# 🔹 Bonus Challenge - Solution
# ======================================

print("🔹 Bonus Challenge - Solution:")
print("-" * 40)

# Q20. Islamic data management system - Solution
print("Q20. Islamic data management system - Solution:")

# Create comprehensive Islamic data structure
islamic_data = {
    "school": "Al-Noor Islamic School",
    "students": [
        {"name": "Ahmed", "age": 15, "grades": {"Quran": 95, "Hadith": 88}},
        {"name": "Fatima", "age": 14, "grades": {"Quran": 92, "Hadith": 90}},
        {"name": "Ali", "age": 16, "grades": {"Quran": 87, "Hadith": 85}}
    ],
    "subjects": ["Quran", "Hadith", "Fiqh", "Aqeedah"],
    "prayer_times": {
        "Fajr": "5:00 AM",
        "Dhuhr": "12:00 PM",
        "Asr": "3:00 PM",
        "Maghrib": "6:00 PM",
        "Isha": "8:00 PM"
    }
}

print("Islamic Data Management System:")
print(f"School: {islamic_data['school']}")
print(f"Subjects: {islamic_data['subjects']}")

print("\nStudent Information:")
for student in islamic_data['students']:
    name = student['name']
    age = student['age']
    avg_grade = sum(student['grades'].values()) / len(student['grades'])
    print(f"  {name} (Age: {age}) - Average Grade: {avg_grade:.1f}%")

print("\nPrayer Schedule:")
for prayer, time in islamic_data['prayer_times'].items():
    print(f"  {prayer}: {time}")

print("Explanation: Complex nested data structure combining lists and dictionaries")
print()

# ======================================
# 🔹 Additional Practice Examples
# ======================================

print("🔹 Additional Practice Examples:")
print("-" * 40)

# Example 1: Islamic calendar management
print("Example 1: Islamic Calendar Management:")
islamic_months = {
    "Muharram": {"days": 30, "special": "Day of Ashura"},
    "Safar": {"days": 29, "special": "Regular month"},
    "Rabi al-Awwal": {"days": 30, "special": "Birth of Prophet Muhammad (PBUH)"},
    "Ramadan": {"days": 30, "special": "Month of Fasting"},
    "Dhul Hijjah": {"days": 30, "special": "Month of Hajj"}
}

print("Islamic Calendar:")
for month, info in islamic_months.items():
    print(f"  {month}: {info['days']} days - {info['special']}")

# Example 2: Student performance analysis
print("\nExample 2: Student Performance Analysis:")
student_records = [
    {"name": "Ahmed", "grades": [85, 92, 78, 95, 88]},
    {"name": "Fatima", "grades": [90, 95, 88, 92, 89]},
    {"name": "Ali", "grades": [75, 82, 78, 85, 80]}
]

print("Student Performance Report:")
for student in student_records:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    print(f"  {name}:")
    print(f"    Average: {average:.1f}%")
    print(f"    Highest: {highest}%")
    print(f"    Lowest: {lowest}%")
    print(f"    Grade Range: {highest - lowest}%")

# Example 3: Prayer tracking system
print("\nExample 3: Prayer Tracking System:")
weekly_prayer_data = {
    "Monday": {"Fajr": True, "Dhuhr": True, "Asr": False, "Maghrib": True, "Isha": True},
    "Tuesday": {"Fajr": True, "Dhuhr": True, "Asr": True, "Maghrib": True, "Isha": False},
    "Wednesday": {"Fajr": False, "Dhuhr": True, "Asr": True, "Maghrib": True, "Isha": True},
    "Thursday": {"Fajr": True, "Dhuhr": True, "Asr": True, "Maghrib": True, "Isha": True},
    "Friday": {"Fajr": True, "Dhuhr": True, "Asr": True, "Maghrib": True, "Isha": True},
    "Saturday": {"Fajr": False, "Dhuhr": True, "Asr": True, "Maghrib": True, "Isha": True},
    "Sunday": {"Fajr": True, "Dhuhr": True, "Asr": True, "Maghrib": True, "Isha": True}
}

print("Weekly Prayer Report:")
total_prayers = 0
total_completed = 0

for day, prayers in weekly_prayer_data.items():
    day_completed = sum(prayers.values())
    day_total = len(prayers)
    total_prayers += day_total
    total_completed += day_completed
    
    percentage = (day_completed / day_total) * 100
    print(f"  {day}: {day_completed}/{day_total} prayers ({percentage:.1f}%)")

overall_percentage = (total_completed / total_prayers) * 100
print(f"\nOverall: {total_completed}/{total_prayers} prayers ({overall_percentage:.1f}%)")

if overall_percentage >= 90:
    print("🌟 Excellent prayer consistency!")
elif overall_percentage >= 80:
    print("✅ Good prayer consistency!")
else:
    print("💪 Keep working on prayer consistency!")

print()
print("🎉 All solutions completed!")
print("📚 Keep practicing and learning data structures!")
print("🕌 Data structures help you organize Islamic information effectively!") 