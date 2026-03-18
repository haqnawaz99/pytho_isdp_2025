# 5_4_default_parameters.py

# ==================================================
# 📝 Functions: Default Parameters
# ==================================================
# 🎯 Learning Objective: Learn how to set default values for parameters
# 📚 Islamic Context: Using Islamic examples to understand default parameters

print("⚙️ Welcome to Default Parameters")
print("=" * 50)

# ======================================
# 🔹 What are Default Parameters?
# ======================================

print("🔹 What are Default Parameters?")
print("-" * 30)
print("Default parameters have pre-set values if none are provided.")
print("They make functions more flexible and easier to use.")
print("In Islamic terms: Like having a default greeting even if you don't know someone's name!")
print()

# ======================================
# 🔹 Example 1: Simple Default Parameter
# ======================================

print("🔹 Example 1: Simple Default Parameter")
print("-" * 30)

# Define a function with default greeting
def greet_person(name="Brother/Sister"):
    print(f"Assalamu Alaikum {name}")

# Call with parameter
greet_person("Ahmed")

# Call without parameter (uses default)
greet_person()
print()

# ======================================
# 🔹 Example 2: Default Prayer Time
# ======================================

print("🔹 Example 2: Default Prayer Time")
print("-" * 30)

# Define a function with default prayer
def show_prayer_info(prayer="Fajr"):
    print(f"🕌 {prayer} prayer is important")
    if prayer == "Fajr":
        print("   🌅 Early morning prayer")
    elif prayer == "Dhuhr":
        print("   ☀️ Noon prayer")
    elif prayer == "Asr":
        print("   🌤️ Afternoon prayer")
    elif prayer == "Maghrib":
        print("   🌆 Sunset prayer")
    elif prayer == "Isha":
        print("   🌙 Night prayer")

# Call with specific prayer
show_prayer_info("Dhuhr")

# Call without parameter (uses default)
show_prayer_info()
print()

# ======================================
# 🔹 Example 3: Default Study Time
# ======================================

print("🔹 Example 3: Default Study Time")
print("-" * 30)

# Define a function with default study time
def study_reminder(subject="Quran", hours=2):
    print(f"📚 Study reminder for {subject}")
    print(f"⏰ Recommended time: {hours} hours")
    
    if hours >= 3:
        print("🌟 Excellent study plan!")
    elif hours >= 2:
        print("✅ Good study time!")
    else:
        print("💪 Try to study more!")

# Call with both parameters
study_reminder("Hadith", 3)

# Call with only subject (uses default hours)
study_reminder("Fiqh")

# Call without parameters (uses both defaults)
study_reminder()
print()

# ======================================
# 🔹 Example 4: Default Grade Threshold
# ======================================

print("🔹 Example 4: Default Grade Threshold")
print("-" * 30)

# Define a function with default passing grade
def check_exam_result(grade, passing_grade=70):
    print(f"📊 Exam Result: {grade}%")
    print(f"📈 Passing Grade: {passing_grade}%")
    
    if grade >= passing_grade:
        print("✅ Passed! MashaAllah!")
    else:
        print("❌ Failed. Study harder!")

# Call with both parameters
check_exam_result(85, 80)

# Call with only grade (uses default passing grade)
check_exam_result(75)
print()

# ======================================
# 🔹 Example 5: Default Islamic Message
# ======================================

print("🔹 Example 5: Default Islamic Message")
print("-" * 30)

# Define a function with default message
def show_islamic_message(message="Seek knowledge from cradle to grave"):
    print(f"📖 Islamic Wisdom: {message}")
    print("💡 Remember this in your daily life")

# Call with custom message
show_islamic_message("Prayer is the key to paradise")

# Call without parameter (uses default)
show_islamic_message()
print()

# ======================================
# 🔹 Example 6: Default Student Info
# ======================================

print("🔹 Example 6: Default Student Info")
print("-" * 30)

# Define a function with multiple default parameters
def student_profile(name="Student", age=15, subject="Quran"):
    print(f"👨 Student Profile:")
    print(f"   Name: {name}")
    print(f"   Age: {age}")
    print(f"   Favorite Subject: {subject}")
    
    if age >= 15:
        print("   📚 Can study advanced topics")
    else:
        print("   📖 Focus on basic education")

# Call with all parameters
student_profile("Ahmed", 16, "Hadith")

# Call with some parameters
student_profile("Fatima", 14)

# Call without parameters (uses all defaults)
student_profile()
print()

# ======================================
# 🔹 Example 7: Default Prayer Status
# ======================================

print("🔹 Example 7: Default Prayer Status")
print("-" * 30)

# Define a function with default prayer status
def prayer_report(prayer="Fajr", completed=True):
    status = "✅ Completed" if completed else "❌ Missed"
    print(f"🕌 {prayer} prayer: {status}")
    
    if completed:
        print("   🌟 Keep up the good work!")
    else:
        print("   💪 Don't miss the next prayer!")

# Call with both parameters
prayer_report("Dhuhr", False)

# Call with only prayer (uses default completed status)
prayer_report("Asr")

# Call without parameters (uses both defaults)
prayer_report()
print()

# ======================================
# 🔹 Example 8: Default Study Session
# ======================================

print("🔹 Example 8: Default Study Session")
print("-" * 30)

# Define a function with default study session
def study_session(subject="Quran", duration=60, focused=True):
    print(f"📚 Study Session Report:")
    print(f"   Subject: {subject}")
    print(f"   Duration: {duration} minutes")
    print(f"   Focused: {'Yes' if focused else 'No'}")
    
    if duration >= 60 and focused:
        print("   🌟 Excellent study session!")
    elif duration >= 30:
        print("   ✅ Good study time!")
    else:
        print("   💪 Try to study longer and stay focused!")

# Call with all parameters
study_session("Hadith", 90, True)

# Call with some parameters
study_session("Fiqh", 45)

# Call without parameters (uses all defaults)
study_session()
print()

# ======================================
# 🔹 Example 9: Default Islamic Greeting
# ======================================

print("🔹 Example 9: Default Islamic Greeting")
print("-" * 30)

# Define a function with default greeting
def islamic_greeting(name="Brother/Sister", time="day"):
    if time == "morning":
        greeting = "🌅 Good morning"
    elif time == "afternoon":
        greeting = "☀️ Good afternoon"
    elif time == "evening":
        greeting = "🌆 Good evening"
    else:
        greeting = "🤝 Assalamu Alaikum"
    
    print(f"{greeting} {name}!")

# Call with both parameters
islamic_greeting("Ahmed", "morning")

# Call with only name (uses default time)
islamic_greeting("Fatima")

# Call without parameters (uses both defaults)
islamic_greeting()
print()

# ======================================
# 🔹 Example 10: Default Grade Calculation
# ======================================

print("🔹 Example 10: Default Grade Calculation")
print("-" * 30)

# Define a function with default grade weights
def calculate_final_grade(quran_grade, hadith_grade, fiqh_grade, 
                         quran_weight=0.4, hadith_weight=0.3, fiqh_weight=0.3):
    final_grade = (quran_grade * quran_weight + 
                   hadith_grade * hadith_weight + 
                   fiqh_grade * fiqh_weight)
    
    print(f"📊 Final Grade Calculation:")
    print(f"   Quran ({quran_weight*100}%): {quran_grade}%")
    print(f"   Hadith ({hadith_weight*100}%): {hadith_grade}%")
    print(f"   Fiqh ({fiqh_weight*100}%): {fiqh_grade}%")
    print(f"   Final Grade: {final_grade:.1f}%")
    
    return final_grade

# Call with custom weights
final1 = calculate_final_grade(85, 90, 88, 0.5, 0.3, 0.2)

# Call with default weights
final2 = calculate_final_grade(92, 85, 90)
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create functions with default parameters for:")
print("1. A function with default name and age")
print("2. A function with default prayer and time")
print("3. A function with default subject and grade")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Default name and age function
def student_info(name="Student", age=15):
    print(f"👨 {name}, Age: {age}")
    if age >= 15:
        print("📚 Advanced level student")

# 2. Default prayer and time function
def prayer_info(prayer="Fajr", time="5:00 AM"):
    print(f"🕌 {prayer} at {time}")

# 3. Default subject and grade function
def subject_report(subject="Quran", grade=80):
    print(f"📚 {subject}: {grade}%")
    if grade >= 80:
        print("✅ Good performance!")

# Use the practice functions
print("1. Student Information:")
student_info("Ahmed", 16)
student_info("Fatima")
student_info()

print("\n2. Prayer Information:")
prayer_info("Dhuhr", "12:00 PM")
prayer_info("Asr")
prayer_info()

print("\n3. Subject Reports:")
subject_report("Hadith", 95)
subject_report("Fiqh")
subject_report()

print()
print("🎉 Congratulations! You've learned default parameters!")
print("📚 Default parameters make functions more flexible and user-friendly!") 