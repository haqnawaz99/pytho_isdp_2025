# Module 6 - Lesson 6.4
# Learning objective: default parameter values

def greet(name="Student"):
    print(f"Welcome, {name}")

greet("Ahmed")
greet()

def show_prayer(prayer="Fajr"):
    print(f"Reminder: {prayer} prayer")

show_prayer("Maghrib")
show_prayer()

def book_total(quantity, price_each=100):
    return quantity * price_each

print("Default price:", book_total(5))
print("Custom price:", book_total(3, 250))

def make_label(item="book", count=1):
    return f"{count} x {item}"

print(make_label())
print(make_label("notebook", 4))

# Practice:
# def city_greeting(city="Lahore"): print welcome
# Call with and without argument

