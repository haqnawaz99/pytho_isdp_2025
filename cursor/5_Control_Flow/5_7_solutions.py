# Module 5 - Quiz solutions

# Q1
age = 12
if age >= 10:
    print("Can start advanced class")
else:
    print("Too young")

# Q2
marks = 45
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Q3
time = "Asr"
if time == "Fajr":
    print("Time for Fajr")
elif time == "Dhuhr":
    print("Time for Dhuhr")
elif time == "Asr":
    print("Time for Asr")
elif time == "Maghrib":
    print("Time for Maghrib")
elif time == "Isha":
    print("Time for Isha")
else:
    print("Unknown time")

# Q4
study_hours = 3
if study_hours >= 2 and study_hours <= 5:
    print("Good session")

# Q5
attended = True
homework = False
if attended and homework:
    print("Perfect")
else:
    print("Keep trying")

# Q6
count = 1
while count <= 5:
    print(count)
    count += 1

# Q7
for i in range(1, 4):
    print(f"Number {i}: Bismillah")

# Q8
subjects = ["Quran", "Hadith", "Fiqh"]
for s in subjects:
    print(s)

# Q9
marks = int(input("Marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Needs work")

# Q10
for num in range(1, 11):
    if num % 2 == 0:
        print(num)
