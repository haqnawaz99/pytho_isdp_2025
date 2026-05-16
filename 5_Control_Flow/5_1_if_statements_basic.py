# 4_1_if_statements_basic.py

# ==================================================
# 📝 Control Flow: Basic If Statements
# ==================================================
# 🎯 Learning Objective: Understand how if statements work
# 📚 Islamic Context: Using Islamic examples to learn programming logic

print("🕌 Welcome to Control Flow - If Statements")
print("=" * 50)

# ======================================
# 🔹 Example 1: Simple If Statement
# ======================================

# Islamic example: Checking if someone is a student
is_student = True

if is_student:
    print("✅ You are a student - keep learning!")

print()  # Empty line for readability

# ======================================
# 🔹 Example 2: If with String Comparison
# ======================================

# Islamic example: Greeting based on time
current_time = "morning"

if current_time == "morning":
    print("🌅 Good morning! Time for Fajr prayer")

print()

# ======================================
# 🔹 Example 3: If with Numbers
# ======================================

# Islamic example: Age for learning
student_age = 15

if student_age >= 10:
    print("📚 You are old enough to learn Quran and programming")

print()

# ======================================
# 🔹 Example 4: If with User Input
# ======================================

# Islamic example: Asking about prayer
print("🕌 Prayer Check:")
prayer_status = input("Did you pray today? (yes/no): ")

if prayer_status == "yes":
    print("✅ Alhamdulillah! Keep up the good work")
if prayer_status == "no":
    print("⏰ Don't forget to pray - it's very important")

print()

# ======================================
# 🔹 Example 5: Multiple Conditions
# ======================================

# Islamic example: Checking study habits
study_hours = 3
is_focused = True

if study_hours >= 2:
    print("📖 Good study time!")
if is_focused:
    print("🎯 Excellent focus!")

print()

# ======================================
# 🔹 Example 6: If with Islamic Greeting
# ======================================

# Islamic example: Greeting based on gender
gender = "male"

if gender == "male":
    print("Assalamu Alaikum Brother")
if gender == "female":
    print("Assalamu Alaikum Sister")

print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create variables and if statements for:")
print("1. Check if someone has memorized Quran")
print("2. Check if it's time for prayer")
print("3. Check if student is in madrasah")

# Example solution:
has_quran_memorized = True
prayer_time = "Asr"
is_in_madrasah = True

if has_quran_memorized:
    print("📖 Hafiz/Hafiza - MashaAllah!")

if prayer_time == "Asr":
    print("🕌 Time for Asr prayer")

if is_in_madrasah:
    print("🏫 Student is in madrasah")

print()
print("🎉 Congratulations! You've learned basic if statements!") 