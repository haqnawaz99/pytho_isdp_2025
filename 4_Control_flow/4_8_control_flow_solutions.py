# 4_8_control_flow_solutions.py

# ==================================================
# 📝 Control Flow: Quiz Solutions
# ==================================================
# 🎯 Learning Objective: Check your answers
# 📚 Islamic Context: Complete solutions with explanations

print("📝 Control Flow Quiz Solutions")
print("=" * 50)
print("📌 These are the complete solutions.")
print("Compare with your answers to learn.")
print()

# ======================================
# 🔹 Section 1: If Statements - Solutions
# ======================================

print("🔹 Section 1: If Statements - Solutions")
print("-" * 40)

# Q1. Student Age Check - Solution
print("Q1. Student Age Check - Solution:")
student_age = 12

if student_age >= 10:
    print("✅ Student can start Quran memorization")
else:
    print("👶 Student is too young for memorization")
print("Explanation: We check if age is 10 or more using >= operator")

print()

# Q2. Prayer Time Check - Solution
print("Q2. Prayer Time Check - Solution:")
current_time = "Fajr"

if current_time == "Fajr":
    print("🌅 Time for Fajr prayer")
elif current_time == "Dhuhr":
    print("☀️ Time for Dhuhr prayer")
elif current_time == "Asr":
    print("🌤️ Time for Asr prayer")
elif current_time == "Maghrib":
    print("🌆 Time for Maghrib prayer")
elif current_time == "Isha":
    print("🌙 Time for Isha prayer")
else:
    print("⏰ Not prayer time")
print("Explanation: Using elif for multiple conditions, else for default case")

print()

# ======================================
# 🔹 Section 2: Comparison Operators - Solutions
# ======================================

print("🔹 Section 2: Comparison Operators - Solutions")
print("-" * 40)

# Q3. Exam Result Check - Solution
print("Q3. Exam Result Check - Solution:")
exam_score = 85

if exam_score >= 70:
    print("🎉 Student passed the exam")
else:
    print("📚 Student needs to study more")
print("Explanation: Using >= to check if score is 70 or higher")

print()

# Q4. Study Hours Check - Solution
print("Q4. Study Hours Check - Solution:")
study_hours = 3

if study_hours >= 2 and study_hours <= 5:
    print("📖 Good study session length")
else:
    print("⏰ Study time needs adjustment")
print("Explanation: Using AND to check if hours are between 2 and 5")

print()

# ======================================
# 🔹 Section 3: Logical Operators - Solutions
# ======================================

print("🔹 Section 3: Logical Operators - Solutions")
print("-" * 40)

# Q5. Student Activity Check - Solution
print("Q5. Student Activity Check - Solution:")
attended_class = True
did_homework = True

if attended_class and did_homework:
    print("🌟 Perfect student!")
elif attended_class or did_homework:
    print("✅ Good effort")
else:
    print("💪 Need to improve")
print("Explanation: AND requires both conditions, OR requires at least one")

print()

# Q6. Weekend Check - Solution
print("Q6. Weekend Check - Solution:")
is_weekend = False

if not is_weekend:
    print("📚 Regular school day")
else:
    print("🏠 Weekend - time to rest")
print("Explanation: NOT operator reverses True to False and vice versa")

print()

# ======================================
# 🔹 Section 4: While Loops - Solutions
# ======================================

print("🔹 Section 4: While Loops - Solutions")
print("-" * 40)

# Q7. Islamic Counting - Solution
print("Q7. Islamic Counting - Solution:")
count = 1
while count <= 5:
    print(f"Number {count}: Bismillah")
    count += 1
print("Explanation: While loop continues until count reaches 5")

print()

# Q8. Prayer Status Tracker - Solution
print("Q8. Prayer Status Tracker - Solution:")
prayer_count = 0
while True:
    status = input("Enter prayer status (prayed/missed/done): ")
    if status == "done":
        break
    elif status == "prayed":
        prayer_count += 1
        print(f"✅ Prayed! Total: {prayer_count}")
    elif status == "missed":
        print("❌ Missed prayer")

print(f"🎉 Total prayers completed: {prayer_count}")
print("Explanation: Infinite while loop with break condition")

print()

# ======================================
# 🔹 Section 5: For Loops - Solutions
# ======================================

print("🔹 Section 5: For Loops - Solutions")
print("-" * 40)

# Q9. Islamic Subjects - Solution
print("Q9. Islamic Subjects - Solution:")
subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah"]

for subject in subjects:
    print(f"📚 Studying {subject}")
print("Explanation: For loop iterates through each item in the list")

print()

# Q10. Even Numbers - Solution
print("Q10. Even Numbers - Solution:")
for num in range(2, 11, 2):
    print(f"Even number: {num}")
print("Explanation: Range with step 2 gives even numbers from 2 to 10")

print()

# ======================================
# 🔹 Section 6: Complex Problems - Solutions
# ======================================

print("🔹 Section 6: Complex Problems - Solutions")
print("-" * 40)

# Q11. Student Grade Evaluation - Solution
print("Q11. Student Grade Evaluation - Solution:")
grades = [85, 92, 78, 95, 88]

for student, grade in enumerate(grades, 1):
    if grade >= 90:
        print(f"Student {student}: {grade} - 🌟 Excellent!")
    elif grade >= 80:
        print(f"Student {student}: {grade} - ✅ Good!")
    else:
        print(f"Student {student}: {grade} - 💪 Need improvement")
print("Explanation: Enumerate gives both index and value, starting from 1")

print()

# Q12. Daily Routine Check - Solution
print("Q12. Daily Routine Check - Solution:")
activities = ["prayer", "study", "help", "prayer", "rest"]

prayer_count = 0
for activity in activities:
    if activity == "prayer":
        prayer_count += 1
        print(f"✅ {activity.capitalize()} #{prayer_count}")
    else:
        print(f"📝 {activity.capitalize()}")

print(f"🎉 Total prayers: {prayer_count}")
print("Explanation: Counting specific activities in a list")

print()

# ======================================
# 🔹 Bonus Challenge - Solution
# ======================================

print("🔹 Bonus Challenge - Solution:")
print("-" * 40)

# Q13. Islamic Quiz System - Solution
print("Q13. Islamic Quiz System - Solution:")
questions = [
    "What is the first surah of Quran?",
    "How many daily prayers are there?",
    "What is the Islamic greeting?"
]

answers = ["Al-Fatiha", "5", "Assalamu Alaikum"]
score = 0

for i, question in enumerate(questions):
    print(f"\nQuestion {i+1}: {question}")
    user_answer = input("Your answer: ")
    
    if user_answer.lower() == answers[i].lower():
        print("✅ Correct! MashaAllah!")
        score += 1
    else:
        print(f"❌ Wrong. Correct answer: {answers[i]}")

print(f"\n🎉 Quiz completed! Score: {score}/{len(questions)}")
print("Explanation: Interactive quiz with score tracking")

print()

# ======================================
# 🔹 Additional Practice Examples
# ======================================

print("🔹 Additional Practice Examples:")
print("-" * 40)

# Example 1: Islamic calendar checker
print("Example 1: Islamic Calendar Checker:")
month = "Ramadan"
day = 15

if month == "Ramadan":
    if day >= 1 and day <= 30:
        print("🕌 Blessed month of Ramadan")
        if day == 27:
            print("🌟 Laylatul Qadr - Night of Power")
    else:
        print("❌ Invalid day for Ramadan")
else:
    print("📅 Regular Islamic month")

print()

# Example 2: Student performance tracker
print("Example 2: Student Performance Tracker:")
subjects = ["Quran", "Hadith", "Fiqh"]
grades = [85, 92, 78]

total_score = 0
for i, subject in enumerate(subjects):
    grade = grades[i]
    total_score += grade
    
    if grade >= 90:
        print(f"{subject}: 🌟 Excellent ({grade})")
    elif grade >= 80:
        print(f"{subject}: ✅ Good ({grade})")
    else:
        print(f"{subject}: 💪 Needs improvement ({grade})")

average = total_score / len(subjects)
print(f"\n📊 Average Score: {average:.1f}")

if average >= 85:
    print("🎉 Overall Performance: Excellent!")
elif average >= 75:
    print("✅ Overall Performance: Good!")
else:
    print("💪 Overall Performance: Needs improvement")

print()

print("🎉 All solutions completed!")
print("📚 Keep practicing and learning!") 