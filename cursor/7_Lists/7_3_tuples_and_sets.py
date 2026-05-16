# Module 7 - Lesson 7.3 (INTRO)
# Learning objective: tuple vs list; set for unique items

# Tuple — fixed order, use () 
prayer_names = ("Fajr", "Dhuhr", "Asr", "Maghrib", "Isha")
print(prayer_names[0])
print(len(prayer_names))

student_tuple = ("Ahmed", 15, "Multan")
print(student_tuple[0], student_tuple[2])

# Cannot change tuple item — this would error:
# prayer_names[0] = "X"

# Set — unique values only
attendance_tags = {"Ali", "Sara", "Ali", "Hassan"}
print(attendance_tags)

cities_seen = set()
cities_seen.add("Lahore")
cities_seen.add("Lahore")
cities_seen.add("Karachi")
print(cities_seen)

# Practice:
# Create a tuple of 3 Pakistani provinces; print the second one

