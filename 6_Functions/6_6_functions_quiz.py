# 5_6_functions_quiz.py

# ==================================================
# 📝 Functions: Final Quiz
# ==================================================
# 🎯 Learning Objective: Test understanding of functions
# 📚 Islamic Context: Using Islamic examples in the quiz

print("📝 Functions Final Quiz")
print("=" * 50)
print("📌 Instructions:")
print("Solve all questions step-by-step.")
print("Do not skip any part.")
print()

# ======================================
# 🔹 Section 1: Basic Functions
# ======================================

print("🔹 Section 1: Basic Functions")
print("-" * 30)

# Q1. Create a function that prints "Assalamu Alaikum"
print("Q1. Create a function that prints 'Assalamu Alaikum'")
# 👇 Write your code below:
def say_salam():
    print("Assalamu Alaikum")

# Call the function
say_salam()
print()

# Q2. Create a function that lists 3 Islamic subjects
print("Q2. Create a function that lists 3 Islamic subjects")
# 👇 Write your code below:
def list_subjects():
    print("📚 Islamic Subjects:")
    print("1. Quran")
    print("2. Hadith")
    print("3. Fiqh")

# Call the function
list_subjects()
print()

# ======================================
# 🔹 Section 2: Functions with Parameters
# ======================================

print("🔹 Section 2: Functions with Parameters")
print("-" * 30)

# Q3. Create a function that takes a name and greets the person
print("Q3. Create a function that takes a name and greets the person")
# 👇 Write your code below:
def greet_person(name):
    print(f"Assalamu Alaikum {name}")

# Call the function
greet_person("Ahmed")
greet_person("Fatima")
print()

# Q4. Create a function that takes prayer name and shows its time
print("Q4. Create a function that takes prayer name and shows its time")
# 👇 Write your code below:
def show_prayer_time(prayer):
    if prayer == "Fajr":
        print(f"🕌 {prayer} prayer: 5:00 AM")
    elif prayer == "Dhuhr":
        print(f"🕌 {prayer} prayer: 12:00 PM")
    elif prayer == "Asr":
        print(f"🕌 {prayer} prayer: 3:00 PM")
    else:
        print(f"🕌 {prayer} prayer time")

# Call the function
show_prayer_time("Fajr")
show_prayer_time("Dhuhr")
print()

# ======================================
# 🔹 Section 3: Functions with Return Values
# ======================================

print("🔹 Section 3: Functions with Return Values")
print("-" * 30)

# Q5. Create a function that returns "MashaAllah" for good grades
print("Q5. Create a function that returns 'MashaAllah' for good grades")
# 👇 Write your code below:
def get_grade_message(grade):
    if grade >= 90:
        return "MashaAllah! Excellent!"
    elif grade >= 80:
        return "MashaAllah! Good job!"
    else:
        return "Keep trying!"

# Test the function
message1 = get_grade_message(95)
print(f"Grade 95: {message1}")

message2 = get_grade_message(85)
print(f"Grade 85: {message2}")
print()

# Q6. Create a function that returns prayer count
print("Q6. Create a function that returns prayer count")
# 👇 Write your code below:
def count_prayers(prayed_fajr, prayed_dhuhr, prayed_asr, prayed_maghrib, prayed_isha):
    total = prayed_fajr + prayed_dhuhr + prayed_asr + prayed_maghrib + prayed_isha
    return total

# Test the function
prayers_today = count_prayers(1, 1, 0, 1, 1)
print(f"Prayers completed today: {prayers_today}/5")
print()

# ======================================
# 🔹 Section 4: Default Parameters
# ======================================

print("🔹 Section 4: Default Parameters")
print("-" * 30)

# Q7. Create a function with default name parameter
print("Q7. Create a function with default name parameter")
# 👇 Write your code below:
def greet_with_default(name="Brother/Sister"):
    print(f"Assalamu Alaikum {name}")

# Test the function
greet_with_default("Ahmed")
greet_with_default()
print()

# Q8. Create a function with default study time
print("Q8. Create a function with default study time")
# 👇 Write your code below:
def study_reminder(subject="Quran", hours=2):
    print(f"📚 Study {subject} for {hours} hours")
    if hours >= 3:
        print("🌟 Excellent study plan!")

# Test the function
study_reminder("Hadith", 3)
study_reminder("Fiqh")
study_reminder()
print()

# ======================================
# 🔹 Section 5: String Methods
# ======================================

print("🔹 Section 5: String Methods")
print("-" * 30)

# Q9. Use string methods to format Islamic text
print("Q9. Use string methods to format Islamic text")
# 👇 Write your code below:
islamic_text = "  assalamu alaikum  "
print(f"Original: '{islamic_text}'")

# Clean and format
cleaned_text = islamic_text.strip().title()
print(f"Cleaned: '{cleaned_text}'")
print()

# Q10. Use string methods to process names
print("Q10. Use string methods to process names")
# 👇 Write your code below:
names = "ahmed,fatima,ali"
print(f"Original: {names}")

# Split and format
name_list = names.split(",")
formatted_names = []
for name in name_list:
    formatted_names.append(name.strip().title())

print(f"Formatted names: {formatted_names}")
print()

# ======================================
# 🔹 Section 6: Complex Functions
# ======================================

print("🔹 Section 6: Complex Functions")
print("-" * 30)

# Q11. Create a student grade calculator function
print("Q11. Create a student grade calculator function")
# 👇 Write your code below:
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

# Test the function
result = calculate_student_grade("Ahmed", 95, 88, 92)
print(f"Result: {result}")
print()

# Q12. Create a prayer status tracker function
print("Q12. Create a prayer status tracker function")
# 👇 Write your code below:
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

# Uncomment to test (requires user input)
# result = track_prayer_status()
# print(f"Result: {result}")
print("(Function created - uncomment to test with user input)")
print()

# ======================================
# 🔹 Section 7: Function Combinations
# ======================================

print("🔹 Section 7: Function Combinations")
print("-" * 30)

# Q13. Create multiple functions that work together
print("Q13. Create multiple functions that work together")
# 👇 Write your code below:

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

# Test the combined functions
create_report("Ahmed", 15, 95, 88)
print()

# ======================================
# 🔹 Bonus Challenge
# ======================================

print("🔹 Bonus Challenge:")
print("-" * 30)

# Q14. Create an Islamic quiz function
print("Q14. Create an Islamic quiz function")
# 👇 Write your code below:

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

# Uncomment to test (requires user input)
# result = islamic_quiz()
# print(f"Result: {result}")
print("(Function created - uncomment to test with user input)")

print()
print("🎉 Congratulations! You've completed the Functions Quiz!")
print("📚 Functions are powerful tools for organizing and reusing code!") 