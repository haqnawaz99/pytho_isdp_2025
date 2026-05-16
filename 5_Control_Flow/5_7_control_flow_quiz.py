# 4_7_control_flow_quiz.py

# ==================================================
# 📝 Control Flow: Final Quiz
# ==================================================
# 🎯 Learning Objective: Test understanding of control flow
# 📚 Islamic Context: Using Islamic examples in the quiz

print("📝 Control Flow Final Quiz")
print("=" * 50)
print("📌 Instructions:")
print("Solve all questions step-by-step.")
print("Do not skip any part.")
print()

# ======================================
# 🔹 Section 1: If Statements
# ======================================

print("🔹 Section 1: If Statements")
print("-" * 30)

# Q1. Create a variable for student age and check if they can start Quran memorization
print("Q1. Student Age Check:")
# 👇 Write your code below:
student_age = 12

if student_age >= 10:
    print("✅ Student can start Quran memorization")
else:
    print("👶 Student is too young for memorization")

print()

# Q2. Check if it's prayer time
print("Q2. Prayer Time Check:")
# 👇 Write your code below:
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

print()

# ======================================
# 🔹 Section 2: Comparison Operators
# ======================================

print("🔹 Section 2: Comparison Operators")
print("-" * 30)

# Q3. Check if student passed exam (score >= 70)
print("Q3. Exam Result Check:")
# 👇 Write your code below:
exam_score = 85

if exam_score >= 70:
    print("🎉 Student passed the exam")
else:
    print("📚 Student needs to study more")

print()

# Q4. Check if study hours are between 2 and 5
print("Q4. Study Hours Check:")
# 👇 Write your code below:
study_hours = 3

if study_hours >= 2 and study_hours <= 5:
    print("📖 Good study session length")
else:
    print("⏰ Study time needs adjustment")

print()

# ======================================
# 🔹 Section 3: Logical Operators
# ======================================

print("🔹 Section 3: Logical Operators")
print("-" * 30)

# Q5. Check if student attended class AND did homework
print("Q5. Student Activity Check:")
# 👇 Write your code below:
attended_class = True
did_homework = True

if attended_class and did_homework:
    print("🌟 Perfect student!")
elif attended_class or did_homework:
    print("✅ Good effort")
else:
    print("💪 Need to improve")

print()

# Q6. Check if it's NOT weekend
print("Q6. Weekend Check:")
# 👇 Write your code below:
is_weekend = False

if not is_weekend:
    print("📚 Regular school day")
else:
    print("🏠 Weekend - time to rest")

print()

# ======================================
# 🔹 Section 4: While Loops
# ======================================

print("🔹 Section 4: While Loops")
print("-" * 30)

# Q7. Count from 1 to 5 with Islamic messages
print("Q7. Islamic Counting:")
# 👇 Write your code below:
count = 1
while count <= 5:
    print(f"Number {count}: Bismillah")
    count += 1

print()

# Q8. Ask user for prayer status until they say "done"
print("Q8. Prayer Status Tracker:")
# 👇 Write your code below:
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

print()

# ======================================
# 🔹 Section 5: For Loops
# ======================================

print("🔹 Section 5: For Loops")
print("-" * 30)

# Q9. Loop through Islamic subjects
print("Q9. Islamic Subjects:")
# 👇 Write your code below:
subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah"]

for subject in subjects:
    print(f"📚 Studying {subject}")

print()

# Q10. Count even numbers from 2 to 10
print("Q10. Even Numbers:")
# 👇 Write your code below:
for num in range(2, 11, 2):
    print(f"Even number: {num}")

print()

# ======================================
# 🔹 Section 6: Complex Problems
# ======================================

print("🔹 Section 6: Complex Problems")
print("-" * 30)

# Q11. Student grade evaluation system
print("Q11. Student Grade Evaluation:")
# 👇 Write your code below:
grades = [85, 92, 78, 95, 88]

for student, grade in enumerate(grades, 1):
    if grade >= 90:
        print(f"Student {student}: {grade} - 🌟 Excellent!")
    elif grade >= 80:
        print(f"Student {student}: {grade} - ✅ Good!")
    else:
        print(f"Student {student}: {grade} - 💪 Need improvement")

print()

# Q12. Daily routine checker
print("Q12. Daily Routine Check:")
# 👇 Write your code below:
activities = ["prayer", "study", "help", "prayer", "rest"]

prayer_count = 0
for activity in activities:
    if activity == "prayer":
        prayer_count += 1
        print(f"✅ {activity.capitalize()} #{prayer_count}")
    else:
        print(f"📝 {activity.capitalize()}")

print(f"🎉 Total prayers: {prayer_count}")

print()

# ======================================
# 🔹 Bonus Challenge
# ======================================

print("🔹 Bonus Challenge:")
print("-" * 30)

# Q13. Create a simple Islamic quiz system
print("Q13. Islamic Quiz System:")
# 👇 Write your code below:
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

print()
print("🎉 Congratulations! You've completed the Control Flow Quiz!") 