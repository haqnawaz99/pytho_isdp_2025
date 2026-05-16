# 4_6_for_loops.py

# ==================================================
# 📝 Control Flow: For Loops
# ==================================================
# 🎯 Learning Objective: Learn for loops for iteration
# 📚 Islamic Context: Using Islamic examples to understand loops

print("🔄 Welcome to For Loops")
print("=" * 50)

# ======================================
# 🔹 Basic For Loop with Range
# ======================================

print("🔹 Basic For Loop with Range:")
print("-" * 30)

# Islamic example: Counting daily prayers
print("🕌 Daily Prayers:")
for prayer in range(1, 6):
    print(f"Prayer {prayer}: Completed")

print()

# Islamic example: Counting from 1 to 10
print("📚 Islamic Counting:")
for number in range(1, 11):
    print(f"Number {number}: Bismillah")

print()

# ======================================
# 🔹 For Loop with Lists
# ======================================

print("🔹 For Loop with Lists:")
print("-" * 30)

# Islamic example: List of prayer times
prayer_times = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

print("🕌 Prayer Times:")
for prayer in prayer_times:
    print(f"Time for {prayer} prayer")

print()

# Islamic example: List of Islamic subjects
subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah", "Seerah"]

print("📚 Islamic Subjects:")
for subject in subjects:
    print(f"Studying {subject}")

print()

# ======================================
# 🔹 For Loop with Strings
# ======================================

print("🔹 For Loop with Strings:")
print("-" * 30)

# Islamic example: Greeting each letter
greeting = "Assalamu Alaikum"

print("🤝 Greeting Letter by Letter:")
for letter in greeting:
    print(f"Letter: {letter}")

print()

# Islamic example: Counting letters in "Allah"
allah_name = "Allah"

print("🕌 Letters in Allah:")
for letter in allah_name:
    print(f"Letter: {letter}")

print()

# ======================================
# 🔹 For Loop with Enumerate
# ======================================

print("🔹 For Loop with Enumerate:")
print("-" * 30)

# Islamic example: Numbered list of good deeds
good_deeds = ["Help parents", "Read Quran", "Say Salam", "Study hard", "Pray on time"]

print("🤝 Good Deeds List:")
for index, deed in enumerate(good_deeds, 1):
    print(f"{index}. {deed}")

print()

# Islamic example: Surah names with numbers
surahs = ["Al-Fatiha", "Al-Baqarah", "Al-Imran", "An-Nisa", "Al-Ma'idah"]

print("📖 First 5 Surahs:")
for number, surah in enumerate(surahs, 1):
    print(f"Surah {number}: {surah}")

print()

# ======================================
# 🔹 For Loop with Range Step
# ======================================

print("🔹 For Loop with Range Step:")
print("-" * 30)

# Islamic example: Counting by 2s (pairs)
print("👥 Counting in Pairs:")
for number in range(2, 11, 2):
    print(f"Pair {number}: Two students")

print()

# Islamic example: Counting by 3s (groups)
print("👨‍👩‍👧‍👦 Counting in Groups:")
for number in range(3, 16, 3):
    print(f"Group {number}: Three students")

print()

# ======================================
# 🔹 For Loop with Conditional Logic
# ======================================

print("🔹 For Loop with Conditional Logic:")
print("-" * 30)

# Islamic example: Checking prayer status
prayer_status = [True, True, False, True, True]

print("🕌 Prayer Status Check:")
for day, prayed in enumerate(prayer_status, 1):
    if prayed:
        print(f"Day {day}: ✅ Prayed")
    else:
        print(f"Day {day}: ❌ Missed prayer")

print()

# Islamic example: Student grades
grades = [85, 92, 78, 95, 88]

print("📚 Student Grades:")
for student, grade in enumerate(grades, 1):
    if grade >= 90:
        print(f"Student {student}: {grade} - 🌟 Excellent!")
    elif grade >= 80:
        print(f"Student {student}: {grade} - ✅ Good!")
    else:
        print(f"Student {student}: {grade} - 💪 Need improvement")

print()

# ======================================
# 🔹 Nested For Loops
# ======================================

print("🔹 Nested For Loops:")
print("-" * 30)

# Islamic example: Weekly prayer schedule
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

print("📅 Weekly Prayer Schedule:")
for day in days:
    print(f"\n{day}:")
    for prayer in prayers:
        print(f"  - {prayer} prayer")

print()

# ======================================
# 🔹 For Loop with Break
# ======================================

print("🔹 For Loop with Break:")
print("-" * 30)

# Islamic example: Finding first missed prayer
prayer_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
missed_prayers = [False, False, True, False, False]

print("🕌 Finding First Missed Prayer:")
for day, missed in zip(prayer_days, missed_prayers):
    if missed:
        print(f"First missed prayer: {day}")
        break
    else:
        print(f"{day}: ✅ All prayers completed")

print()

# ======================================
# 🔹 For Loop with Continue
# ======================================

print("🔹 For Loop with Continue:")
print("-" * 30)

# Islamic example: Skipping non-prayer activities
activities = ["prayer", "study", "prayer", "play", "prayer", "eat", "prayer"]

print("🕌 Prayer Activities Only:")
for activity in activities:
    if activity != "prayer":
        continue
    print(f"✅ {activity.capitalize()} time")

print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create for loops for:")
print("1. Print numbers 1-5 with Islamic messages")
print("2. Loop through a list of Islamic names")
print("3. Count even numbers from 2 to 10")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Numbers with Islamic messages
print("1. Numbers with Islamic Messages:")
for num in range(1, 6):
    print(f"Number {num}: Alhamdulillah")

# 2. Islamic names
print("\n2. Islamic Names:")
names = ["Ahmed", "Fatima", "Ali", "Aisha", "Hassan"]
for name in names:
    print(f"Assalamu Alaikum {name}")

# 3. Even numbers
print("\n3. Even Numbers:")
for num in range(2, 11, 2):
    print(f"Even number: {num}")

print()
print("🎉 Congratulations! You've learned for loops!") 