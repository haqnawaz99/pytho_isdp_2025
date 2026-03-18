# 6_2_list_operations.py

# ==================================================
# 📝 Lists: List Operations
# ==================================================
# 🎯 Learning Objective: Learn advanced list operations and methods
# 📚 Islamic Context: Using Islamic examples to understand list operations

print("🔧 Welcome to List Operations")
print("=" * 50)

# ======================================
# 🔹 What are List Operations?
# ======================================

print("🔹 What are List Operations?")
print("-" * 30)
print("List operations are actions we can perform on lists.")
print("They help us modify, search, and organize our data.")
print("In Islamic terms: Like organizing Islamic books or managing student records!")
print()

# ======================================
# 🔹 Example 1: List Concatenation
# ======================================

print("🔹 Example 1: List Concatenation")
print("-" * 30)

# Combine different Islamic lists
morning_prayers = ["Fajr"]
afternoon_prayers = ["Dhuhr", "Asr"]
evening_prayers = ["Maghrib", "Isha"]

# Concatenate lists
all_prayers = morning_prayers + afternoon_prayers + evening_prayers
print(f"Morning prayers: {morning_prayers}")
print(f"Afternoon prayers: {afternoon_prayers}")
print(f"Evening prayers: {evening_prayers}")
print(f"All prayers combined: {all_prayers}")

# Combine Islamic subjects
basic_subjects = ["Quran", "Hadith"]
advanced_subjects = ["Fiqh", "Aqeedah", "Seerah"]
all_subjects = basic_subjects + advanced_subjects
print(f"\nAll subjects: {all_subjects}")
print()

# ======================================
# 🔹 Example 2: List Repetition
# ======================================

print("🔹 Example 2: List Repetition")
print("-" * 30)

# Repeat Islamic greetings
greeting = ["Assalamu Alaikum"]
repeated_greeting = greeting * 3
print(f"Original greeting: {greeting}")
print(f"Repeated 3 times: {repeated_greeting}")

# Repeat prayer reminder
prayer_reminder = ["Pray on time"]
daily_reminders = prayer_reminder * 5
print(f"\nPrayer reminder: {prayer_reminder}")
print(f"Daily reminders: {daily_reminders}")
print()

# ======================================
# 🔹 Example 3: List Sorting
# ======================================

print("🔹 Example 3: List Sorting")
print("-" * 30)

# Sort Islamic names alphabetically
islamic_names = ["Fatima", "Ahmed", "Zainab", "Ali", "Bilal"]
print(f"Original names: {islamic_names}")

# Sort in ascending order
islamic_names.sort()
print(f"Sorted names (A-Z): {islamic_names}")

# Sort in descending order
islamic_names.sort(reverse=True)
print(f"Sorted names (Z-A): {islamic_names}")

# Sort grades
grades = [85, 92, 78, 95, 88]
print(f"\nOriginal grades: {grades}")
grades.sort()
print(f"Sorted grades (low to high): {grades}")
grades.sort(reverse=True)
print(f"Sorted grades (high to low): {grades}")
print()

# ======================================
# 🔹 Example 4: List Copying
# ======================================

print("🔹 Example 4: List Copying")
print("-" * 30)

# Original Islamic activities list
original_activities = ["Prayer", "Quran Reading", "Dhikr"]
print(f"Original activities: {original_activities}")

# Shallow copy
copied_activities = original_activities.copy()
print(f"Copied activities: {copied_activities}")

# Modify the copy
copied_activities.append("Helping Others")
print(f"After adding to copy: {copied_activities}")
print(f"Original unchanged: {original_activities}")

# List slicing for copying
slice_copy = original_activities[:]
print(f"Slice copy: {slice_copy}")
print()

# ======================================
# 🔹 Example 5: List Comprehension
# ======================================

print("🔹 Example 5: List Comprehension")
print("-" * 30)

# Create list of Islamic greetings with names
names = ["Ahmed", "Fatima", "Ali"]
greetings = [f"Assalamu Alaikum {name}" for name in names]
print(f"Names: {names}")
print(f"Personalized greetings: {greetings}")

# Create list of prayer times with labels
prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
times = ["5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM"]
prayer_schedule = [f"{prayer}: {time}" for prayer, time in zip(prayers, times)]
print(f"\nPrayer schedule: {prayer_schedule}")

# Filter high grades
all_grades = [85, 92, 78, 95, 88, 70, 96]
high_grades = [grade for grade in all_grades if grade >= 90]
print(f"\nAll grades: {all_grades}")
print(f"High grades (90+): {high_grades}")
print()

# ======================================
# 🔹 Example 6: List Filtering
# ======================================

print("🔹 Example 6: List Filtering")
print("-" * 30)

# Filter Islamic subjects by length
subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah", "Seerah", "Tafsir"]
short_subjects = [subject for subject in subjects if len(subject) <= 5]
long_subjects = [subject for subject in subjects if len(subject) > 5]

print(f"All subjects: {subjects}")
print(f"Short subjects (≤5 letters): {short_subjects}")
print(f"Long subjects (>5 letters): {long_subjects}")

# Filter students by age
students = [["Ahmed", 15], ["Fatima", 14], ["Ali", 16], ["Aisha", 13]]
older_students = [student for student in students if student[1] >= 15]
print(f"\nAll students: {students}")
print(f"Students 15 and older: {older_students}")
print()

# ======================================
# 🔹 Example 7: List Mapping
# ======================================

print("🔹 Example 7: List Mapping")
print("-" * 30)

# Convert prayer names to uppercase
prayers = ["fajr", "dhuhr", "asr", "maghrib", "isha"]
uppercase_prayers = [prayer.upper() for prayer in prayers]
print(f"Original prayers: {prayers}")
print(f"Uppercase prayers: {uppercase_prayers}")

# Add "Al-" prefix to Islamic names
names = ["Fatima", "Ali", "Hassan", "Aisha"]
prefixed_names = [f"Al-{name}" for name in names]
print(f"\nOriginal names: {names}")
print(f"Names with 'Al-' prefix: {prefixed_names}")

# Calculate prayer percentages
prayers_completed = [4, 5, 3, 5, 4, 5, 5]
total_prayers = 5
percentages = [(completed/total_prayers)*100 for completed in prayers_completed]
print(f"\nPrayers completed this week: {prayers_completed}")
print(f"Completion percentages: {percentages}")
print()

# ======================================
# 🔹 Example 8: List Aggregation
# ======================================

print("🔹 Example 8: List Aggregation")
print("-" * 30)

# Calculate statistics for Islamic grades
quran_grades = [85, 92, 78, 95, 88, 90, 87]
print(f"Quran grades: {quran_grades}")

# Basic statistics
total = sum(quran_grades)
count = len(quran_grades)
average = total / count
highest = max(quran_grades)
lowest = min(quran_grades)

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# Count prayer completions
weekly_prayers = [5, 5, 4, 5, 3, 5, 5]
perfect_days = sum(1 for prayers in weekly_prayers if prayers == 5)
print(f"\nWeekly prayers: {weekly_prayers}")
print(f"Perfect prayer days: {perfect_days}")
print(f"Perfect days percentage: {(perfect_days/len(weekly_prayers))*100:.1f}%")
print()

# ======================================
# 🔹 Example 9: List Searching
# ======================================

print("🔹 Example 9: List Searching")
print("-" * 30)

# Search for Islamic books
books = ["Quran", "Sahih Bukhari", "Sahih Muslim", "Abu Dawud", "Tirmidhi"]
print(f"Available books: {books}")

# Check if book exists
search_book = "Quran"
if search_book in books:
    print(f"'{search_book}' is available")
    print(f"Position: {books.index(search_book)}")
else:
    print(f"'{search_book}' is not available")

# Search for high grades
grades = [85, 92, 78, 95, 88, 70, 96]
excellent_grades = [grade for grade in grades if grade >= 95]
print(f"\nAll grades: {grades}")
print(f"Excellent grades (95+): {excellent_grades}")
print(f"Number of excellent grades: {len(excellent_grades)}")
print()

# ======================================
# 🔹 Example 10: List Transformation
# ======================================

print("🔹 Example 10: List Transformation")
print("-" * 30)

# Transform student data
students = [["ahmed", 15, "quran"], ["fatima", 14, "hadith"]]
print(f"Original student data: {students}")

# Transform to proper case and add titles
transformed_students = []
for student in students:
    name = student[0].title()
    age = student[1]
    subject = student[2].title()
    transformed_students.append([name, age, subject])

print(f"Transformed student data: {transformed_students}")

# Transform prayer times to 24-hour format
prayer_times_12h = ["5:00 AM", "12:00 PM", "3:00 PM", "6:00 PM", "8:00 PM"]
prayer_times_24h = []

for time in prayer_times_12h:
    if "PM" in time and "12" not in time:
        # Convert PM times (except 12 PM)
        hour = int(time.split(":")[0]) + 12
        minute = time.split(":")[1].split(" ")[0]
        prayer_times_24h.append(f"{hour}:{minute}")
    elif "AM" in time and "12" not in time:
        # Keep AM times (except 12 AM)
        prayer_times_24h.append(time.replace(" AM", ""))
    else:
        # Handle 12 PM and 12 AM
        if "12:00 PM" in time:
            prayer_times_24h.append("12:00")
        else:
            prayer_times_24h.append("00:00")

print(f"\n12-hour format: {prayer_times_12h}")
print(f"24-hour format: {prayer_times_24h}")
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Perform these operations on lists:")
print("1. Create a list of Islamic names and sort them")
print("2. Filter grades above 80 from a list")
print("3. Add 'Al-' prefix to a list of names")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Sort Islamic names
names = ["Fatima", "Ahmed", "Zainab", "Ali"]
print(f"1. Original names: {names}")
names.sort()
print(f"   Sorted names: {names}")

# 2. Filter high grades
grades = [85, 92, 78, 95, 88, 70]
print(f"\n2. All grades: {grades}")
high_grades = [grade for grade in grades if grade > 80]
print(f"   Grades above 80: {high_grades}")

# 3. Add prefix to names
original_names = ["Fatima", "Ali", "Hassan"]
prefixed_names = [f"Al-{name}" for name in original_names]
print(f"\n3. Original names: {original_names}")
print(f"   Names with prefix: {prefixed_names}")

print()
print("🎉 Congratulations! You've learned list operations!")
print("📚 List operations help you manipulate and organize data effectively!") 