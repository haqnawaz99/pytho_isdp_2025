# 3_4_logical_operators.py

# ==================================================
# 🔀 Operators: Logical Operators
# ==================================================
# 🎯 Learning Objective: Learn and, or, not
# 📚 Madrasa Context: Attendance, homework, fasting, study routine

print("🔀 Welcome to Logical Operators (and / or / not)")
print("=" * 50)

# ----------------------------------
# 1. AND (both conditions must be True)
# ----------------------------------
print("\n1. AND examples:")
has_attended_class = True
has_done_homework = True
print("Attended and homework ->", has_attended_class and has_done_homework)

has_attended_class = True
has_done_homework = False
print("Attended and homework ->", has_attended_class and has_done_homework)

# ----------------------------------
# 2. OR (at least one condition must be True)
# ----------------------------------
print("\n2. OR examples:")
is_reading_quran = True
is_listening_lecture = False
print("Reading or listening ->", is_reading_quran or is_listening_lecture)

is_reading_quran = False
is_listening_lecture = False
print("Reading or listening ->", is_reading_quran or is_listening_lecture)

# ----------------------------------
# 3. NOT (reverses True/False)
# ----------------------------------
print("\n3. NOT examples:")
is_fasting = False
print("not fasting ->", not is_fasting)

is_weekend = True
print("not weekend ->", not is_weekend)

# ----------------------------------
# 4. Combining operators
# ----------------------------------
print("\n4. Combined logic:")
age = 15
has_basic_knowledge = True
is_weekend = False
print("Eligible for advanced class ->", age >= 12 and has_basic_knowledge and not is_weekend)

