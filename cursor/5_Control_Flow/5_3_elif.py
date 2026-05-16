# Module 5 - Lesson 5.3
# Learning objective: if / elif / else chains

time_of_day = "evening"
if time_of_day == "morning":
    print("Good morning")
elif time_of_day == "afternoon":
    print("Good afternoon")
elif time_of_day == "evening":
    print("Good evening")
else:
    print("Good night")

# Grades from marks
score = int(input("Enter marks (0-100): "))
if score >= 90:
    print("Grade: A - Excellent")
elif score >= 80:
    print("Grade: B - Very good")
elif score >= 70:
    print("Grade: C - Good")
elif score >= 50:
    print("Grade: D - Pass")
else:
    print("Grade: F - Need improvement")

# Transport
transport = input("How did you come? (bus van walk): ")
if transport == "bus":
    print("Bus fare saved in diary")
elif transport == "van":
    print("Van pickup")
elif transport == "walk":
    print("Healthy walk!")
else:
    print("Other transport")

# Practice:
# Ask favourite sport: cricket / football / hockey — print one line each with elif

