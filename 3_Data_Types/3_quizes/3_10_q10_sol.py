# 3_1_q10_sol.py

# =======================================================
# ✅ Task 10: Greeting by Time (Solution)
# =======================================================

time = input("Enter time of day (morning, afternoon, night): ").lower()

if time == "morning":
    print("Good Morning!")
elif time == "afternoon":
    print("Good Afternoon!")
elif time == "night":
    print("Good Night!")
else:
    print("Invalid time entered.")