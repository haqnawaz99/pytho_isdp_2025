# 4_5_while_loops.py

# ==================================================
# 📝 Control Flow: While Loops
# ==================================================
# 🎯 Learning Objective: Learn while loops for repetition
# 📚 Islamic Context: Using Islamic examples to understand loops

print("🔄 Welcome to While Loops")
print("=" * 50)

# ======================================
# 🔹 Basic While Loop
# ======================================

print("🔹 Basic While Loop Examples:")
print("-" * 30)

# Islamic example: Counting prayers
print("🕌 Counting Daily Prayers:")
prayer_count = 1

while prayer_count <= 5:
    print(f"Prayer {prayer_count}: Completed")
    prayer_count += 1

print()

# ======================================
# 🔹 While Loop with User Input
# ======================================

print("🔹 While Loop with User Input:")
print("-" * 30)

# Islamic example: Quran reading tracker
print("📖 Quran Reading Tracker:")
pages_read = 0
target_pages = 3

while pages_read < target_pages:
    print(f"Pages read: {pages_read}/{target_pages}")
    read_more = input("Did you read a page? (yes/no): ")
    
    if read_more == "yes":
        pages_read += 1
        print("✅ MashaAllah! Keep going")
    else:
        print("📖 Try to read one page")

print("🎉 Congratulations! You completed your daily Quran reading")

print()

# ======================================
# 🔹 While Loop with Condition
# ======================================

print("🔹 While Loop with Condition:")
print("-" * 30)

# Islamic example: Study session
print("📚 Study Session:")
study_time = 0
max_study_time = 60  # minutes

while study_time < max_study_time:
    print(f"Study time: {study_time} minutes")
    study_time += 15
    print("📖 15 minutes of studying completed")

print("⏰ Study session completed!")

print()

# ======================================
# 🔹 While Loop with Break
# ======================================

print("🔹 While Loop with Break:")
print("-" * 30)

# Islamic example: Prayer time check
print("🕌 Prayer Time Check:")
current_hour = 0

while True:
    if current_hour == 5:
        print("🌅 Time for Fajr prayer!")
        break
    elif current_hour == 12:
        print("☀️ Time for Dhuhr prayer!")
        break
    elif current_hour == 15:
        print("🌤️ Time for Asr prayer!")
        break
    elif current_hour == 18:
        print("🌆 Time for Maghrib prayer!")
        break
    elif current_hour == 20:
        print("🌙 Time for Isha prayer!")
        break
    
    print(f"Hour: {current_hour} - No prayer time yet")
    current_hour += 1

print()

# ======================================
# 🔹 While Loop with Continue
# ======================================

print("🔹 While Loop with Continue:")
print("-" * 30)

# Islamic example: Good deeds counter
print("🤝 Good Deeds Counter:")
deed_count = 0
attempts = 0

while attempts < 10:
    attempts += 1
    deed = input(f"Attempt {attempts}: What good deed did you do? (help/salam/study/none): ")
    
    if deed == "none":
        print("💝 Try to do a good deed")
        continue
    
    deed_count += 1
    print(f"✅ MashaAllah! Good deed #{deed_count}")

print(f"🎉 Total good deeds: {deed_count}")

print()

# ======================================
# 🔹 While Loop with Islamic Learning
# ======================================

print("🔹 While Loop with Islamic Learning:")
print("-" * 30)

# Islamic example: Surah memorization
print("📖 Surah Memorization Tracker:")
surah_number = 1
total_surahs = 5

while surah_number <= total_surahs:
    print(f"📚 Memorizing Surah {surah_number}")
    
    if surah_number == 1:
        print("   - Surah Al-Fatiha (The Opening)")
    elif surah_number == 2:
        print("   - Surah Al-Baqarah (The Cow)")
    elif surah_number == 3:
        print("   - Surah Al-Imran (The Family of Imran)")
    elif surah_number == 4:
        print("   - Surah An-Nisa (The Women)")
    elif surah_number == 5:
        print("   - Surah Al-Ma'idah (The Table Spread)")
    
    memorized = input(f"Have you memorized Surah {surah_number}? (yes/no): ")
    
    if memorized == "yes":
        print("✅ MashaAllah! Excellent progress")
        surah_number += 1
    else:
        print("📖 Keep practicing - you can do it!")

print("🎉 Congratulations! You've memorized 5 surahs!")

print()

# ======================================
# 🔹 While Loop with Counter
# ======================================

print("🔹 While Loop with Counter:")
print("-" * 30)

# Islamic example: Dhikr counter
print("🕌 Dhikr Counter:")
dhikr_count = 0
target_dhikr = 33

while dhikr_count < target_dhikr:
    dhikr_count += 1
    print(f"SubhanAllah #{dhikr_count}")
    
    if dhikr_count == 33:
        print("✅ Completed SubhanAllah 33 times")
        break

print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Create while loops for:")
print("1. Count from 1 to 10 (Islamic counting)")
print("2. Ask user to enter prayer times until they enter 'done'")
print("3. Count good deeds until reaching 5")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Islamic counting
print("1. Islamic Counting:")
count = 1
while count <= 10:
    print(f"Number {count}: Bismillah")
    count += 1

# 2. Prayer times
print("\n2. Prayer Times:")
prayer_times = []
while True:
    prayer = input("Enter prayer time (or 'done' to finish): ")
    if prayer == "done":
        break
    prayer_times.append(prayer)
    print(f"Added: {prayer}")

print(f"Prayer times: {prayer_times}")

# 3. Good deeds counter
print("\n3. Good Deeds Counter:")
good_deeds = 0
while good_deeds < 5:
    deed = input("What good deed did you do? ")
    good_deeds += 1
    print(f"Good deed #{good_deeds}: {deed}")

print("🎉 You've done 5 good deeds!")

print()
print("🎉 Congratulations! You've learned while loops!") 