# Project 4 - Student Name Formatter (SOLUTION)

print("=== Student Name Formatter ===")

raw_name = input("Enter your full name: ")
clean_name = raw_name.strip().title()

print(f"Formatted name: {clean_name}")
print(f"Number of letters: {len(clean_name)}")

if len(clean_name) < 3:
    print("Name seems too short.")
else:
    print("Name looks good.")

school = input("School or madrasa name: ").strip().title()
print(f"{clean_name} studies at {school}.")
