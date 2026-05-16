# Module 7 - Lesson 7.5
# Learning objective: list of dicts; dict containing a list

# List of student records
class_list = [
    {"name": "Ali", "marks": 85, "city": "Lahore"},
    {"name": "Sara", "marks": 92, "city": "Karachi"},
    {"name": "Hassan", "marks": 76, "city": "Multan"}
]

print("--- Class marks ---")
for pupil in class_list:
    print(f"{pupil['name']} from {pupil['city']}: {pupil['marks']}")

# Count how many passed (marks >= 50)
passed_count = 0
for pupil in class_list:
    if pupil["marks"] >= 50:
        passed_count += 1
print("Passed:", passed_count)

# Dictionary with a list inside
school = {
    "name": "Government High School",
    "city": "Peshawar",
    "subjects": ["Math", "Urdu", "Science", "Islamiat"],
    "strength": 450
}
print(school["name"])
print("First subject:", school["subjects"][0])

for sub in school["subjects"]:
    print("Subject:", sub)

# Simple Maktaba: book name -> copies
maktaba = {
    "Tafsir Ibn Kathir": 12,
    "Sahih Bukhari": 8,
    "Riyadus Saliheen": 15
}
total_copies = 0
for book, copies in maktaba.items():
    print(f"{book}: {copies} copies")
    total_copies += copies
print("Total copies:", total_copies)

# Practice:
# Add one more student dict to class_list; loop and print all names only

