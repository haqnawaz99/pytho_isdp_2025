# Module 4 - Lesson 4.4
# Learning objective: and, or, not

has_attended = True
has_homework = True
print("AND both true:", has_attended and has_homework)

has_attended = True
has_homework = False
print("AND one false:", has_attended and has_homework)

print("OR one true:", True or False)
print("OR both false:", False or False)

is_fasting = False
print("NOT fasting:", not is_fasting)

# Comparisons + logic
age = 14
is_teen = age >= 10 and age <= 19
print("Teenager:", is_teen)

marks = 82
passed = marks >= 50
print("Passed:", passed)

# Eligibility: attended AND (homework OR read_quran)
attended = True
homework = False
read_quran = True
eligible = attended and (homework or read_quran)
print("Eligible:", eligible)

# School: rain OR holiday -> no outdoor game
heavy_rain = False
is_holiday = True
no_game = heavy_rain or is_holiday
print("No outdoor game:", no_game)

# Practice:
# marks = 45, attendance = True
# Print True if passed (marks>=50) AND attended

