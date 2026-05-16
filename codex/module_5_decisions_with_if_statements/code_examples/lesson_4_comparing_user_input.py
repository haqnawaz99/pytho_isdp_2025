answer = input("Did you complete homework? (yes/no): ")

if answer == "yes":
    print("Well done")
else:
    print("Please complete it soon")

marks = int(input("Enter your marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")
