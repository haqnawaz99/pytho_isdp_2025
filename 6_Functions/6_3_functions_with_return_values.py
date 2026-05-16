# 5_3_functions_with_return_values.py

# ==================================================
# 📝 Functions: Functions with Return Values
# ==================================================
# 🎯 Learning Objective: Learn how functions can return data
# 📚 Islamic Context: Using Islamic examples to understand return values

print("🔄 Welcome to Functions with Return Values")
print("=" * 50)

# ======================================
# 🔹 What are Return Values?
# ======================================

print("🔹 What are Return Values?")
print("-" * 30)
print("Return values are like answers from a function.")
print("Functions can give us back data that we can use.")
print("In Islamic terms: Like asking for a dua and getting a blessing back!")
print()

# ======================================
# 🔹 Example 1: Simple Return Value
# ======================================

print("🔹 Example 1: Simple Return Value")
print("-" * 30)

# Define a function that returns an Islamic greeting
def get_islamic_greeting():
    return "Assalamu Alaikum"

# Use the returned value
greeting = get_islamic_greeting()
print(f"Greeting: {greeting}")

# Use the function directly in print
print(f"Direct greeting: {get_islamic_greeting()}")
print()

# ======================================
# 🔹 Example 2: Return Value with Parameter
# ======================================

print("🔹 Example 2: Return Value with Parameter")
print("-" * 30)

# Define a function that returns a personalized greeting
def get_personalized_greeting(name):
    return f"Assalamu Alaikum {name}"

# Use the returned value
student_greeting = get_personalized_greeting("Ahmed")
print(student_greeting)

teacher_greeting = get_personalized_greeting("Maulana")
print(teacher_greeting)
print()

# ======================================
# 🔹 Example 3: Return Number Value
# ======================================

print("🔹 Example 3: Return Number Value")
print("-" * 30)

# Define a function that calculates prayer count
def calculate_prayer_count(prayed_fajr, prayed_dhuhr, prayed_asr, prayed_maghrib, prayed_isha):
    total_prayers = prayed_fajr + prayed_dhuhr + prayed_asr + prayed_maghrib + prayed_isha
    return total_prayers

# Use the function
today_prayers = calculate_prayer_count(True, True, False, True, True)
print(f"Prayers completed today: {today_prayers}/5")

# Convert boolean to number (True=1, False=0)
today_prayers = calculate_prayer_count(1, 1, 0, 1, 1)
print(f"Prayers completed today: {today_prayers}/5")
print()

# ======================================
# 🔹 Example 4: Return Grade Status
# ======================================

print("🔹 Example 4: Return Grade Status")
print("-" * 30)

# Define a function that returns grade status
def get_grade_status(grade):
    if grade >= 90:
        return "Excellent"
    elif grade >= 80:
        return "Good"
    elif grade >= 70:
        return "Satisfactory"
    else:
        return "Needs Improvement"

# Use the function
ahmed_grade = get_grade_status(95)
print(f"Ahmed's grade status: {ahmed_grade}")

fatima_grade = get_grade_status(85)
print(f"Fatima's grade status: {fatima_grade}")

ali_grade = get_grade_status(75)
print(f"Ali's grade status: {ali_grade}")
print()

# ======================================
# 🔹 Example 5: Return Prayer Time
# ======================================

print("🔹 Example 5: Return Prayer Time")
print("-" * 30)

# Define a function that returns prayer time
def get_prayer_time(prayer):
    prayer_times = {
        "Fajr": "5:00 AM",
        "Dhuhr": "12:00 PM",
        "Asr": "3:00 PM",
        "Maghrib": "6:00 PM",
        "Isha": "8:00 PM"
    }
    return prayer_times.get(prayer, "Time not found")

# Use the function
fajr_time = get_prayer_time("Fajr")
print(f"Fajr prayer time: {fajr_time}")

dhuhr_time = get_prayer_time("Dhuhr")
print(f"Dhuhr prayer time: {dhuhr_time}")

unknown_time = get_prayer_time("Unknown")
print(f"Unknown prayer: {unknown_time}")
print()

# ======================================
# 🔹 Example 6: Return Study Recommendation
# ======================================

print("🔹 Example 6: Return Study Recommendation")
print("-" * 30)

# Define a function that returns study recommendation
def get_study_recommendation(hours_studied):
    if hours_studied >= 4:
        return "🌟 Excellent! You're a dedicated student!"
    elif hours_studied >= 2:
        return "✅ Good effort! Keep it up!"
    elif hours_studied >= 1:
        return "📚 Decent study time. Try to study more!"
    else:
        return "💪 Need to study more! Knowledge is power!"

# Use the function
recommendation1 = get_study_recommendation(5)
print(f"5 hours study: {recommendation1}")

recommendation2 = get_study_recommendation(2)
print(f"2 hours study: {recommendation2}")

recommendation3 = get_study_recommendation(0)
print(f"0 hours study: {recommendation3}")
print()

# ======================================
# 🔹 Example 7: Return Islamic Subject Info
# ======================================

print("🔹 Example 7: Return Islamic Subject Info")
print("-" * 30)

# Define a function that returns subject information
def get_subject_info(subject):
    subject_info = {
        "Quran": "The Holy Book of Allah",
        "Hadith": "Sayings and actions of Prophet Muhammad (PBUH)",
        "Fiqh": "Islamic jurisprudence and law",
        "Aqeedah": "Islamic beliefs and theology",
        "Seerah": "Life and biography of Prophet Muhammad (PBUH)"
    }
    return subject_info.get(subject, "Subject not found")

# Use the function
quran_info = get_subject_info("Quran")
print(f"Quran: {quran_info}")

hadith_info = get_subject_info("Hadith")
print(f"Hadith: {hadith_info}")

unknown_info = get_subject_info("Unknown")
print(f"Unknown: {unknown_info}")
print()

# ======================================
# 🔹 Example 8: Return Multiple Values
# ======================================

print("🔹 Example 8: Return Multiple Values")
print("-" * 30)

# Define a function that returns multiple values
def get_student_info(name, age, grade):
    status = "Senior" if age >= 15 else "Junior"
    performance = "Excellent" if grade >= 90 else "Good" if grade >= 80 else "Average"
    return name, age, status, performance

# Use the function
student_name, student_age, student_status, student_performance = get_student_info("Ahmed", 16, 95)
print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"Status: {student_status}")
print(f"Performance: {student_performance}")
print()

# ======================================
# 🔹 Example 9: Return with Calculations
# ======================================

print("🔹 Example 9: Return with Calculations")
print("-" * 30)

# Define a function that calculates average grade
def calculate_average_grade(grades):
    if len(grades) == 0:
        return 0
    total = sum(grades)
    average = total / len(grades)
    return round(average, 2)

# Use the function
ahmed_grades = [85, 92, 78, 95, 88]
ahmed_average = calculate_average_grade(ahmed_grades)
print(f"Ahmed's average grade: {ahmed_average}%")

fatima_grades = [90, 95, 88, 92, 89]
fatima_average = calculate_average_grade(fatima_grades)
print(f"Fatima's average grade: {fatima_average}%")
print()

# ======================================
# 🔹 Example 10: Return Boolean Value
# ======================================

print("🔹 Example 10: Return Boolean Value")
print("-" * 30)

# Define a function that checks if student passed
def has_passed_exam(grade):
    return grade >= 70

# Define a function that checks if prayer time
def is_prayer_time(current_hour):
    prayer_hours = [5, 12, 15, 18, 20]
    return current_hour in prayer_hours

# Use the functions
exam_result = has_passed_exam(85)
print(f"Student passed exam: {exam_result}")

prayer_check = is_prayer_time(12)
print(f"Is prayer time at 12: {prayer_check}")

prayer_check2 = is_prayer_time(10)
print(f"Is prayer time at 10: {prayer_check2}")
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create functions with return values for:")
print("1. A function that returns 'MashaAllah' for good grades")
print("2. A function that returns prayer status (True/False)")
print("3. A function that returns student level based on age")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. MashaAllah function
def get_grade_message(grade):
    if grade >= 90:
        return "MashaAllah! Excellent!"
    elif grade >= 80:
        return "MashaAllah! Good job!"
    else:
        return "Keep trying!"

# 2. Prayer status function
def check_prayer_completed(prayed):
    return prayed

# 3. Student level function
def get_student_level(age):
    if age >= 15:
        return "Advanced"
    elif age >= 12:
        return "Intermediate"
    else:
        return "Beginner"

# Use the practice functions
message1 = get_grade_message(95)
print(f"Grade message: {message1}")

prayer_status = check_prayer_completed(True)
print(f"Prayer completed: {prayer_status}")

student_level = get_student_level(14)
print(f"Student level: {student_level}")

print()
print("🎉 Congratulations! You've learned functions with return values!")
print("📚 Return values make functions more useful and powerful!") 