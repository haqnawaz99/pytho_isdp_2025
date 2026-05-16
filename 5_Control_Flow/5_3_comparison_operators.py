# 4_3_comparison_operators.py

# ==================================================
# 📝 Control Flow: Comparison Operators
# ==================================================
# 🎯 Learning Objective: Learn ==, !=, >, <, >=, <=
# 📚 Islamic Context: Using Islamic examples to understand comparisons

print("🕌 Welcome to Comparison Operators")
print("=" * 50)

# ======================================
# 🔹 Equal to (==)
# ======================================

print("🔹 Equal to (==) Examples:")
print("-" * 30)

# Islamic example: Checking prayer time
prayer_time = "Fajr"

if prayer_time == "Fajr":
    print("🌅 Time for Fajr prayer")

# Islamic example: Checking student name
student_name = "Ahmed"

if student_name == "Ahmed":
    print("👨 Assalamu Alaikum Ahmed")

print()

# ======================================
# 🔹 Not Equal to (!=)
# ======================================

print("🔹 Not Equal to (!=) Examples:")
print("-" * 30)

# Islamic example: Checking if not a holiday
day = "Monday"

if day != "Friday":
    print("📚 Regular school day")

# Islamic example: Checking if not fasting
is_fasting = False

if is_fasting != True:
    print("🍽️ You can eat - not fasting today")

print()

# ======================================
# 🔹 Greater than (>)
# ======================================

print("🔹 Greater than (>) Examples:")
print("-" * 30)

# Islamic example: Age for learning
student_age = 15

if student_age > 10:
    print("📚 You're old enough to learn Quran")

# Islamic example: Study hours
study_hours = 4

if study_hours > 2:
    print("📖 Excellent study time!")

print()

# ======================================
# 🔹 Less than (<)
# ======================================

print("🔹 Less than (<) Examples:")
print("-" * 30)

# Islamic example: Age for advanced studies
student_age = 8

if student_age < 10:
    print("👶 Focus on basic Islamic education first")

# Islamic example: Prayer time remaining
minutes_until_prayer = 5

if minutes_until_prayer < 10:
    print("⏰ Prepare for prayer - time is near")

print()

# ======================================
# 🔹 Greater than or Equal to (>=)
# ======================================

print("🔹 Greater than or Equal to (>=) Examples:")
print("-" * 30)

# Islamic example: Age for memorization
student_age = 10

if student_age >= 10:
    print("📖 You can start memorizing Quran")

# Islamic example: Exam score
exam_score = 70

if exam_score >= 70:
    print("🎉 You passed the exam!")

print()

# ======================================
# 🔹 Less than or Equal to (<=)
# ======================================

print("🔹 Less than or Equal to (<=) Examples:")
print("-" * 30)

# Islamic example: Young student
student_age = 5

if student_age <= 6:
    print("👶 You're in kindergarten age")

# Islamic example: Basic level
quran_level = 3

if quran_level <= 5:
    print("📚 You're in basic Quran level")

print()

# ======================================
# 🔹 Multiple Comparisons
# ======================================

print("🔹 Multiple Comparisons Examples:")
print("-" * 30)

# Islamic example: Age range for different activities
student_age = 12

if student_age >= 10 and student_age <= 15:
    print("📚 Perfect age for Quran memorization")

# Islamic example: Study time range
study_hours = 3

if study_hours >= 2 and study_hours <= 4:
    print("📖 Good study session length")

print()

# ======================================
# 🔹 Practice with User Input
# ======================================

print("🔹 Practice with User Input:")
print("-" * 30)

# Islamic example: Age check for activities
age_input = input("Enter your age: ")
age = int(age_input)

if age >= 15:
    print("📚 You can study advanced Islamic subjects")
elif age >= 10:
    print("📖 You can start Quran memorization")
else:
    print("👶 Focus on basic Islamic education")

print()

# ======================================
# 🔹 Islamic Quiz Score Example
# ======================================

print("🔹 Islamic Quiz Score Example:")
print("-" * 30)

quiz_score = 85

if quiz_score == 100:
    print("🌟 Perfect score! MashaAllah!")
elif quiz_score >= 90:
    print("🎉 Excellent! Very good understanding")
elif quiz_score >= 80:
    print("✅ Good job! Keep studying")
elif quiz_score >= 70:
    print("📚 Passed! Study a bit more")
else:
    print("💪 Try harder next time")

print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create comparison statements for:")
print("1. Check if student age is between 10-15")
print("2. Check if prayer time is not 'Isha'")
print("3. Check if study hours are more than 1 but less than 5")

# Example solution:
student_age = 12
prayer_time = "Maghrib"
study_hours = 3

if student_age >= 10 and student_age <= 15:
    print("✅ Student is in the right age group")

if prayer_time != "Isha":
    print("✅ It's not Isha prayer time")

if study_hours > 1 and study_hours < 5:
    print("✅ Good study session length")

print()
print("🎉 Congratulations! You've learned comparison operators!") 