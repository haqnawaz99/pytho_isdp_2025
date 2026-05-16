# 4_9_islamic_applications.py

# ==================================================
# 📝 Control Flow: Islamic Applications
# ==================================================
# 🎯 Learning Objective: Apply control flow to real Islamic scenarios
# 📚 Islamic Context: Practical applications for madrasah students

print("🕌 Islamic Applications with Control Flow")
print("=" * 50)

# ======================================
# 🔹 Application 1: Prayer Time Reminder System
# ======================================

print("🔹 Application 1: Prayer Time Reminder System")
print("-" * 40)

def prayer_reminder():
    print("🕌 Prayer Time Reminder System")
    print("=" * 30)
    
    # Get current time from user
    current_hour = int(input("Enter current hour (0-23): "))
    
    # Prayer time logic
    if current_hour >= 5 and current_hour < 6:
        print("🌅 Time for Fajr prayer!")
        print("📖 Recommended: Read 2-3 pages of Quran after Fajr")
    elif current_hour >= 12 and current_hour < 13:
        print("☀️ Time for Dhuhr prayer!")
        print("📚 Good time to study Islamic subjects")
    elif current_hour >= 15 and current_hour < 16:
        print("🌤️ Time for Asr prayer!")
        print("🤝 Good time to help others")
    elif current_hour >= 18 and current_hour < 19:
        print("🌆 Time for Maghrib prayer!")
        print("🍽️ Time to break fast (if fasting)")
    elif current_hour >= 20 and current_hour < 21:
        print("🌙 Time for Isha prayer!")
        print("📖 Good time to read Quran before sleep")
    else:
        print("⏰ Not prayer time")
        if current_hour < 5:
            print("💤 Early morning - time to rest")
        elif current_hour < 12:
            print("📚 Morning study time")
        elif current_hour < 15:
            print("🕌 Afternoon activities")
        elif current_hour < 18:
            print("🌅 Evening preparation")
        else:
            print("🌙 Night time - prepare for sleep")

# Run prayer reminder
prayer_reminder()
print()

# ======================================
# 🔹 Application 2: Student Grade Calculator
# ======================================

print("🔹 Application 2: Student Grade Calculator")
print("-" * 40)

def grade_calculator():
    print("📚 Student Grade Calculator")
    print("=" * 30)
    
    # Get student information
    student_name = input("Enter student name: ")
    subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah", "Seerah"]
    grades = []
    
    # Collect grades for each subject
    for subject in subjects:
        while True:
            try:
                grade = int(input(f"Enter grade for {subject} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("❌ Grade must be between 0 and 100")
            except ValueError:
                print("❌ Please enter a valid number")
    
    # Calculate average
    average = sum(grades) / len(grades)
    
    # Display results
    print(f"\n📊 Grade Report for {student_name}")
    print("-" * 30)
    
    for i, subject in enumerate(subjects):
        grade = grades[i]
        if grade >= 90:
            status = "🌟 Excellent"
        elif grade >= 80:
            status = "✅ Good"
        elif grade >= 70:
            status = "📚 Satisfactory"
        else:
            status = "💪 Needs Improvement"
        
        print(f"{subject}: {grade}% - {status}")
    
    print(f"\n📊 Overall Average: {average:.1f}%")
    
    if average >= 90:
        print("🎉 Overall Performance: Excellent! MashaAllah!")
    elif average >= 80:
        print("✅ Overall Performance: Good! Keep it up!")
    elif average >= 70:
        print("📚 Overall Performance: Satisfactory. Study more!")
    else:
        print("💪 Overall Performance: Needs improvement. Work harder!")

# Run grade calculator
grade_calculator()
print()

# ======================================
# 🔹 Application 3: Islamic Quiz System
# ======================================

print("🔹 Application 3: Islamic Quiz System")
print("-" * 40)

def islamic_quiz():
    print("📖 Islamic Knowledge Quiz")
    print("=" * 30)
    
    # Quiz questions and answers
    questions = [
        "What is the first surah of the Quran?",
        "How many daily prayers are obligatory?",
        "What is the Islamic greeting?",
        "Which month is the month of fasting?",
        "What is the name of the Prophet's mosque in Madinah?"
    ]
    
    answers = ["Al-Fatiha", "5", "Assalamu Alaikum", "Ramadan", "Masjid Nabawi"]
    explanations = [
        "Al-Fatiha is the opening chapter of the Quran",
        "There are 5 obligatory daily prayers",
        "Assalamu Alaikum means 'Peace be upon you'",
        "Ramadan is the blessed month of fasting",
        "Masjid Nabawi is the Prophet's mosque in Madinah"
    ]
    
    score = 0
    total_questions = len(questions)
    
    print(f"📝 Total Questions: {total_questions}")
    print("🎯 Answer each question correctly to score points\n")
    
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == answers[i-1].lower():
            print("✅ Correct! MashaAllah!")
            print(f"💡 {explanations[i-1]}")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer: {answers[i-1]}")
            print(f"💡 {explanations[i-1]}")
        
        print()
    
    # Display final results
    percentage = (score / total_questions) * 100
    
    print("📊 Quiz Results")
    print("-" * 20)
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("🌟 Excellent! You have great Islamic knowledge!")
    elif percentage >= 80:
        print("✅ Good! Keep learning more about Islam!")
    elif percentage >= 70:
        print("📚 Satisfactory! Study more Islamic topics!")
    else:
        print("💪 Keep studying! Knowledge is a blessing!")

# Run Islamic quiz
islamic_quiz()
print()

# ======================================
# 🔹 Application 4: Daily Routine Tracker
# ======================================

print("🔹 Application 4: Daily Routine Tracker")
print("-" * 40)

def daily_routine_tracker():
    print("📅 Daily Islamic Routine Tracker")
    print("=" * 35)
    
    # Initialize routine checklist
    routine_items = [
        "Fajr Prayer",
        "Quran Reading",
        "Islamic Study",
        "Dhuhr Prayer",
        "Help Family",
        "Asr Prayer",
        "Dhikr",
        "Maghrib Prayer",
        "Evening Quran",
        "Isha Prayer"
    ]
    
    completed_items = []
    missed_items = []
    
    print("📋 Daily Routine Checklist:")
    print("Mark each item as completed (yes) or missed (no)")
    print()
    
    for item in routine_items:
        while True:
            response = input(f"✅ {item}? (yes/no): ").lower()
            if response in ['yes', 'no']:
                if response == 'yes':
                    completed_items.append(item)
                else:
                    missed_items.append(item)
                break
            else:
                print("❌ Please enter 'yes' or 'no'")
    
    # Display results
    print("\n📊 Daily Routine Report")
    print("-" * 25)
    print(f"✅ Completed: {len(completed_items)}/{len(routine_items)}")
    print(f"❌ Missed: {len(missed_items)}/{len(routine_items)}")
    
    completion_rate = (len(completed_items) / len(routine_items)) * 100
    
    print(f"📈 Completion Rate: {completion_rate:.1f}%")
    
    if completion_rate >= 90:
        print("🌟 Excellent day! MashaAllah!")
    elif completion_rate >= 80:
        print("✅ Good day! Keep it up!")
    elif completion_rate >= 70:
        print("📚 Decent day. Try to do better tomorrow!")
    else:
        print("💪 Tomorrow is a new day. Make it better!")
    
    if missed_items:
        print(f"\n📝 Missed items to improve:")
        for item in missed_items:
            print(f"   - {item}")

# Run daily routine tracker
daily_routine_tracker()
print()

# ======================================
# 🔹 Application 5: Islamic Calendar Helper
# ======================================

print("🔹 Application 5: Islamic Calendar Helper")
print("-" * 40)

def islamic_calendar_helper():
    print("📅 Islamic Calendar Helper")
    print("=" * 30)
    
    # Get user input
    month = input("Enter Islamic month name: ").title()
    
    try:
        day = int(input("Enter day of the month (1-30): "))
    except ValueError:
        print("❌ Please enter a valid day number")
        return
    
    # Check if day is valid
    if day < 1 or day > 30:
        print("❌ Day must be between 1 and 30")
        return
    
    # Islamic calendar logic
    print(f"\n📅 {month} - Day {day}")
    print("-" * 20)
    
    if month == "Ramadan":
        if day == 1:
            print("🕌 First day of Ramadan!")
            print("📖 Start your fasting and Quran reading")
        elif day == 27:
            print("🌟 Laylatul Qadr - Night of Power!")
            print("🕌 Special night for worship and dua")
        elif day == 30:
            print("🌙 Last day of Ramadan")
            print("📖 Complete your Quran reading")
        else:
            print("🕌 Blessed day of Ramadan")
            print("📖 Continue fasting and reading Quran")
    
    elif month == "Dhul Hijjah":
        if day >= 10 and day <= 13:
            print("🐪 Days of Eid al-Adha!")
            print("🕌 Time for sacrifice and celebration")
        elif day == 9:
            print("🏔️ Day of Arafah!")
            print("🕌 Special day for fasting and dua")
        else:
            print("📅 Regular day in Dhul Hijjah")
    
    elif month == "Muharram":
        if day == 10:
            print("📖 Day of Ashura!")
            print("🕌 Recommended to fast on this day")
        else:
            print("📅 Regular day in Muharram")
    
    elif month == "Rajab":
        if day == 27:
            print("🌙 Laylatul Isra wal Mi'raj!")
            print("🕌 Night of the Prophet's journey")
        else:
            print("📅 Regular day in Rajab")
    
    elif month == "Shaban":
        if day == 15:
            print("🌙 Laylatul Bara'ah!")
            print("🕌 Night of forgiveness")
        else:
            print("📅 Regular day in Shaban")
    
    else:
        print("📅 Regular Islamic month")
        print("📖 Continue your daily Islamic activities")

# Run Islamic calendar helper
islamic_calendar_helper()
print()

print("🎉 All Islamic Applications Completed!")
print("📚 These applications show how control flow can be used in real Islamic scenarios")
print("🕌 Keep learning and applying programming to Islamic education!") 