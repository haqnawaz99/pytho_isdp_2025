# 5_2_functions_with_parameters.py

# ==================================================
# 📝 Functions: Functions with Parameters
# ==================================================
# 🎯 Learning Objective: Learn how to pass data to functions
# 📚 Islamic Context: Using Islamic examples to understand parameters

print("🕌 Welcome to Functions with Parameters")
print("=" * 50)

# ======================================
# 🔹 What are Parameters?
# ======================================

print("🔹 What are Parameters?")
print("-" * 30)
print("Parameters are like ingredients in a recipe.")
print("They allow us to pass data into our functions.")
print("In Islamic terms: Like saying 'Assalamu Alaikum' to different people!")
print()

# ======================================
# 🔹 Example 1: Function with One Parameter
# ======================================

print("🔹 Example 1: Function with One Parameter")
print("-" * 30)

# Define a function to greet someone
def greet_person(name):
    print(f"Assalamu Alaikum {name}")

# Call the function with different names
print("Greeting different people:")
greet_person("Ahmed")
greet_person("Fatima")
greet_person("Ali")
print()

# ======================================
# 🔹 Example 2: Function with String Parameter
# ======================================

print("🔹 Example 2: Function with String Parameter")
print("-" * 30)

# Define a function to show prayer time
def show_prayer_time(prayer):
    print(f"🕌 Time for {prayer} prayer")

# Call the function with different prayers
print("Prayer Times:")
show_prayer_time("Fajr")
show_prayer_time("Dhuhr")
show_prayer_time("Asr")
show_prayer_time("Maghrib")
show_prayer_time("Isha")
print()

# ======================================
# 🔹 Example 3: Function with Number Parameter
# ======================================

print("🔹 Example 3: Function with Number Parameter")
print("-" * 30)

# Define a function to show study progress
def show_study_progress(hours):
    print(f"📚 You studied for {hours} hours")
    if hours >= 3:
        print("🌟 Excellent study session!")
    elif hours >= 2:
        print("✅ Good study time!")
    else:
        print("💪 Try to study more!")

# Call the function with different study hours
print("Study Progress Check:")
show_study_progress(1)
show_study_progress(2)
show_study_progress(4)
print()

# ======================================
# 🔹 Example 4: Function with Multiple Parameters
# ======================================

print("🔹 Example 4: Function with Multiple Parameters")
print("-" * 30)

# Define a function to introduce a student
def introduce_student(name, age, subject):
    print(f"👨 Student Information:")
    print(f"   Name: {name}")
    print(f"   Age: {age}")
    print(f"   Favorite Subject: {subject}")

# Call the function with different students
print("Student Introductions:")
introduce_student("Ahmed", 15, "Quran")
introduce_student("Fatima", 14, "Hadith")
introduce_student("Ali", 16, "Fiqh")
print()

# ======================================
# 🔹 Example 5: Function with Islamic Greeting
# ======================================

print("🔹 Example 5: Function with Islamic Greeting")
print("-" * 30)

# Define a function to greet based on time
def greet_by_time(name, time):
    if time == "morning":
        print(f"🌅 Good morning {name}! Time for Fajr prayer")
    elif time == "afternoon":
        print(f"☀️ Good afternoon {name}! Time for Dhuhr prayer")
    elif time == "evening":
        print(f"🌆 Good evening {name}! Time for Maghrib prayer")
    else:
        print(f"🌙 Good night {name}! Time for Isha prayer")

# Call the function with different times
print("Time-based Greetings:")
greet_by_time("Ahmed", "morning")
greet_by_time("Fatima", "afternoon")
greet_by_time("Ali", "evening")
greet_by_time("Hassan", "night")
print()

# ======================================
# 🔹 Example 6: Function with Grade Check
# ======================================

print("🔹 Example 6: Function with Grade Check")
print("-" * 30)

# Define a function to check student grade
def check_grade(student_name, subject, grade):
    print(f"📊 Grade Report for {student_name}")
    print(f"Subject: {subject}")
    print(f"Grade: {grade}%")
    
    if grade >= 90:
        print("🌟 Excellent! MashaAllah!")
    elif grade >= 80:
        print("✅ Good! Keep it up!")
    elif grade >= 70:
        print("📚 Satisfactory. Study more!")
    else:
        print("💪 Needs improvement. Work harder!")

# Call the function with different grades
print("Grade Reports:")
check_grade("Ahmed", "Quran", 95)
check_grade("Fatima", "Hadith", 85)
check_grade("Ali", "Fiqh", 75)
check_grade("Hassan", "Aqeedah", 65)
print()

# ======================================
# 🔹 Example 7: Function with Prayer Status
# ======================================

print("🔹 Example 7: Function with Prayer Status")
print("-" * 30)

# Define a function to check prayer status
def check_prayer_status(prayer_name, prayed):
    if prayed:
        print(f"✅ {prayer_name} prayer: Completed")
    else:
        print(f"❌ {prayer_name} prayer: Missed")

# Call the function with different prayer statuses
print("Prayer Status Check:")
check_prayer_status("Fajr", True)
check_prayer_status("Dhuhr", True)
check_prayer_status("Asr", False)
check_prayer_status("Maghrib", True)
check_prayer_status("Isha", False)
print()

# ======================================
# 🔹 Example 8: Function with Islamic Activity
# ======================================

print("🔹 Example 8: Function with Islamic Activity")
print("-" * 30)

# Define a function to show Islamic activity
def show_islamic_activity(activity, duration):
    print(f"📖 Islamic Activity: {activity}")
    print(f"⏰ Duration: {duration} minutes")
    
    if duration >= 60:
        print("🌟 Long session - excellent dedication!")
    elif duration >= 30:
        print("✅ Good session - keep it up!")
    else:
        print("💪 Short session - try to spend more time!")

# Call the function with different activities
print("Islamic Activities:")
show_islamic_activity("Quran Reading", 45)
show_islamic_activity("Hadith Study", 90)
show_islamic_activity("Dhikr", 15)
show_islamic_activity("Islamic Discussion", 60)
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create functions with parameters for:")
print("1. A function that takes a name and age")
print("2. A function that takes a subject and grade")
print("3. A function that takes a prayer and time")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Name and age function
def student_info(name, age):
    print(f"👨 Student: {name}")
    print(f"📅 Age: {age}")
    if age >= 15:
        print("📚 Can study advanced subjects")
    else:
        print("📖 Focus on basic Islamic education")

# 2. Subject and grade function
def subject_grade(subject, grade):
    print(f"📚 Subject: {subject}")
    print(f"📊 Grade: {grade}%")
    if grade >= 80:
        print("✅ Good performance!")

# 3. Prayer and time function
def prayer_schedule(prayer, time):
    print(f"🕌 {prayer} prayer at {time}")

# Call the practice functions
print("1. Student Information:")
student_info("Ahmed", 16)
student_info("Fatima", 12)

print("\n2. Subject Grades:")
subject_grade("Quran", 85)
subject_grade("Hadith", 92)

print("\n3. Prayer Schedule:")
prayer_schedule("Fajr", "5:00 AM")
prayer_schedule("Dhuhr", "12:00 PM")

print()
print("🎉 Congratulations! You've learned functions with parameters!")
print("📚 Parameters make functions flexible and reusable!") 