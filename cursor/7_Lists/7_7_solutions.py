# Module 7 - Quiz solutions

# Q1
cities = ["Lahore", "Karachi", "Islamabad"]
print(cities[1])

# Q2
marks = [70, 85, 90]
print(len(marks))
print(marks[-1])

# Q3
fruits = ["mango", "apple"]
fruits.append("banana")
fruits.remove("apple")
print(fruits)

# Q4
nums = [45, 12, 88]
nums.sort()
print(nums)

# Q5
for sub in ["Quran", "Hadith", "Fiqh"]:
    print(f"Subject: {sub}")

# Q6
place = ("Lahore", "Punjab")
print(place[0], place[1])

# Q7
student = {"name": "Ahmed", "age": 14, "city": "Multan"}
print(student["name"])

# Q8
student["marks"] = 80
print(student)

# Q9
times = {"Fajr": 5, "Dhuhr": 12}
for k in times:
    print(k, times[k])

# Q10
class_list = [{"name": "Ali", "marks": 40}, {"name": "Sara", "marks": 75}]
for p in class_list:
    if p["marks"] >= 50:
        print(p["name"], "Pass")
    else:
        print(p["name"], "Fail")
