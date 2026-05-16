# Module 6 - Lesson 6.2
# Learning objective: functions with parameters

def greet_person(name):
    print(f"Assalamu Alaikum {name}")

greet_person("Ahmed")
greet_person("Fatima")

def show_city(city):
    print(f"Beautiful city: {city}")

show_city("Lahore")
show_city("Karachi")

def print_marks(student, marks):
    print(f"{student} scored {marks}")

print_marks("Ali", 88)
print_marks("Sara", 92)

def total_cost(price, quantity):
    total = price * quantity
    print(f"Total: {total} rupees")

total_cost(250, 6)

def study_message(hours):
    print(f"You studied {hours} hours")
    if hours >= 2:
        print("Good effort!")
    else:
        print("Try a bit more tomorrow")

study_message(3)
study_message(1)

# Practice:
# Function show_subject(name) that prints "Lesson: ..."
# Call with three different subjects

