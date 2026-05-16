# Module 3 - Lesson 3.4 (OPTIONAL)
# Learning objective: basic bool() conversion

print(bool(""))        # False
print(bool("hello"))   # True
print(bool("False"))   # True — non-empty string!

print(bool(0))         # False
print(bool(42))        # True

is_present = True
print("Present:", is_present)
print(type(is_present))

