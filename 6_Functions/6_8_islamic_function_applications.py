# 5_8_islamic_function_applications.py

# ==================================================
# 📝 Functions: Islamic Applications
# ==================================================
# 🎯 Learning Objective: Apply functions to real Islamic scenarios
# 📚 Islamic Context: Practical applications for madrasah students

print("🕌 Islamic Applications with Functions")
print("=" * 50)

# ======================================
# 🔹 Application 1: Islamic Greeting System
# ======================================

print("🔹 Application 1: Islamic Greeting System")
print("-" * 40)

def islamic_greeting_system():
    print("🤝 Islamic Greeting System")
    print("=" * 30)
    
    def get_greeting(name, time_of_day, is_teacher=False):
        """Generate appropriate Islamic greeting based on context"""
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
    
    def get_response_greeting(name, is_teacher=False):
        """Generate response greeting"""
        if is_teacher:
            return f"Wa Alaikum Assalam Maulana {name}"
        else:
            return f"Wa Alaikum Assalam {name}"
    
    # Test the greeting system
    print("Morning Greetings:")
    print(get_greeting("Ahmed", "morning", True))
    print(get_response_greeting("Ahmed", True))
    
    print("\nAfternoon Greetings:")
    print(get_greeting("Fatima", "afternoon", False))
    print(get_response_greeting("Fatima", False))
    
    print("\nEvening Greetings:")
    print(get_greeting("Ali", "evening", False))
    print(get_response_greeting("Ali", False))

# Run the greeting system
islamic_greeting_system()
print()

# ======================================
# 🔹 Application 2: Prayer Time Calculator
# ======================================

print("🔹 Application 2: Prayer Time Calculator")
print("-" * 40)

def prayer_time_calculator():
    print("🕌 Prayer Time Calculator")
    print("=" * 30)
    
    def get_prayer_time(prayer, city="Lahore"):
        """Get prayer time for a specific prayer and city"""
        prayer_times = {
            "Lahore": {
                "Fajr": "5:15 AM",
                "Dhuhr": "12:15 PM",
                "Asr": "3:30 PM",
                "Maghrib": "6:45 PM",
                "Isha": "8:15 PM"
            },
            "Karachi": {
                "Fajr": "5:30 AM",
                "Dhuhr": "12:30 PM",
                "Asr": "3:45 PM",
                "Maghrib": "7:00 PM",
                "Isha": "8:30 PM"
            }
        }
        
        if city in prayer_times and prayer in prayer_times[city]:
            return prayer_times[city][prayer]
        else:
            return "Time not available"
    
    def get_next_prayer(current_hour):
        """Determine the next prayer based on current time"""
        if current_hour < 5:
            return "Fajr"
        elif current_hour < 12:
            return "Dhuhr"
        elif current_hour < 15:
            return "Asr"
        elif current_hour < 18:
            return "Maghrib"
        else:
            return "Isha"
    
    def format_prayer_schedule(city="Lahore"):
        """Format complete prayer schedule for a city"""
        prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
        schedule = f"📅 Prayer Schedule for {city}:\n"
        
        for prayer in prayers:
            time = get_prayer_time(prayer, city)
            schedule += f"   {prayer}: {time}\n"
        
        return schedule
    
    # Test the prayer calculator
    print("Current Prayer Times:")
    print(get_prayer_time("Fajr", "Lahore"))
    print(get_prayer_time("Dhuhr", "Karachi"))
    
    print(f"\nNext prayer at 2 PM: {get_next_prayer(14)}")
    
    print("\nComplete Schedule:")
    print(format_prayer_schedule("Lahore"))

# Run the prayer calculator
prayer_time_calculator()
print()

# ======================================
# 🔹 Application 3: Student Grade Management System
# ======================================

print("🔹 Application 3: Student Grade Management System")
print("-" * 40)

def student_grade_management():
    print("📚 Student Grade Management System")
    print("=" * 35)
    
    def calculate_average(grades):
        """Calculate average grade from a list of grades"""
        if not grades:
            return 0
        return sum(grades) / len(grades)
    
    def get_grade_letter(percentage):
        """Convert percentage to letter grade"""
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "F"
    
    def analyze_student_performance(name, grades_dict):
        """Analyze student performance across subjects"""
        print(f"📊 Performance Analysis for {name}")
        print("-" * 30)
        
        total_grades = []
        for subject, grade in grades_dict.items():
            print(f"{subject}: {grade}% ({get_grade_letter(grade)})")
            total_grades.append(grade)
        
        average = calculate_average(total_grades)
        print(f"\nOverall Average: {average:.1f}% ({get_grade_letter(average)})")
        
        if average >= 90:
            return "🌟 Outstanding! MashaAllah!"
        elif average >= 80:
            return "✅ Excellent! Keep it up!"
        elif average >= 70:
            return "📚 Good! Study more to improve!"
        else:
            return "💪 Needs improvement! Work harder!"
    
    def generate_report_card(name, age, grades_dict):
        """Generate a complete report card"""
        print(f"📋 Report Card - {name}")
        print("=" * 25)
        print(f"Student: {name}")
        print(f"Age: {age}")
        print(f"Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}")
        print()
        
        result = analyze_student_performance(name, grades_dict)
        print(f"\nFinal Result: {result}")
        
        return result
    
    # Test the grade management system
    ahmed_grades = {
        "Quran": 95,
        "Hadith": 88,
        "Fiqh": 92,
        "Aqeedah": 85,
        "Seerah": 90
    }
    
    fatima_grades = {
        "Quran": 78,
        "Hadith": 82,
        "Fiqh": 75,
        "Aqeedah": 80,
        "Seerah": 85
    }
    
    print("Student Report Cards:")
    print()
    generate_report_card("Ahmed", 15, ahmed_grades)
    print()
    generate_report_card("Fatima", 14, fatima_grades)

# Run the grade management system
student_grade_management()
print()

# ======================================
# 🔹 Application 4: Islamic Calendar Helper
# ======================================

print("🔹 Application 4: Islamic Calendar Helper")
print("-" * 40)

def islamic_calendar_helper():
    print("📅 Islamic Calendar Helper")
    print("=" * 30)
    
    def get_islamic_month_info(month, day):
        """Get information about specific Islamic month and day"""
        month_info = {
            "Muharram": {
                "description": "First month of Islamic calendar",
                "special_days": {10: "Day of Ashura - Recommended to fast"}
            },
            "Ramadan": {
                "description": "Blessed month of fasting",
                "special_days": {
                    1: "First day of Ramadan - Start fasting",
                    27: "Laylatul Qadr - Night of Power",
                    30: "Last day of Ramadan - Complete Quran reading"
                }
            },
            "Dhul Hijjah": {
                "description": "Month of Hajj",
                "special_days": {
                    9: "Day of Arafah - Special day for fasting",
                    10: "Eid al-Adha - Day of sacrifice"
                }
            }
        }
        
        if month in month_info:
            info = month_info[month]
            result = f"📅 {month} - Day {day}\n"
            result += f"📖 {info['description']}\n"
            
            if day in info['special_days']:
                result += f"🌟 {info['special_days'][day]}"
            else:
                result += "📚 Regular day - Continue your Islamic activities"
            
            return result
        else:
            return f"📅 {month} - Day {day}\n📚 Regular Islamic month"
    
    def get_prayer_recommendations(month, day):
        """Get prayer recommendations for specific days"""
        if month == "Ramadan" and day == 27:
            return [
                "🌙 Spend the night in worship",
                "📖 Read extra Quran",
                "🤲 Make special dua",
                "🕌 Pray Tahajjud"
            ]
        elif month == "Muharram" and day == 10:
            return [
                "📖 Fast on this day",
                "🤲 Make dua for forgiveness",
                "📚 Learn about Islamic history"
            ]
        else:
            return [
                "🕌 Pray all 5 daily prayers",
                "📖 Read Quran daily",
                "🤲 Make regular dua",
                "💝 Help others"
            ]
    
    def format_islamic_date(month, day):
        """Format Islamic date nicely"""
        return f"📅 {month} {day}, 1445 AH"
    
    # Test the calendar helper
    print("Islamic Calendar Information:")
    print()
    
    print(get_islamic_month_info("Ramadan", 27))
    print()
    
    print(get_islamic_month_info("Muharram", 10))
    print()
    
    print("Prayer Recommendations for Ramadan 27:")
    recommendations = get_prayer_recommendations("Ramadan", 27)
    for rec in recommendations:
        print(f"   {rec}")
    
    print(f"\nFormatted Date: {format_islamic_date('Ramadan', 27)}")

# Run the calendar helper
islamic_calendar_helper()
print()

# ======================================
# 🔹 Application 5: Islamic Study Planner
# ======================================

print("🔹 Application 5: Islamic Study Planner")
print("-" * 40)

def islamic_study_planner():
    print("📚 Islamic Study Planner")
    print("=" * 30)
    
    def create_study_schedule(subjects, hours_per_day):
        """Create a study schedule for Islamic subjects"""
        schedule = f"📅 Daily Study Schedule ({hours_per_day} hours)\n"
        schedule += "=" * 40 + "\n"
        
        hours_per_subject = hours_per_day / len(subjects)
        
        for i, subject in enumerate(subjects, 1):
            schedule += f"{i}. {subject}: {hours_per_subject:.1f} hours\n"
        
        return schedule
    
    def get_study_tips(subject):
        """Get study tips for specific Islamic subjects"""
        tips = {
            "Quran": [
                "📖 Read with proper tajweed",
                "🎯 Memorize one verse daily",
                "📝 Write down difficult words",
                "🔄 Review previous memorization"
            ],
            "Hadith": [
                "📚 Learn the chain of narrators",
                "🎯 Understand the context",
                "📝 Take notes on key points",
                "🔄 Practice narrating to others"
            ],
            "Fiqh": [
                "⚖️ Understand the reasoning",
                "📚 Study with examples",
                "📝 Compare different opinions",
                "🔄 Apply to daily situations"
            ]
        }
        
        if subject in tips:
            return tips[subject]
        else:
            return [
                "📖 Read regularly",
                "📝 Take notes",
                "🔄 Review frequently",
                "🤲 Ask Allah for help"
            ]
    
    def calculate_study_progress(current_page, total_pages, subject):
        """Calculate and display study progress"""
        progress = (current_page / total_pages) * 100
        remaining = total_pages - current_page
        
        print(f"📊 Progress in {subject}")
        print(f"Current Page: {current_page}")
        print(f"Total Pages: {total_pages}")
        print(f"Progress: {progress:.1f}%")
        print(f"Remaining: {remaining} pages")
        
        if progress >= 100:
            return "🎉 Completed! MashaAllah!"
        elif progress >= 75:
            return "🌟 Almost done! Keep going!"
        elif progress >= 50:
            return "✅ Good progress! Stay consistent!"
        else:
            return "💪 Keep studying regularly!"
    
    def recommend_study_time(age, difficulty_level):
        """Recommend study time based on age and difficulty"""
        base_time = 30  # minutes
        
        if age < 10:
            recommended = base_time
        elif age < 15:
            recommended = base_time * 2
        else:
            recommended = base_time * 3
        
        if difficulty_level == "easy":
            recommended *= 0.8
        elif difficulty_level == "hard":
            recommended *= 1.5
        
        return round(recommended)
    
    # Test the study planner
    subjects = ["Quran", "Hadith", "Fiqh", "Aqeedah"]
    
    print("Study Schedule:")
    print(create_study_schedule(subjects, 3))
    
    print("Study Tips for Quran:")
    quran_tips = get_study_tips("Quran")
    for tip in quran_tips:
        print(f"   {tip}")
    
    print("\nStudy Progress:")
    result = calculate_study_progress(15, 30, "Quran Memorization")
    print(f"Result: {result}")
    
    print(f"\nRecommended study time for 12-year-old (easy level):")
    time = recommend_study_time(12, "easy")
    print(f"{time} minutes per session")

# Run the study planner
islamic_study_planner()
print()

# ======================================
# 🔹 Application 6: Islamic Quiz System
# ======================================

print("🔹 Application 6: Islamic Quiz System")
print("-" * 40)

def islamic_quiz_system():
    print("📖 Islamic Quiz System")
    print("=" * 30)
    
    def create_quiz_question(question, answer, options=None, explanation=""):
        """Create a quiz question with all details"""
        return {
            "question": question,
            "answer": answer,
            "options": options,
            "explanation": explanation
        }
    
    def run_quiz(questions):
        """Run a complete quiz with scoring"""
        print("📝 Islamic Knowledge Quiz")
        print("=" * 25)
        print(f"Total Questions: {len(questions)}")
        print("Answer each question correctly to score points\n")
        
        score = 0
        total_questions = len(questions)
        
        for i, q in enumerate(questions, 1):
            print(f"Question {i}: {q['question']}")
            
            if q['options']:
                for j, option in enumerate(q['options'], 1):
                    print(f"   {j}. {option}")
                print("Enter the number of your answer:")
            else:
                print("Enter your answer:")
            
            # Simulate user input for demonstration
            user_answer = q['answer']  # In real app, this would be input()
            
            if user_answer.lower() == q['answer'].lower():
                print("✅ Correct! MashaAllah!")
                score += 1
            else:
                print(f"❌ Wrong. Correct answer: {q['answer']}")
            
            if q['explanation']:
                print(f"💡 {q['explanation']}")
            print()
        
        percentage = (score / total_questions) * 100
        print(f"🎉 Quiz completed! Score: {score}/{total_questions} ({percentage:.1f}%)")
        
        return get_quiz_result(percentage)
    
    def get_quiz_result(percentage):
        """Get result message based on quiz percentage"""
        if percentage >= 90:
            return "🌟 Excellent! You have outstanding Islamic knowledge!"
        elif percentage >= 80:
            return "✅ Very Good! Keep learning more about Islam!"
        elif percentage >= 70:
            return "📚 Good! Study more Islamic topics!"
        elif percentage >= 60:
            return "📖 Satisfactory! Need to study more!"
        else:
            return "💪 Keep studying! Knowledge is a blessing!"
    
    def generate_certificate(name, score, total_questions):
        """Generate a certificate for quiz completion"""
        percentage = (score / total_questions) * 100
        grade = "A+" if percentage >= 90 else "A" if percentage >= 80 else "B" if percentage >= 70 else "C"
        
        certificate = f"""
        🏆 Islamic Knowledge Certificate
        {'=' * 40}
        
        This is to certify that
        
        {name}
        
        has completed the Islamic Knowledge Quiz with a score of
        
        {score}/{total_questions} ({percentage:.1f}%) - Grade: {grade}
        
        Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}
        
        {'=' * 40}
        """
        return certificate
    
    # Create quiz questions
    questions = [
        create_quiz_question(
            "What is the first surah of the Quran?",
            "Al-Fatiha",
            ["Al-Fatiha", "Al-Baqarah", "Al-Imran", "An-Nisa"],
            "Al-Fatiha is the opening chapter of the Quran"
        ),
        create_quiz_question(
            "How many daily prayers are obligatory?",
            "5",
            ["3", "4", "5", "6"],
            "There are 5 obligatory daily prayers in Islam"
        ),
        create_quiz_question(
            "What is the Islamic greeting?",
            "Assalamu Alaikum",
            ["Hello", "Good morning", "Assalamu Alaikum", "Peace"],
            "Assalamu Alaikum means 'Peace be upon you'"
        )
    ]
    
    # Run the quiz
    result = run_quiz(questions)
    print(f"Result: {result}")
    
    # Generate certificate
    print("\nCertificate:")
    certificate = generate_certificate("Ahmed", 3, 3)
    print(certificate)

# Run the quiz system
islamic_quiz_system()
print()

print("🎉 All Islamic Applications Completed!")
print("📚 These applications show how functions can be used in real Islamic scenarios")
print("🕌 Functions help you create powerful and reusable Islamic tools!")
print("📖 Keep learning and applying programming to Islamic education!") 