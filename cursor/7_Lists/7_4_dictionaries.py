# Module 7 - Lesson 7.4
# Learning objective: dict create, access, get, update, loop

student = {
    "name": "Ahmed",
    "age": 15,
    "city": "Lahore",
    "subject": "Quran"
}
print(student)
print(student["name"])
print(student.get("age"))
print(student.get("phone", "Not given"))

student["marks"] = 88
student["city"] = "Multan"
print(student)

# Prayer times
prayer_times = {
    "Fajr": "5:15",
    "Dhuhr": "12:30",
    "Asr": "15:45",
    "Maghrib": "18:20",
    "Isha": "20:00"
}
print(prayer_times["Maghrib"])

# Loop keys and values
for prayer in prayer_times:
    print(prayer, prayer_times[prayer])

for key, value in prayer_times.items():
    print(f"{key}: {value}")

# School fee example
fee_record = {
    "student": "Sara",
    "class": "7-A",
    "fee_paid": True,
    "amount": 3000
}
print(f"{fee_record['student']} paid {fee_record['amount']} rupees")

# Practice:
# Dict for one book: title, author, pages — print each key and value in a loop

