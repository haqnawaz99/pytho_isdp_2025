# Module 7 - Lesson 7.1
# Learning objective: create lists, index, len

prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
print(prayers)
print("First prayer:", prayers[0])
print("Third prayer:", prayers[2])
print("Last prayer:", prayers[-1])

cities = ["Lahore", "Karachi", "Peshawar", "Quetta"]
print("Second city:", cities[1])
print("Number of cities:", len(cities))

subjects = ["Quran", "Hadith", "Fiqh", "Math", "Urdu"]
print(subjects[0], subjects[-1])

marks = [88, 92, 76, 95]
print("First mark:", marks[0])
print("Average not yet - just list:", marks)

# Mixed types (allowed, but often we keep one type per list)
student_row = ["Fatima", 14, "Lahore"]
print(student_row[0], student_row[2])

# Practice:
# Make a list of 4 favourite foods; print first and last with index

