# Module 2 - Lesson 2.3
# Learning objective: len() on variables; str() or comma in print

# Fixed string in variable
book = "Tafsir Ibn Kathir"
print(len(book))

# With str() and +
name = "Sara"
print("Letters in name: " + str(len(name)))

# With comma (easier)
city = "Karachi"
print("Letters in city:", len(city))

# With input
user_name = input("Enter your name: ")
print("Your name has", len(user_name), "characters")

surah = input("Enter a Surah name: ")
print("Length of Surah name:", len(surah))

# Store length in another variable
school = "Sindh Madressatul Islam"
school_length = len(school)
print("School name length:", school_length)

# Practice:
# Ask for favourite sport; print how many characters it has

