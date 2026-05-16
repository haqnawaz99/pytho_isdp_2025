# 5_7_functions_solutions.py

# ==================================================
# 📝 Functions: Quiz Solutions
# ==================================================
# 🎯 Learning Objective: Check your answers
# 📚 Islamic Context: Complete solutions with explanations

print("📝 Functions Quiz Solutions")
print("=" * 50)
print("📌 These are the complete solutions.")
print("Compare with your answers to learn.")
print()

# ======================================
# 🔹 Section 1: Basic Functions - Solutions
# ======================================

print("🔹 Section 1: Basic Functions - Solutions")
print("-" * 40)

# Q1. Create a function that prints "Assalamu Alaikum" - Solution
print("Q1. Create a function that prints 'Assalamu Alaikum' - Solution:")
def say_salam():
    print("Assalamu Alaikum")

say_salam()
print("Explanation: Simple function with no parameters that prints a greeting")
print()

# Q2. Create a function that lists 3 Islamic subjects - Solution
print("Q2. Create a function that lists 3 Islamic subjects - Solution:")
def list_subjects():
    print("📚 Islamic Subjects:")
    print("1. Quran")
    print("2. Hadith")
    print("3. Fiqh")

list_subjects()
print("Explanation: Function that prints multiple lines of Islamic subjects")
print()

# ======================================
# 🔹 Section 2: Functions with Parameters - Solutions
# ======================================

print("🔹 Section 2: Functions with Parameters - Solutions")
print("-" * 40)

# Q3. Create a function that takes a name and greets the person - Solution
print("Q3. Create a function that takes a name and greets the person - Solution:")
def greet_person(name):
    print(f"Assalamu Alaikum {name}")

greet_person("Ahmed")
greet_person("Fatima")
print("Explanation: Function with one parameter that personalizes the greeting")
print()

# Q4. Create a function that takes prayer name and shows its time - Solution
print("Q4. Create a function that takes prayer name and shows its time - Solution:")
def show_prayer_time(prayer):
    if prayer == "Fajr":
        print(f"🕌 {prayer} prayer: 5:00 AM")
    elif prayer == "Dhuhr":
        print(f"🕌 {prayer} prayer: 12:00 PM")
    elif prayer == "Asr":
        print(f"🕌 {prayer} prayer: 3:00 PM")
    else:
        print(f"🕌 {prayer} prayer time")

show_prayer_time("Fajr")
show_prayer_time("Dhuhr")
print("Explanation: Function with conditional logic based on the prayer parameter")
print()

# ======================================
# 🔹 Section 3: Functions with Return Values - Solutions
# ======================================

print("🔹 Section 3: Functions with Return Values - Solutions")
print("-" * 40)

# Q5. Create a function that returns "MashaAllah" for good grades - Solution
print("Q5. Create a function that returns 'MashaAllah' for good grades - Solution:")
def get_grade_message(grade):
    if grade >= 90:
        return "MashaAllah! Excellent!"
    elif grade >= 80:
        return "MashaAllah! Good job!"
    else:
        return "Keep trying!"

message1 = get_grade_message(95)
print(f"Grade 95: {message1}")

message2 = get_grade_message(85)
print(f"Grade 85: {message2}")
print("Explanation: Function returns different messages based on grade thresholds")
print()

# Q6. Create a function that returns prayer count - Solution
print("Q6. Create a function that returns prayer count - Solution:")
def count_prayers(prayed_fajr, prayed_dhuhr, prayed_asr, prayed_maghrib, prayed_isha):
    total = prayed_fajr + prayed_dhuhr + prayed_asr + prayed_maghrib + prayed_isha
    return total

prayers_today = count_prayers(1, 1, 0, 1, 1)
print(f"Prayers completed today: {prayers_today}/5")
print("Explanation: Function takes multiple parameters and returns their sum")
print()

# ======================================
# 🔹 Section 4: Default Parameters - Solutions
# ======================================

print("🔹 Section 4: Default Parameters - Solutions")
print("-" * 40)

# Q7. Create a function with default name parameter - Solution
print("Q7. Create a function with default name parameter - Solution:")
def greet_with_default(name="Brother/Sister"):
    print(f"Assalamu Alaikum {name}")

greet_with_default("Ahmed")
greet_with_default()
print("Explanation: Function with default parameter value that can be overridden")
print()

# Q8. Create a function with default study time - Solution
print("Q8. Create a function with default study time - Solution:")
def study_reminder(subject="Quran", hours=2):
    print(f"📚 Study {subject} for {hours} hours")
    if hours >= 3:
        print("🌟 Excellent study plan!")

study_reminder("Hadith", 3)
study_reminder("Fiqh")
study_reminder()
print("Explanation: Function with multiple default parameters")
print()

# ======================================
# 🔹 Section 5: String Methods - Solutions
# ======================================

print("🔹 Section 5: String Methods - Solutions")
print("-" * 40)

# Q9. Use string methods to format Islamic text - Solution
print("Q9. Use string methods to format Islamic text - Solution:")
islamic_text = "  assalamu alaikum  "
print(f"Original: '{islamic_text}'")

cleaned_text = islamic_text.strip().title()
print(f"Cleaned: '{cleaned_text}'")
print("Explanation: Using strip() to remove spaces and title() to capitalize words")
print()

# Q10. Use string methods to process names - Solution
print("Q10. Use string methods to process names - Solution:")
names = "ahmed,fatima,ali"
print(f"Original: {names}")

name_list = names.split(",")
formatted_names = []
for name in name_list:
    formatted_names.append(name.strip().title())

print(f"Formatted names: {formatted_names}")
print("Explanation: Using split(), strip(), and title() methods together")
print()

# ======================================
# 🔹 Section 6: Complex Functions - Solutions
# ======================================

print("🔹 Section 6: Complex Functions - Solutions")
print("-" * 40)

# Q11. Create a student grade calculator function - Solution
print("Q11. Create a student grade calculator function - Solution:")
def calculate_student_grade(name, quran_grade, hadith_grade, fiqh_grade):
    average = (quran_grade + hadith_grade + fiqh_grade) / 3
    
    print(f"📊 Grade Report for {name}")
    print(f"Quran: {quran_grade}%")
    print(f"Hadith: {hadith_grade}%")
    print(f"Fiqh: {fiqh_grade}%")
    print(f"Average: {average:.1f}%")
    
    if average >= 90:
        return "🌟 Excellent! MashaAllah!"
    elif average >= 80:
        return "✅ Good! Keep it up!"
    else:
        return "💪 Needs improvement!"

result = calculate_student_grade("Ahmed", 95, 88, 92)
print(f"Result: {result}")
print("Explanation: Complex function with calculations, printing, and conditional returns")
print()

# Q12. Create a prayer status tracker function - Solution
print("Q12. Create a prayer status tracker function - Solution:")
def track_prayer_status():
    prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
    completed = []
    
    print("🕌 Prayer Status Tracker:")
    for prayer in prayers:
        status = input(f"Did you pray {prayer}? (yes/no): ")
        if status.lower() == "yes":
            completed.append(prayer)
    
    print(f"\n✅ Completed prayers: {len(completed)}/5")
    print(f"📝 Prayers: {', '.join(completed)}")
    
    if len(completed) == 5:
        return "🌟 Perfect! All prayers completed!"
    elif len(completed) >= 3:
        return "✅ Good effort! Keep it up!"
    else:
        return "💪 Try to pray more regularly!"

print("(Function created - requires user input to test)")
print("Explanation: Interactive function that collects user input and tracks prayer status")
print()

# ======================================
# 🔹 Section 7: Function Combinations - Solutions
# ======================================

print("🔹 Section 7: Function Combinations - Solutions")
print("-" * 40)

# Q13. Create multiple functions that work together - Solution
print("Q13. Create multiple functions that work together - Solution:")
def get_student_info(name, age):
    return f"Student: {name}, Age: {age}"

def get_subject_grade(subject, grade):
    if grade >= 90:
        status = "🌟 Excellent"
    elif grade >= 80:
        status = "✅ Good"
    else:
        status = "💪 Needs improvement"
    return f"{subject}: {grade}% - {status}"

def create_report(name, age, quran_grade, hadith_grade):
    print("📋 Student Report")
    print("-" * 20)
    print(get_student_info(name, age))
    print(get_subject_grade("Quran", quran_grade))
    print(get_subject_grade("Hadith", hadith_grade))

create_report("Ahmed", 15, 95, 88)
print("Explanation: Multiple functions working together - helper functions and main function")
print()

# ======================================
# 🔹 Bonus Challenge - Solution
# ======================================

print("🔹 Bonus Challenge - Solution:")
print("-" * 40)

# Q14. Create an Islamic quiz function - Solution
print("Q14. Create an Islamic quiz function - Solution:")
def islamic_quiz():
    questions = [
        "What is the first surah of Quran?",
        "How many daily prayers are there?",
        "What is the Islamic greeting?"
    ]
    answers = ["Al-Fatiha", "5", "Assalamu Alaikum"]
    score = 0
    
    print("📖 Islamic Quiz")
    print("=" * 20)
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == answers[i-1].lower():
            print("✅ Correct! MashaAllah!")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer: {answers[i-1]}")
    
    percentage = (score / len(questions)) * 100
    print(f"\n🎉 Quiz completed! Score: {score}/{len(questions)} ({percentage:.1f}%)")
    
    if percentage >= 80:
        return "🌟 Excellent Islamic knowledge!"
    elif percentage >= 60:
        return "✅ Good knowledge! Keep learning!"
    else:
        return "💪 Study more about Islam!"

print("(Function created - requires user input to test)")
print("Explanation: Interactive quiz function with scoring and feedback system")
print()

# ======================================
# 🔹 Additional Practice Examples
# ======================================

print("🔹 Additional Practice Examples:")
print("-" * 40)

# Example 1: Islamic calendar function
print("Example 1: Islamic Calendar Function:")
def check_islamic_month(month, day):
    if month.lower() == "ramadan":
        if day == 1:
            return "🕌 First day of Ramadan! Start fasting and reading Quran"
        elif day == 27:
            return "🌟 Laylatul Qadr - Night of Power! Special night for worship"
        elif day == 30:
            return "🌙 Last day of Ramadan! Complete your Quran reading"
        else:
            return f"🕌 Day {day} of Ramadan - Continue fasting and worship"
    else:
        return f"📅 Regular day in {month}"

# Test the function
print(check_islamic_month("Ramadan", 1))
print(check_islamic_month("Ramadan", 27))
print(check_islamic_month("Shaban", 15))
print()

# Example 2: Student performance analyzer
print("Example 2: Student Performance Analyzer:")
def analyze_student_performance(name, grades):
    if not grades:
        return "No grades available"
    
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    print(f"📊 Performance Analysis for {name}")
    print(f"Average: {average:.1f}%")
    print(f"Highest: {highest}%")
    print(f"Lowest: {lowest}%")
    
    if average >= 90:
        return "🌟 Outstanding performance! MashaAllah!"
    elif average >= 80:
        return "✅ Excellent performance! Keep it up!"
    elif average >= 70:
        return "📚 Good performance! Study more to improve!"
    else:
        return "💪 Needs significant improvement! Work harder!"

# Test the function
ahmed_grades = [85, 92, 78, 95, 88]
result = analyze_student_performance("Ahmed", ahmed_grades)
print(f"Result: {result}")
print()

# Example 3: Islamic greeting system
print("Example 3: Islamic Greeting System:")
def islamic_greeting_system(name, time_of_day, is_teacher=False):
    if is_teacher:
        title = "Maulana" if name == "Ahmed" else "Ustadh"
        greeting = f"Assalamu Alaikum {title} {name}"
    else:
        greeting = f"Assalamu Alaikum {name}"
    
    if time_of_day == "morning":
        greeting += " - Good morning! Time for Fajr prayer"
    elif time_of_day == "afternoon":
        greeting += " - Good afternoon! Time for Dhuhr prayer"
    elif time_of_day == "evening":
        greeting += " - Good evening! Time for Maghrib prayer"
    else:
        greeting += " - May Allah bless you"
    
    return greeting

# Test the function
print(islamic_greeting_system("Ahmed", "morning", True))
print(islamic_greeting_system("Fatima", "afternoon", False))
print(islamic_greeting_system("Ali", "evening", False))
print()

print("🎉 All solutions completed!")
print("📚 Keep practicing and learning functions!")
print("🕌 Functions help you create reusable Islamic tools and applications!") 