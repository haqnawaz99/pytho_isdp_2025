# 4_2_if_else_statements.py

# ==================================================
# 📝 Control Flow: If-Else Statements
# ==================================================
# 🎯 Learning Objective: Understand if-else logic
# 📚 Islamic Context: Making decisions based on conditions

print("🕌 Welcome to If-Else Statements")
print("=" * 50)

# ======================================
# 🔹 Example 1: Basic If-Else
# ======================================

# Islamic example: Checking prayer status
has_prayed = True

if has_prayed:
    print("✅ Alhamdulillah! You prayed")
else:
    print("⏰ Please pray - it's very important")

print()

# ======================================
# 🔹 Example 2: If-Else with Numbers
# ======================================

# Islamic example: Age for learning Quran
student_age = 12

if student_age >= 10:
    print("📚 You can start memorizing Quran")
else:
    print("👶 You're still young, focus on basic learning")

print()

# ======================================
# 🔹 Example 3: If-Else with User Input
# ======================================

# Islamic example: Asking about Quran reading
print("📖 Quran Reading Check:")
quran_read = input("Did you read Quran today? (yes/no): ")

if quran_read == "yes":
    print("✅ MashaAllah! Keep reading daily")
else:
    print("📖 Try to read at least one page today")

print()

# ======================================
# 🔹 Example 4: If-Else with String Comparison
# ======================================

# Islamic example: Greeting based on time
current_time = "evening"

if current_time == "morning":
    print("🌅 Good morning! Time for Fajr")
elif current_time == "afternoon":
    print("☀️ Good afternoon! Time for Dhuhr")
elif current_time == "evening":
    print("🌆 Good evening! Time for Maghrib")
else:
    print("🌙 Good night! Time for Isha")

print()

# ======================================
# 🔹 Example 5: If-Else with Study Habits
# ======================================

# Islamic example: Checking study progress
study_hours = 2
is_focused = True

if study_hours >= 3 and is_focused:
    print("🌟 Excellent! You're a dedicated student")
elif study_hours >= 2:
    print("📚 Good effort! Keep it up")
else:
    print("💪 Try to study more - knowledge is power")

print()

# ======================================
# 🔹 Example 6: If-Else with Islamic Values
# ======================================

# Islamic example: Checking good deeds
has_helped_someone = True
has_said_salam = True

if has_helped_someone and has_said_salam:
    print("🤝 MashaAllah! You're following Islamic values")
else:
    print("💝 Remember to help others and greet with Salam")

print()

# ======================================
# 🔹 Example 7: If-Else with Madrasah Subjects
# ======================================

# Islamic example: Subject preference
favorite_subject = "Quran"

if favorite_subject == "Quran":
    print("📖 Quran is the best subject!")
elif favorite_subject == "Hadith":
    print("📚 Hadith teaches us the Prophet's way")
elif favorite_subject == "Fiqh":
    print("⚖️ Fiqh helps us understand Islamic law")
else:
    print("📚 All Islamic subjects are important")

print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create if-else statements for:")
print("1. Check if student passed exam (score >= 70)")
print("2. Check if it's weekend or weekday")
print("3. Check if student is Hafiz/Hafiza")

# Example solution:
exam_score = 85
day_of_week = "Friday"
is_hafiz = False

if exam_score >= 70:
    print("🎉 Congratulations! You passed the exam")
else:
    print("📚 Study harder for the next exam")

if day_of_week == "Friday":
    print("🕌 Jummah Mubarak!")
else:
    print("📅 Regular school day")

if is_hafiz:
    print("📖 MashaAllah! You're a Hafiz/Hafiza")
else:
    print("📚 Keep working towards memorizing Quran")

print()
print("🎉 Congratulations! You've learned if-else statements!") 