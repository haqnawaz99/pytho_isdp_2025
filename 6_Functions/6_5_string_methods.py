# 5_5_string_methods.py

# ==================================================
# 📝 Functions: String Methods
# ==================================================
# 🎯 Learning Objective: Learn built-in string methods
# 📚 Islamic Context: Using Islamic text to understand string methods

print("📝 Welcome to String Methods")
print("=" * 50)

# ======================================
# 🔹 What are String Methods?
# ======================================

print("🔹 What are String Methods?")
print("-" * 30)
print("String methods are built-in functions for working with text.")
print("They help us format, search, and modify strings.")
print("In Islamic terms: Like different ways to read and understand Quranic text!")
print()

# ======================================
# 🔹 Example 1: upper() and lower()
# ======================================

print("🔹 Example 1: upper() and lower()")
print("-" * 30)

# Islamic greeting examples
greeting = "Assalamu Alaikum"
print(f"Original: {greeting}")
print(f"Upper case: {greeting.upper()}")
print(f"Lower case: {greeting.lower()}")

# Islamic name examples
name = "Ahmed"
print(f"\nName: {name}")
print(f"Upper case: {name.upper()}")
print(f"Lower case: {name.lower()}")
print()

# ======================================
# 🔹 Example 2: title() and capitalize()
# ======================================

print("🔹 Example 2: title() and capitalize()")
print("-" * 30)

# Islamic text examples
islamic_text = "the holy quran"
print(f"Original: {islamic_text}")
print(f"Title case: {islamic_text.title()}")
print(f"Capitalize: {islamic_text.capitalize()}")

# Islamic name examples
full_name = "ahmed ibn ali"
print(f"\nFull name: {full_name}")
print(f"Title case: {full_name.title()}")
print(f"Capitalize: {full_name.capitalize()}")
print()

# ======================================
# 🔹 Example 3: strip(), lstrip(), rstrip()
# ======================================

print("🔹 Example 3: strip(), lstrip(), rstrip()")
print("-" * 30)

# Islamic text with extra spaces
prayer_text = "   Fajr Prayer   "
print(f"Original: '{prayer_text}'")
print(f"Strip: '{prayer_text.strip()}'")
print(f"Left strip: '{prayer_text.lstrip()}'")
print(f"Right strip: '{prayer_text.rstrip()}'")

# Quran verse with spaces
quran_verse = "  Bismillah ir-Rahman ir-Raheem  "
print(f"\nQuran verse: '{quran_verse}'")
print(f"Cleaned: '{quran_verse.strip()}'")
print()

# ======================================
# 🔹 Example 4: replace()
# ======================================

print("🔹 Example 4: replace()")
print("-" * 30)

# Islamic text replacement
islamic_message = "Peace be upon you"
print(f"Original: {islamic_message}")
print(f"Replace 'Peace' with 'Salam': {islamic_message.replace('Peace', 'Salam')}")

# Prayer time replacement
prayer_schedule = "Fajr at 5 AM, Dhuhr at 12 PM, Asr at 3 PM"
print(f"\nOriginal: {prayer_schedule}")
print(f"Replace 'AM' with 'AM': {prayer_schedule.replace('AM', 'AM')}")
print(f"Replace 'PM' with 'PM': {prayer_schedule.replace('PM', 'PM')}")
print()

# ======================================
# 🔹 Example 5: split() and join()
# ======================================

print("🔹 Example 5: split() and join()")
print("-" * 30)

# Islamic names
islamic_names = "Ahmed, Fatima, Ali, Aisha, Hassan"
print(f"Original string: {islamic_names}")
names_list = islamic_names.split(", ")
print(f"Split into list: {names_list}")

# Join names back
joined_names = " and ".join(names_list)
print(f"Joined with 'and': {joined_names}")

# Islamic subjects
subjects = "Quran Hadith Fiqh Aqeedah Seerah"
print(f"\nSubjects: {subjects}")
subject_list = subjects.split()
print(f"Split into list: {subject_list}")
print()

# ======================================
# 🔹 Example 6: startswith() and endswith()
# ======================================

print("🔹 Example 6: startswith() and endswith()")
print("-" * 30)

# Check Islamic greetings
greeting1 = "Assalamu Alaikum"
greeting2 = "Wa Alaikum Assalam"
greeting3 = "Bismillah"

print(f"'{greeting1}' starts with 'Assalamu': {greeting1.startswith('Assalamu')}")
print(f"'{greeting2}' starts with 'Wa': {greeting2.startswith('Wa')}")
print(f"'{greeting3}' starts with 'Bismillah': {greeting3.startswith('Bismillah')}")

print(f"\n'{greeting1}' ends with 'Alaikum': {greeting1.endswith('Alaikum')}")
print(f"'{greeting2}' ends with 'Assalam': {greeting2.endswith('Assalam')}")
print()

# ======================================
# 🔹 Example 7: find() and index()
# ======================================

print("🔹 Example 7: find() and index()")
print("-" * 30)

# Find words in Islamic text
quran_text = "In the name of Allah, the Most Gracious, the Most Merciful"
print(f"Text: {quran_text}")

# Find positions
allah_position = quran_text.find("Allah")
print(f"'Allah' found at position: {allah_position}")

gracious_position = quran_text.find("Gracious")
print(f"'Gracious' found at position: {gracious_position}")

# Find non-existent word
not_found = quran_text.find("Quran")
print(f"'Quran' found at position: {not_found} (not found)")

# Using index (raises error if not found)
try:
    mercy_position = quran_text.index("Merciful")
    print(f"'Merciful' found at position: {mercy_position}")
except ValueError:
    print("'Merciful' not found")
print()

# ======================================
# 🔹 Example 8: count()
# ======================================

print("🔹 Example 8: count()")
print("-" * 30)

# Count occurrences in Islamic text
islamic_verse = "Allah is the Most Merciful, the Most Gracious, the Most Merciful"
print(f"Text: {islamic_verse}")

# Count words
allah_count = islamic_verse.count("Allah")
print(f"'Allah' appears {allah_count} times")

merciful_count = islamic_verse.count("Merciful")
print(f"'Merciful' appears {merciful_count} times")

the_count = islamic_verse.count("the")
print(f"'the' appears {the_count} times")
print()

# ======================================
# 🔹 Example 9: isalpha(), isdigit(), isspace()
# ======================================

print("🔹 Example 9: isalpha(), isdigit(), isspace()")
print("-" * 30)

# Check different types of strings
test_strings = ["Ahmed", "123", "   ", "Ahmed123", "Assalamu Alaikum"]

for text in test_strings:
    print(f"'{text}':")
    print(f"  Is alphabetic: {text.isalpha()}")
    print(f"  Is digit: {text.isdigit()}")
    print(f"  Is space: {text.isspace()}")
    print()

# ======================================
# 🔹 Example 10: format() and f-strings
# ======================================

print("🔹 Example 10: format() and f-strings")
print("-" * 30)

# Using format() method
student_name = "Ahmed"
subject = "Quran"
grade = 95

# Old format method
message1 = "Student {} got {}% in {}".format(student_name, grade, subject)
print(f"Format method: {message1}")

# F-string (modern way)
message2 = f"Student {student_name} got {grade}% in {subject}"
print(f"F-string: {message2}")

# Islamic greeting with format
greeting_template = "Assalamu Alaikum {}, may Allah bless you"
personalized_greeting = greeting_template.format("Ahmed")
print(f"Personalized greeting: {personalized_greeting}")
print()

# ======================================
# 🔹 Example 11: Multiple Methods Together
# ======================================

print("🔹 Example 11: Multiple Methods Together")
print("-" * 30)

# Clean and format Islamic text
messy_text = "  assalamu alaikum, brother!  "
print(f"Original messy text: '{messy_text}'")

# Apply multiple methods
cleaned_text = messy_text.strip().title()
print(f"After strip() and title(): '{cleaned_text}'")

# Replace and format
formatted_text = cleaned_text.replace("Brother", "Sister").replace("!", ".")
print(f"After replace(): '{formatted_text}'")

# Islamic name processing
raw_name = "  ahmed ibn ali al-hassan  "
print(f"\nRaw name: '{raw_name}'")

# Clean and format name
clean_name = raw_name.strip().title()
print(f"Clean name: '{clean_name}'")

# Split and join
name_parts = clean_name.split()
formatted_name = " ".join(name_parts)
print(f"Formatted name: '{formatted_name}'")
print()

# ======================================
# 🔹 Practice Exercise
# ======================================

print("📝 Practice Exercise:")
print("Use string methods to:")
print("1. Convert 'assalamu alaikum' to title case")
print("2. Remove extra spaces from '  Fajr Prayer  '")
print("3. Replace 'brother' with 'sister' in a greeting")
print("4. Split 'Quran,Hadith,Fiqh' into a list")

# Example solution:
print("\n🔹 Exercise Solutions:")

# 1. Title case
greeting = "assalamu alaikum"
print(f"1. '{greeting}' -> '{greeting.title()}'")

# 2. Remove spaces
prayer = "  Fajr Prayer  "
print(f"2. '{prayer}' -> '{prayer.strip()}'")

# 3. Replace word
message = "Assalamu Alaikum brother"
print(f"3. '{message}' -> '{message.replace('brother', 'sister')}'")

# 4. Split string
subjects = "Quran,Hadith,Fiqh"
subject_list = subjects.split(",")
print(f"4. '{subjects}' -> {subject_list}")

print()
print("🎉 Congratulations! You've learned string methods!")
print("📚 String methods help you work with text effectively!") 