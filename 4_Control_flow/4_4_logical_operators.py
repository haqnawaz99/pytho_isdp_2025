# 4_4_logical_operators.py

# ==================================================
# 📝 Control Flow: Logical Operators
# ==================================================
# 🎯 Learning Objective: Learn and, or, not operators
# 📚 Islamic Context: Using Islamic examples to understand logic

print("🕌 Welcome to Logical Operators")
print("=" * 50)

# ======================================
# 🔹 AND Operator (both conditions must be True)
# ======================================

print("🔹 AND Operator Examples:")
print("-" * 30)

# Islamic example: Student requirements
has_attended_class = True
has_done_homework = True

if has_attended_class and has_done_homework:
    print("✅ Perfect student! You attended and did homework")

# Islamic example: Prayer requirements
is_clean = True
is_prayer_time = True

if is_clean and is_prayer_time:
    print("🕌 You can pray now")

print()

# ======================================
# 🔹 OR Operator (at least one condition must be True)
# ======================================

print("🔹 OR Operator Examples:")
print("-" * 30)

# Islamic example: Ways to learn
is_reading_quran = True
is_listening_lecture = False

if is_reading_quran or is_listening_lecture:
    print("📚 You're learning Islamic knowledge")

# Islamic example: Good deeds
has_helped_parents = False
has_helped_friends = True

if has_helped_parents or has_helped_friends:
    print("🤝 MashaAllah! You're helping others")

print()

# ======================================
# 🔹 NOT Operator (reverses True to False and vice versa)
# ======================================

print("🔹 NOT Operator Examples:")
print("-" * 30)

# Islamic example: Checking if not fasting
is_fasting = False

if not is_fasting:
    print("🍽️ You can eat - not fasting today")

# Islamic example: Checking if not weekend
is_weekend = False

if not is_weekend:
    print("📚 Regular school day")

print()

# ======================================
# 🔹 Combining AND, OR, NOT
# ======================================

print("🔹 Combining AND, OR, NOT Examples:")
print("-" * 30)

# Islamic example: Student eligibility for advanced class
age = 15
has_basic_knowledge = True
is_weekend = False

if age >= 12 and has_basic_knowledge and not is_weekend:
    print("📚 You can join the advanced Islamic studies class")

# Islamic example: Prayer conditions
is_clean = True
is_prayer_time = True
is_busy = False

if is_clean and is_prayer_time and not is_busy:
    print("🕌 Perfect time to pray")

print()

# ======================================
# 🔹 Complex Logical Examples
# ======================================

print("🔹 Complex Logical Examples:")
print("-" * 30)

# Islamic example: Student performance evaluation
attendance_good = True
homework_done = True
exam_score = 85
is_helpful = True

if attendance_good and homework_done and (exam_score >= 80 or is_helpful):
    print("🌟 Excellent student! Keep it up")

# Islamic example: Daily routine check
has_prayed = True
has_read_quran = False
has_helped_family = True

if has_prayed and (has_read_quran or has_helped_family):
    print("✅ Good day! You're following Islamic values")

print()

# ======================================
# 🔹 Practice with User Input
# ======================================

print("🔹 Practice with User Input:")
print("-" * 30)

# Islamic example: Student activity check
print("📝 Student Activity Check:")
attended_class = input("Did you attend class today? (yes/no): ") == "yes"
did_homework = input("Did you do homework? (yes/no): ") == "yes"
read_quran = input("Did you read Quran? (yes/no): ") == "yes"

if attended_class and did_homework and read_quran:
    print("🌟 Perfect day! You're an excellent student")
elif attended_class and (did_homework or read_quran):
    print("✅ Good effort! Keep it up")
else:
    print("💪 Try to do better tomorrow")

print()

# ======================================
# 🔹 Islamic Values Check
# ======================================

print("🔹 Islamic Values Check:")
print("-" * 30)

# Islamic example: Checking good character
is_honest = True
is_kind = True
is_respectful = True
is_patient = False

if is_honest and is_kind and is_respectful:
    print("🤝 MashaAllah! You have excellent character")
elif is_honest and (is_kind or is_respectful):
    print("✅ Good character! Work on improving")
else:
    print("💝 Remember to be honest, kind, and respectful")

print()

# ======================================
# 🔹 Study Session Logic
# ======================================

print("🔹 Study Session Logic:")
print("-" * 30)

# Islamic example: Optimal study conditions
is_quiet = True
is_focused = True
is_well_rested = False
has_materials = True

if is_quiet and is_focused and (is_well_rested or has_materials):
    print("📚 Good study conditions! Start learning")
elif not is_quiet:
    print("🔇 Find a quiet place to study")
elif not is_focused:
    print("🎯 Try to focus more on your studies")
else:
    print("💤 Get some rest before studying")

print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create logical statements for:")
print("1. Check if student is eligible for Quran competition")
print("2. Check if it's good time to study")
print("3. Check if student has good Islamic character")

# Example solution:
student_age = 14
has_memorized_surah = True
is_weekend = True
is_quiet_environment = True

is_honest = True
is_kind = True
is_respectful = True

# 1. Quran competition eligibility
if student_age >= 12 and has_memorized_surah:
    print("✅ Eligible for Quran competition")

# 2. Good study time
if is_weekend and is_quiet_environment:
    print("📚 Perfect time for studying")

# 3. Good Islamic character
if is_honest and is_kind and is_respectful:
    print("🤝 Excellent Islamic character")

print()
print("🎉 Congratulations! You've learned logical operators!") 