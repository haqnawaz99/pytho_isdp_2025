# 6_7_islamic_applications.py

# ==================================================
# 📝 Lists: Islamic Applications
# ==================================================
# 🎯 Learning Objective: Apply data structures to Islamic real-world problems
# 📚 Islamic Context: Practical applications in Islamic education and daily life

print("🕌 Islamic Applications of Data Structures")
print("=" * 50)

# ======================================
# 🔹 Application 1: Islamic School Management System
# ======================================

print("🔹 Application 1: Islamic School Management System")
print("-" * 50)

# School database using nested dictionaries
islamic_school = {
    "name": "Al-Noor Islamic School",
    "location": "Karachi, Pakistan",
    "established": 2010,
    "departments": {
        "Quran": {
            "head": "Maulana Ahmed",
            "students": 45,
            "subjects": ["Tajweed", "Memorization", "Tafsir"]
        },
        "Hadith": {
            "head": "Maulana Ali",
            "students": 32,
            "subjects": ["Sahih Bukhari", "Sahih Muslim", "Abu Dawud"]
        },
        "Fiqh": {
            "head": "Maulana Hassan",
            "students": 28,
            "subjects": ["Hanafi Fiqh", "Islamic Law", "Fatwa"]
        }
    },
    "facilities": ["Library", "Prayer Hall", "Computer Lab", "Sports Ground"]
}

print("🏫 Islamic School Information:")
print(f"School: {islamic_school['name']}")
print(f"Location: {islamic_school['location']}")
print(f"Established: {islamic_school['established']}")

print("\n📚 Department Information:")
for dept, info in islamic_school['departments'].items():
    print(f"  {dept} Department:")
    print(f"    Head: {info['head']}")
    print(f"    Students: {info['students']}")
    print(f"    Subjects: {', '.join(info['subjects'])}")

print(f"\n🏢 Facilities: {', '.join(islamic_school['facilities'])}")

# Calculate total students
total_students = sum(dept['students'] for dept in islamic_school['departments'].values())
print(f"\n📊 Total Students: {total_students}")
print()

# ======================================
# 🔹 Application 2: Prayer Time Management System
# ======================================

print("🔹 Application 2: Prayer Time Management System")
print("-" * 50)

# Prayer times for different cities
prayer_times_db = {
    "Karachi": {
        "Fajr": "5:15 AM",
        "Sunrise": "6:45 AM",
        "Dhuhr": "12:30 PM",
        "Asr": "3:45 PM",
        "Maghrib": "6:30 PM",
        "Isha": "8:00 PM"
    },
    "Lahore": {
        "Fajr": "5:00 AM",
        "Sunrise": "6:30 AM",
        "Dhuhr": "12:15 PM",
        "Asr": "3:30 PM",
        "Maghrib": "6:15 PM",
        "Isha": "7:45 PM"
    },
    "Islamabad": {
        "Fajr": "4:45 AM",
        "Sunrise": "6:15 AM",
        "Dhuhr": "12:00 PM",
        "Asr": "3:15 PM",
        "Maghrib": "6:00 PM",
        "Isha": "7:30 PM"
    }
}

# Current time simulation
current_time = "3:30 PM"
current_city = "Karachi"

print(f"🕐 Prayer Times for {current_city}:")
for prayer, time in prayer_times_db[current_city].items():
    print(f"  {prayer}: {time}")

# Find next prayer
def find_next_prayer(city, current_time):
    """Find the next prayer based on current time"""
    prayer_order = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
    current_hour = int(current_time.split(":")[0])
    current_minute = int(current_time.split(":")[1].split(" ")[0])
    current_period = current_time.split(" ")[1]
    
    # Convert to 24-hour format
    if current_period == "PM" and current_hour != 12:
        current_hour += 12
    elif current_period == "AM" and current_hour == 12:
        current_hour = 0
    
    current_minutes = current_hour * 60 + current_minute
    
    for prayer in prayer_order:
        prayer_time = prayer_times_db[city][prayer]
        prayer_hour = int(prayer_time.split(":")[0])
        prayer_minute = int(prayer_time.split(":")[1].split(" ")[0])
        prayer_period = prayer_time.split(" ")[1]
        
        if prayer_period == "PM" and prayer_hour != 12:
            prayer_hour += 12
        elif prayer_period == "AM" and prayer_hour == 12:
            prayer_hour = 0
        
        prayer_minutes = prayer_hour * 60 + prayer_minute
        
        if prayer_minutes > current_minutes:
            return prayer, prayer_time
    
    return "Fajr", prayer_times_db[city]["Fajr"]  # Next day's Fajr

next_prayer, next_time = find_next_prayer(current_city, current_time)
print(f"\n⏰ Current Time: {current_time}")
print(f"🕌 Next Prayer: {next_prayer} at {next_time}")
print()

# ======================================
# 🔹 Application 3: Islamic Calendar System
# ======================================

print("🔹 Application 3: Islamic Calendar System")
print("-" * 50)

# Islamic months with their characteristics
islamic_calendar = {
    "Muharram": {
        "days": 30,
        "special_days": ["10th - Day of Ashura"],
        "significance": "First month of Islamic year",
        "recommended_acts": ["Fasting on 9th and 10th", "Charity", "Prayer"]
    },
    "Safar": {
        "days": 29,
        "special_days": [],
        "significance": "Second month",
        "recommended_acts": ["Regular prayers", "Good deeds"]
    },
    "Rabi al-Awwal": {
        "days": 30,
        "special_days": ["12th - Birth of Prophet Muhammad (PBUH)"],
        "significance": "Month of Prophet's birth",
        "recommended_acts": ["Sending blessings on Prophet", "Charity", "Learning Seerah"]
    },
    "Rabi al-Thani": {
        "days": 29,
        "special_days": [],
        "significance": "Fourth month",
        "recommended_acts": ["Regular worship", "Good character"]
    },
    "Jumada al-Awwal": {
        "days": 30,
        "special_days": [],
        "significance": "Fifth month",
        "recommended_acts": ["Prayer", "Quran recitation"]
    },
    "Jumada al-Thani": {
        "days": 29,
        "special_days": [],
        "significance": "Sixth month",
        "recommended_acts": ["Regular worship", "Good deeds"]
    },
    "Rajab": {
        "days": 30,
        "special_days": ["27th - Laylat al-Miraj"],
        "significance": "Sacred month",
        "recommended_acts": ["Fasting", "Prayer", "Charity"]
    },
    "Shaban": {
        "days": 29,
        "special_days": ["15th - Laylat al-Bara'ah"],
        "significance": "Month before Ramadan",
        "recommended_acts": ["Fasting", "Prayer", "Preparation for Ramadan"]
    },
    "Ramadan": {
        "days": 30,
        "special_days": ["1st-30th - Month of Fasting", "27th - Laylat al-Qadr"],
        "significance": "Month of fasting and Quran",
        "recommended_acts": ["Fasting", "Taraweeh", "Quran recitation", "Charity"]
    },
    "Shawwal": {
        "days": 29,
        "special_days": ["1st - Eid al-Fitr"],
        "significance": "Month after Ramadan",
        "recommended_acts": ["6 days of fasting", "Eid celebration", "Charity"]
    },
    "Dhul Qadah": {
        "days": 30,
        "special_days": [],
        "significance": "Sacred month",
        "recommended_acts": ["Regular worship", "Good deeds"]
    },
    "Dhul Hijjah": {
        "days": 30,
        "special_days": ["10th - Eid al-Adha", "9th - Day of Arafah"],
        "significance": "Month of Hajj",
        "recommended_acts": ["Hajj", "Sacrifice", "Fasting on 9th", "Charity"]
    }
}

# Current Islamic month (example)
current_islamic_month = "Ramadan"

print(f"📅 Islamic Calendar - {current_islamic_month}:")
month_info = islamic_calendar[current_islamic_month]
print(f"Days: {month_info['days']}")
print(f"Significance: {month_info['significance']}")
print(f"Special Days: {', '.join(month_info['special_days'])}")
print(f"Recommended Acts: {', '.join(month_info['recommended_acts'])}")

# Find sacred months
sacred_months = [month for month, info in islamic_calendar.items() 
                if "Sacred" in info['significance']]
print(f"\n🕊 Sacred Months: {', '.join(sacred_months)}")

# Count total days in Islamic year
total_days = sum(info['days'] for info in islamic_calendar.values())
print(f"📊 Total Days in Islamic Year: {total_days}")
print()

# ======================================
# 🔹 Application 4: Student Performance Tracking
# ======================================

print("🔹 Application 4: Student Performance Tracking")
print("-" * 50)

# Student database with performance tracking
students_database = [
    {
        "id": "ST001",
        "name": "Ahmed Hassan",
        "age": 15,
        "grade": "10th",
        "subjects": {
            "Quran": {
                "grades": [85, 92, 88, 95, 90],
                "attendance": 95,
                "teacher": "Maulana Ali"
            },
            "Hadith": {
                "grades": [78, 85, 82, 88, 85],
                "attendance": 88,
                "teacher": "Maulana Ahmed"
            },
            "Fiqh": {
                "grades": [90, 88, 92, 85, 89],
                "attendance": 92,
                "teacher": "Maulana Hassan"
            }
        },
        "prayer_attendance": {
            "Fajr": 85,
            "Dhuhr": 90,
            "Asr": 88,
            "Maghrib": 92,
            "Isha": 87
        }
    },
    {
        "id": "ST002",
        "name": "Fatima Zahra",
        "age": 14,
        "grade": "9th",
        "subjects": {
            "Quran": {
                "grades": [92, 95, 90, 88, 93],
                "attendance": 98,
                "teacher": "Maulana Ali"
            },
            "Hadith": {
                "grades": [88, 92, 85, 90, 87],
                "attendance": 95,
                "teacher": "Maulana Ahmed"
            },
            "Fiqh": {
                "grades": [85, 88, 90, 87, 89],
                "attendance": 90,
                "teacher": "Maulana Hassan"
            }
        },
        "prayer_attendance": {
            "Fajr": 92,
            "Dhuhr": 95,
            "Asr": 90,
            "Maghrib": 95,
            "Isha": 93
        }
    }
]

print("📊 Student Performance Report:")
for student in students_database:
    print(f"\n👤 {student['name']} (ID: {student['id']})")
    print(f"   Grade: {student['grade']}, Age: {student['age']}")
    
    # Calculate subject averages
    print("   📚 Subject Performance:")
    for subject, info in student['subjects'].items():
        avg_grade = sum(info['grades']) / len(info['grades'])
        print(f"      {subject}: {avg_grade:.1f}% (Teacher: {info['teacher']})")
    
    # Calculate prayer attendance average
    prayer_avg = sum(student['prayer_attendance'].values()) / len(student['prayer_attendance'])
    print(f"   🕌 Prayer Attendance: {prayer_avg:.1f}%")
    
    # Performance rating
    subject_avg = sum(sum(info['grades']) / len(info['grades']) 
                     for info in student['subjects'].values()) / len(student['subjects'])
    
    if subject_avg >= 90 and prayer_avg >= 90:
        rating = "🌟 Excellent"
    elif subject_avg >= 80 and prayer_avg >= 80:
        rating = "✅ Good"
    else:
        rating = "💪 Needs Improvement"
    
    print(f"   📈 Overall Rating: {rating}")

print()

# ======================================
# 🔹 Application 5: Islamic Library Management
# ======================================

print("🔹 Application 5: Islamic Library Management")
print("-" * 50)

# Library catalog system
islamic_library = {
    "books": {
        "Quran": {
            "copies": 10,
            "available": 7,
            "category": "Primary Source",
            "language": ["Arabic", "Urdu", "English"],
            "location": "Section A-1"
        },
        "Sahih Bukhari": {
            "copies": 5,
            "available": 2,
            "category": "Hadith",
            "language": ["Arabic", "Urdu", "English"],
            "location": "Section B-1"
        },
        "Sahih Muslim": {
            "copies": 5,
            "available": 3,
            "category": "Hadith",
            "language": ["Arabic", "Urdu", "English"],
            "location": "Section B-1"
        },
        "Tafsir Ibn Kathir": {
            "copies": 3,
            "available": 1,
            "category": "Tafsir",
            "language": ["Arabic", "Urdu"],
            "location": "Section A-2"
        },
        "Fiqh al-Islami": {
            "copies": 4,
            "available": 4,
            "category": "Fiqh",
            "language": ["Arabic", "Urdu"],
            "location": "Section C-1"
        }
    },
    "members": {
        "M001": {"name": "Ahmed Ali", "books_borrowed": ["Quran", "Sahih Bukhari"]},
        "M002": {"name": "Fatima Hassan", "books_borrowed": ["Sahih Muslim"]},
        "M003": {"name": "Ali Ahmed", "books_borrowed": []}
    }
}

print("📚 Islamic Library Catalog:")
for book, info in islamic_library['books'].items():
    borrowed = info['copies'] - info['available']
    print(f"  📖 {book}")
    print(f"     Category: {info['category']}")
    print(f"     Available: {info['available']}/{info['copies']} copies")
    print(f"     Languages: {', '.join(info['language'])}")
    print(f"     Location: {info['location']}")

print(f"\n👥 Library Members:")
for member_id, member_info in islamic_library['members'].items():
    print(f"  {member_info['name']} (ID: {member_id})")
    if member_info['books_borrowed']:
        print(f"    Borrowed: {', '.join(member_info['books_borrowed'])}")
    else:
        print(f"    No books currently borrowed")

# Library statistics
total_books = sum(info['copies'] for info in islamic_library['books'].values())
total_available = sum(info['available'] for info in islamic_library['books'].values())
total_borrowed = total_books - total_available

print(f"\n📊 Library Statistics:")
print(f"  Total Books: {total_books}")
print(f"  Available: {total_available}")
print(f"  Borrowed: {total_borrowed}")
print(f"  Utilization: {(total_borrowed/total_books)*100:.1f}%")

print()

# ======================================
# 🔹 Application 6: Islamic Event Management
# ======================================

print("🔹 Application 6: Islamic Event Management")
print("-" * 50)

# Islamic events calendar
islamic_events = {
    "Eid al-Fitr": {
        "date": "1st Shawwal",
        "type": "Celebration",
        "activities": ["Eid Prayer", "Family Gatherings", "Charity", "Feasting"],
        "preparation_days": 1,
        "significance": "End of Ramadan fasting"
    },
    "Eid al-Adha": {
        "date": "10th Dhul Hijjah",
        "type": "Celebration",
        "activities": ["Eid Prayer", "Sacrifice", "Charity", "Family Time"],
        "preparation_days": 3,
        "significance": "Commemoration of Prophet Ibrahim's sacrifice"
    },
    "Laylat al-Qadr": {
        "date": "27th Ramadan",
        "type": "Worship",
        "activities": ["Night Prayer", "Quran Recitation", "Dhikr", "Charity"],
        "preparation_days": 0,
        "significance": "Night of Power"
    },
    "Day of Ashura": {
        "date": "10th Muharram",
        "type": "Commemoration",
        "activities": ["Fasting", "Prayer", "Charity", "Reflection"],
        "preparation_days": 1,
        "significance": "Day of fasting and reflection"
    },
    "Mawlid al-Nabi": {
        "date": "12th Rabi al-Awwal",
        "type": "Celebration",
        "activities": ["Seerah Lectures", "Charity", "Community Gatherings"],
        "preparation_days": 7,
        "significance": "Birth of Prophet Muhammad (PBUH)"
    }
}

print("📅 Islamic Events Calendar:")
for event, details in islamic_events.items():
    print(f"\n🎉 {event}")
    print(f"   Date: {details['date']}")
    print(f"   Type: {details['type']}")
    print(f"   Significance: {details['significance']}")
    print(f"   Activities: {', '.join(details['activities'])}")
    print(f"   Preparation Days: {details['preparation_days']}")

# Event statistics
celebration_events = [event for event, details in islamic_events.items() 
                     if details['type'] == 'Celebration']
worship_events = [event for event, details in islamic_events.items() 
                 if details['type'] == 'Worship']

print(f"\n📊 Event Statistics:")
print(f"  Total Events: {len(islamic_events)}")
print(f"  Celebrations: {len(celebration_events)}")
print(f"  Worship Events: {len(worship_events)}")

print()

# ======================================
# 🔹 Application 7: Islamic Finance Tracker
# ======================================

print("🔹 Application 7: Islamic Finance Tracker")
print("-" * 50)

# Zakat and charity tracking system
islamic_finance = {
    "zakat_calculation": {
        "gold_threshold": 87.48,  # grams
        "silver_threshold": 612.36,  # grams
        "cash_threshold": 50000,  # PKR
        "rate": 0.025  # 2.5%
    },
    "charity_categories": {
        "Zakat": {
            "amount": 25000,
            "frequency": "Annual",
            "recipients": ["Poor", "Needy", "Debtors", "Travelers"],
            "calculation_basis": "Wealth"
        },
        "Sadaqah": {
            "amount": 5000,
            "frequency": "Monthly",
            "recipients": ["Charity Organizations", "Mosques", "Schools"],
            "calculation_basis": "Voluntary"
        },
        "Fitra": {
            "amount": 200,
            "frequency": "Annual (Eid al-Fitr)",
            "recipients": ["Poor", "Needy"],
            "calculation_basis": "Per Person"
        }
    },
    "monthly_donations": [
        {"month": "January", "amount": 5000, "category": "Sadaqah"},
        {"month": "February", "amount": 3000, "category": "Sadaqah"},
        {"month": "March", "amount": 7000, "category": "Sadaqah"},
        {"month": "April", "amount": 4000, "category": "Sadaqah"},
        {"month": "May", "amount": 6000, "category": "Sadaqah"},
        {"month": "June", "amount": 8000, "category": "Sadaqah"}
    ]
}

print("💰 Islamic Finance Management:")
print(f"\n📋 Zakat Calculation Parameters:")
for param, value in islamic_finance['zakat_calculation'].items():
    if param == "rate":
        print(f"  {param.title()}: {value*100}%")
    else:
        print(f"  {param.replace('_', ' ').title()}: {value}")

print(f"\n🎯 Charity Categories:")
for category, details in islamic_finance['charity_categories'].items():
    print(f"  {category}:")
    print(f"    Amount: PKR {details['amount']:,}")
    print(f"    Frequency: {details['frequency']}")
    print(f"    Recipients: {', '.join(details['recipients'])}")

# Calculate total annual charity
annual_charity = sum(details['amount'] for details in islamic_finance['charity_categories'].values())
monthly_donations_total = sum(donation['amount'] for donation in islamic_finance['monthly_donations'])
total_annual = annual_charity + monthly_donations_total

print(f"\n📊 Annual Charity Summary:")
print(f"  Fixed Charity: PKR {annual_charity:,}")
print(f"  Monthly Donations: PKR {monthly_donations_total:,}")
print(f"  Total Annual: PKR {total_annual:,}")

# Monthly donation trend
print(f"\n📈 Monthly Donation Trend:")
for donation in islamic_finance['monthly_donations']:
    print(f"  {donation['month']}: PKR {donation['amount']:,}")

print()

# ======================================
# 🔹 Application 8: Islamic Learning Progress Tracker
# ======================================

print("🔹 Application 8: Islamic Learning Progress Tracker")
print("-" * 50)

# Learning progress tracking system
learning_progress = {
    "student_id": "ST001",
    "name": "Ahmed Hassan",
    "learning_goals": {
        "Quran_Memorization": {
            "target": "Complete Juz 30",
            "current": "Juz 30 - 15 pages",
            "progress": 75,
            "deadline": "2024-12-31"
        },
        "Hadith_Study": {
            "target": "Complete Sahih Bukhari Book 1",
            "current": "Sahih Bukhari Book 1 - 50 hadith",
            "progress": 60,
            "deadline": "2024-10-31"
        },
        "Arabic_Language": {
            "target": "Basic Arabic Grammar",
            "current": "Basic Grammar - 8 lessons",
            "progress": 80,
            "deadline": "2024-11-30"
        }
    },
    "daily_activities": {
        "Quran_Recitation": {
            "target_minutes": 30,
            "average_minutes": 25,
            "consistency": 85
        },
        "Prayer_Learning": {
            "target_minutes": 15,
            "average_minutes": 12,
            "consistency": 80
        },
        "Islamic_Reading": {
            "target_minutes": 20,
            "average_minutes": 18,
            "consistency": 90
        }
    },
    "achievements": [
        "Completed Juz 29",
        "Memorized 50 hadith",
        "Learned basic Arabic alphabet",
        "Completed Islamic etiquette course"
    ]
}

print("📚 Learning Progress Report:")
print(f"Student: {learning_progress['name']} (ID: {learning_progress['student_id']})")

print(f"\n🎯 Learning Goals:")
for goal, details in learning_progress['learning_goals'].items():
    print(f"  {goal.replace('_', ' ')}:")
    print(f"    Target: {details['target']}")
    print(f"    Current: {details['current']}")
    print(f"    Progress: {details['progress']}%")
    print(f"    Deadline: {details['deadline']}")

print(f"\n⏰ Daily Activities:")
for activity, details in learning_progress['daily_activities'].items():
    print(f"  {activity.replace('_', ' ')}:")
    print(f"    Target: {details['target_minutes']} minutes")
    print(f"    Average: {details['average_minutes']} minutes")
    print(f"    Consistency: {details['consistency']}%")

print(f"\n🏆 Achievements:")
for achievement in learning_progress['achievements']:
    print(f"  ✅ {achievement}")

# Overall progress calculation
overall_progress = sum(details['progress'] for details in learning_progress['learning_goals'].values()) / len(learning_progress['learning_goals'])
overall_consistency = sum(details['consistency'] for details in learning_progress['daily_activities'].values()) / len(learning_progress['daily_activities'])

print(f"\n📊 Overall Progress: {overall_progress:.1f}%")
print(f"📈 Overall Consistency: {overall_consistency:.1f}%")

if overall_progress >= 80 and overall_consistency >= 80:
    print("🌟 Excellent progress! Keep up the good work!")
elif overall_progress >= 60 and overall_consistency >= 60:
    print("✅ Good progress! Continue with dedication!")
else:
    print("💪 Keep working hard! Consistency is key!")

print()
print("🎉 Islamic Applications Completed!")
print("📚 These applications show how data structures help organize Islamic information!")
print("🕌 Use these concepts to create your own Islamic software solutions!") 