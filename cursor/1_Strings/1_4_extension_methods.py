# Module 1 - Lesson 1.4 (OPTIONAL / Extension)
# Learning objective: split, join, startswith, find, count
# Teach after students are comfortable with core lessons 1.1-1.3

print("Ahmed, Fatima, Ali".split(", "))
print(" and ".join(["Lahore", "Karachi", "Islamabad"]))

print("Assalamu Alaikum".startswith("Assalamu"))
print("Pakistan".endswith("stan"))

print("Cricket in Pakistan".find("Pakistan"))
print("banana".count("a"))

# Character checks
print("Ahmed".isalpha())
print("2025".isdigit())
print("Assalamu Alaikum".isalpha())  # False because of space

