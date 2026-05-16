# Module 5 - Lesson 5.5
# Learning objective: for, range(), lists

for i in range(1, 6):
    print("Number:", i)

for x in range(5):
    print("x =", x)

# Even numbers 2,4,6,8,10
for num in range(2, 11, 2):
    print("Even:", num)

# List — school subjects
subjects = ["Math", "Urdu", "Science", "Islamiat", "English"]
for subject in subjects:
    print(f"Studying {subject}")

# Madrasa subjects
islamic_subjects = ["Quran", "Hadith", "Fiqh"]
for subj in islamic_subjects:
    print(f"Lesson: {subj}")

# Pakistani cities
cities = ["Lahore", "Karachi", "Peshawar", "Quetta"]
for city in cities:
    print(f"City: {city}")

# Each character in a string
word = "Pakistan"
for letter in word:
    print(letter)

# Practice:
# Make a list of 3 favourite foods; print each with for loop

