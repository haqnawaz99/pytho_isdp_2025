# Module 7 - Lesson 7.2
# Learning objective: append, remove, sort, for loop on list

books = ["Tafsir", "Hadith"]
print("Start:", books)

books.append("Fiqh")
print("After append:", books)

books.remove("Hadith")
print("After remove:", books)

# More items
class_students = ["Ali", "Sara", "Hassan"]
class_students.append("Aisha")
print(class_students)

numbers = [45, 12, 88, 30]
numbers.sort()
print("Sorted:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

# Loop
print("--- Subjects ---")
subjects = ["Math", "Urdu", "Science", "Islamiat"]
for sub in subjects:
    print(f"Studying {sub}")

# Loop with index using range
for i in range(len(subjects)):
    print(i, subjects[i])

# Practice:
# Start list ["cricket", "football"]; append "hockey"; loop and print each

