# 6_5_lists_quiz.py

# ==================================================
# 📝 Lists: Final Quiz
# ==================================================
# 🎯 Learning Objective: Test understanding of lists and data structures
# 📚 Islamic Context: Using Islamic examples in the quiz

print("📝 Lists and Data Structures Final Quiz")
print("=" * 50)
print("📌 Instructions:")
print("Solve all questions step-by-step.")
print("Do not skip any part.")
print()

# ======================================
# 🔹 Section 1: Basic Lists
# ======================================

print("🔹 Section 1: Basic Lists")
print("-" * 30)

# Q1. Create a list of Islamic greetings
print("Q1. Create a list of Islamic greetings")
# 👇 Write your code below:
islamic_greetings = ["Assalamu Alaikum", "Wa Alaikum Assalam", "Bismillah"]
print(f"Islamic greetings: {islamic_greetings}")
print()

# Q2. Create a list of daily prayers
print("Q2. Create a list of daily prayers")
# 👇 Write your code below:
daily_prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
print(f"Daily prayers: {daily_prayers}")
print(f"Number of prayers: {len(daily_prayers)}")
print()

# ======================================
# 🔹 Section 2: List Operations
# ======================================

print("🔹 Section 2: List Operations")
print("-" * 30)

# Q3. Add and remove elements from a list
print("Q3. Add and remove elements from a list")
# 👇 Write your code below:
islamic_virtues = ["Honesty", "Kindness"]
print(f"Original virtues: {islamic_virtues}")

islamic_virtues.append("Patience")
print(f"After adding patience: {islamic_virtues}")

islamic_virtues.remove("Kindness")
print(f"After removing kindness: {islamic_virtues}")
print()

# Q4. Sort and reverse a list
print("Q4. Sort and reverse a list")
# 👇 Write your code below:
islamic_names = ["Fatima", "Ahmed", "Zainab", "Ali"]
print(f"Original names: {islamic_names}")

islamic_names.sort()
print(f"Sorted names: {islamic_names}")

islamic_names.reverse()
print(f"Reversed names: {islamic_names}")
print()

# ======================================
# 🔹 Section 3: List Comprehension
# ======================================

print("🔹 Section 3: List Comprehension")
print("-" * 30)

# Q5. Create a list comprehension for personalized greetings
print("Q5. Create a list comprehension for personalized greetings")
# 👇 Write your code below:
names = ["Ahmed", "Fatima", "Ali"]
greetings = [f"Assalamu Alaikum {name}" for name in names]
print(f"Names: {names}")
print(f"Personalized greetings: {greetings}")
print()

# Q6. Filter high grades using list comprehension
print("Q6. Filter high grades using list comprehension")
# 👇 Write your code below:
all_grades = [85, 92, 78, 95, 88, 70, 96]
high_grades = [grade for grade in all_grades if grade >= 90]
print(f"All grades: {all_grades}")
print(f"High grades (90+): {high_grades}")
print()

# ======================================
# 🔹 Section 4: Tuples
# ======================================

print("🔹 Section 4: Tuples")
print("-" * 30)

# Q7. Create a tuple of prayer times
print("Q7. Create a tuple of prayer times")
# 👇 Write your code below:
prayer_times = ("5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM")
print(f"Prayer times tuple: {prayer_times}")
print(f"First prayer time: {prayer_times[0]}")
print(f"Last prayer time: {prayer_times[-1]}")
print()

# Q8. Tuple unpacking
print("Q8. Tuple unpacking")
# 👇 Write your code below:
student_info = ("Ahmed", 15, "Quran")
name, age, subject = student_info
print(f"Student tuple: {student_info}")
print(f"Unpacked - Name: {name}, Age: {age}, Subject: {subject}")
print()

# ======================================
# 🔹 Section 5: Sets
# ======================================

print("🔹 Section 5: Sets")
print("-" * 30)

# Q9. Create a set of unique Islamic virtues
print("Q9. Create a set of unique Islamic virtues")
# 👇 Write your code below:
islamic_virtues_set = {"Honesty", "Kindness", "Patience", "Humility", "Generosity"}
print(f"Islamic virtues set: {islamic_virtues_set}")

islamic_virtues_set.add("Forgiveness")
print(f"After adding forgiveness: {islamic_virtues_set}")
print()

# Q10. Set operations
print("Q10. Set operations")
# 👇 Write your code below:
basic_qualities = {"Honesty", "Kindness", "Patience"}
advanced_qualities = {"Wisdom", "Courage", "Patience", "Humility"}

common_qualities = basic_qualities.intersection(advanced_qualities)
print(f"Basic qualities: {basic_qualities}")
print(f"Advanced qualities: {advanced_qualities}")
print(f"Common qualities: {common_qualities}")
print()

# ======================================
# 🔹 Section 6: Dictionaries
# ======================================

print("🔹 Section 6: Dictionaries")
print("-" * 30)

# Q11. Create a dictionary of prayer times
print("Q11. Create a dictionary of prayer times")
# 👇 Write your code below:
prayer_schedule = {
    "Fajr": "5:00 AM",
    "Dhuhr": "12:00 PM",
    "Asr": "3:00 PM",
    "Maghrib": "6:00 PM",
    "Isha": "8:00 PM"
}
print(f"Prayer schedule: {prayer_schedule}")
print(f"Fajr time: {prayer_schedule['Fajr']}")
print()

# Q12. Dictionary operations
print("Q12. Dictionary operations")
# 👇 Write your code below:
student = {"name": "Ahmed", "age": 15, "subject": "Quran"}
print(f"Original student: {student}")

student["grade"] = 95
print(f"After adding grade: {student}")

print(f"Student keys: {list(student.keys())}")
print(f"Student values: {list(student.values())}")
print()

# ======================================
# 🔹 Section 7: Complex Data Structures
# ======================================

print("🔹 Section 7: Complex Data Structures")
print("-" * 30)

# Q13. Nested lists
print("Q13. Nested lists")
# 👇 Write your code below:
students = [
    ["Ahmed", 15, "Quran"],
    ["Fatima", 14, "Hadith"],
    ["Ali", 16, "Fiqh"]
]
print(f"Students list: {students}")

for student in students:
    print(f"Name: {student[0]}, Age: {student[1]}, Subject: {student[2]}")
print()

# Q14. Nested dictionaries
print("Q14. Nested dictionaries")
# 👇 Write your code below:
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
print()

# ======================================
# 🔹 Section 8: Data Structure Conversions
# ======================================

print("🔹 Section 8: Data Structure Conversions")
print("-" * 30)

# Q15. Convert between data structures
print("Q15. Convert between data structures")
# 👇 Write your code below:
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
print()

# ======================================
# 🔹 Section 9: Practical Applications
# ======================================

print("🔹 Section 9: Practical Applications")
print("-" * 30)

# Q16. Prayer tracker
print("Q16. Prayer tracker")
# 👇 Write your code below:
completed_prayers = {"Fajr", "Dhuhr", "Asr"}
all_prayers = {"Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"}

remaining_prayers = all_prayers - completed_prayers
print(f"Completed prayers: {completed_prayers}")
print(f"All prayers: {all_prayers}")
print(f"Remaining prayers: {remaining_prayers}")
print()

# Q17. Grade calculator
print("Q17. Grade calculator")
# 👇 Write your code below:
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
print()

# ======================================
# 🔹 Section 10: Advanced Operations
# ======================================

print("🔹 Section 10: Advanced Operations")
print("-" * 30)

# Q18. List filtering and mapping
print("Q18. List filtering and mapping")
# 👇 Write your code below:
islamic_subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah", "Seerah"]
print(f"All subjects: {islamic_subjects}")

# Filter long subjects
long_subjects = [subject for subject in islamic_subjects if len(subject) > 5]
print(f"Long subjects: {long_subjects}")

# Map to uppercase
uppercase_subjects = [subject.upper() for subject in islamic_subjects]
print(f"Uppercase subjects: {uppercase_subjects}")
print()

# Q19. Dictionary comprehension
print("Q19. Dictionary comprehension")
# 👇 Write your code below:
subjects = ["Quran", "Hadith", "Fiqh"]
grades = [95, 88, 92]

subject_grades = {subject: grade for subject, grade in zip(subjects, grades)}
print(f"Subject grades: {subject_grades}")

# Add letter grades
letter_grades = {subject: "A" if grade >= 90 else "B" if grade >= 80 else "C" 
                for subject, grade in subject_grades.items()}
print(f"Letter grades: {letter_grades}")
print()

# ======================================
# 🔹 Bonus Challenge
# ======================================

print("🔹 Bonus Challenge:")
print("-" * 30)

# Q20. Islamic data management system
print("Q20. Islamic data management system")
# 👇 Write your code below:

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

print()
print("🎉 Congratulations! You've completed the Lists and Data Structures Quiz!")
print("📚 You now understand how to organize and manage Islamic data effectively!") 